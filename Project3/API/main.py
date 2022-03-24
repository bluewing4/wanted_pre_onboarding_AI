import os
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import (
    ElectraConfig,
    ElectraTokenizer,
    ElectraForSequenceClassification
)
from main_modules import make_features, make_inputs, make_dataloader, predict
# from torch.utils.data import DataLoader, RandomSampler, SequentialSampler
# from torch.utils.data import TensorDataset 
# import numpy as np
import torch

# 같은 경로에 모델두고
# 터미널 ->  uvicorn help_check_copy:app --reload -> http://127.0.0.1:8000/docs

app = FastAPI()

args = {
  "task": "korsts",
  "data_dir": "data",
  "ckpt_dir": "ckpt",
  "train_file": "sts-train.tsv",
  "dev_file": "sts-dev.tsv",
  "test_file": "sts-test.tsv",
  "evaluate_test_during_training": False, 
  "eval_all_checkpoints": True,
  "save_optimizer": False,
  "do_lower_case": False,
  "do_train": True,
  "do_eval": True,
  "max_seq_len": 120,
  "num_train_epochs": 20,
  "weight_decay": 0.001,
  "gradient_accumulation_steps": 1,
  "adam_epsilon": 1e-8,
  "warmup_proportion": 0.2,
  "max_steps": -1,
  "max_grad_norm": 1.0,
  "no_cuda": False,
  "model_type": "koelectra-base-v3",
  "model_name_or_path": "monologg/koelectra-base-v3-discriminator",
  "output_dir": "koelectra-base-v3-korsts-ckpt",
  "seed": 42,
  "train_batch_size": 32,
  "eval_batch_size": 64,
  "logging_steps": 100,
  "save_steps": 100,
  "learning_rate": 5e-5
}

### PRE-LODAD ###
# check device
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")


# load checkpoint file
_CKPT_PATH = os.path.abspath(os.path.dirname(__file__))
checkpoint = torch.load(os.path.join(_CKPT_PATH, "basev3_model_ms_1.ckpt.16"), map_location=device)

# 모델 초기화
model_name = "monologg/koelectra-base-v3-discriminator"
model = ElectraForSequenceClassification.from_pretrained(model_name,  config=ElectraConfig.from_pretrained(model_name, num_labels=1)
    )
# 가중치 로드   
model.load_state_dict(checkpoint["model_state_dict"])

# 토커나이저 사전로드 
tokenizer = ElectraTokenizer.from_pretrained("monologg/koelectra-base-v3-discriminator", do_lower_case=False)



class Data(BaseModel):
    sentence:str  # user가 입력해야 할 문장

@app.post("/")  # url 지정
async def classifier(r1:Data, r2:Data): # 데이터 클래스의 인스턴스
    request1 = r1.sentence.strip()
    request2 = r2.sentence.strip()

    d_sent_pairs = [(request1, request2)]

    # 토크나이징
    d_batch_encoding = tokenizer([(request1, request2)],
                              max_length=128,
                              padding="max_length",    
                              add_special_tokens=True,
                              truncation=True,
                              )



    d_features = make_features(d_sent_pairs, d_batch_encoding) #[{1}, {2}]
    d_dataset = make_inputs(d_features)
    dev_dataloader = make_dataloader(d_dataset, mode='dev')
    preds = predict(args, model, d_dataset, 'test')

    if preds.tolist() >= 3:
        k = '유사함'
    elif preds.tolist() :
        k = '유사하지 않음'

    return {"Sentence1" : request1, "Sentence2" : request2, "문장유사도 점수(5점 만점 중)": preds.tolist(), "결론" : k}


# 확인
# classifier('이를 위해 3가지 협력 방향을 제안합니다.', '이를 위해, 우리는 세 가지 협력적인 방향을 제안합니다.')