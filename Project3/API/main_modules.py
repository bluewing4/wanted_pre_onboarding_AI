from torch.utils.data import DataLoader, SequentialSampler
from torch.utils.data import TensorDataset 
import numpy as np
import torch

# check device
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

def make_features(sent_pairs, batch_encoding):
    features = []
    for i in range(len(sent_pairs)):
        inputs = {k: batch_encoding[k][i] for k in batch_encoding}
        if "token_type_ids" not in inputs:
            inputs["token_type_ids"] = [0] * len(inputs["input_ids"])

        feature = {'input_ids':inputs['input_ids'],
                'attention_mask':inputs['attention_mask'],
                'token_type_ids':inputs['token_type_ids'],
                }
        
        features.append(feature)      
    return features


def make_inputs(features, output_mode:str="regression"):
    # inputs

    all_input_ids = torch.tensor([f['input_ids'] for f in features], dtype=torch.long) # 두 문장의 인풋아이디만 리스트에 넣음

    all_attention_mask = torch.tensor([f['attention_mask'] for f in features], dtype=torch.long)
    all_token_type_ids = torch.tensor([f['token_type_ids'] for f in features], dtype=torch.long)

    # dataset
    dataset = TensorDataset(all_input_ids, all_attention_mask, all_token_type_ids)
    return dataset



def make_dataloader(dataset, mode:str):
    if mode == "dev":
        dataloader = DataLoader(dataset = dataset,
                                sampler = SequentialSampler(dataset), 
                                batch_size = 64)
    return dataloader



def predict(args, model, dev_dataloader, mode, global_step=None):
    model.to(device)
    # for batch in dev_dataloader:
    for batch in dev_dataloader:
        batch = tuple(item for item in dev_dataloader)
        # no_grad
        with torch.no_grad():
            # inputs
            inputs = {
                "input_ids": dev_dataloader[0][0].unsqueeze(0),
                "attention_mask": dev_dataloader[0][1].unsqueeze(0),
                "token_type_ids": dev_dataloader[0][2].unsqueeze(0),
            }

            # outputs
            outputs = model(**inputs)
            logits = outputs.logits

        # preds and labels
        preds = logits.detach().cpu().numpy()
    preds = np.squeeze(preds)
    return preds 