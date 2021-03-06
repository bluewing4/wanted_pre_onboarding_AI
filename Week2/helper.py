# -*- coding: utf-8 -*-
"""helper

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IL_IzzMJPKKzvjVpLN9gYazHLLMtZ2Zf
"""

#!pip install transformers

# 스크립트 내 포함해야하는 함수
# - set_device()
# - load_clean_data()
# - label_evenly_balanced_dataset_sampler()
# - custom_collate_fn()
# 포함해야하는 클래스
# - CustomDataset
# - CustomClassifier

import os
import sys
import pandas as pd
import numpy as np 
import torch
import random

#- set_device()
def set_device():
  if torch.cuda.is_available():
    device = torch.device("cuda")
    print(f"# available GPUs : {torch.cuda.device_count()}")
    print(f"GPU name : {torch.cuda.get_device_name()}")
  else:
    device = torch.device("cpu")
  print(device)
  return device


  #- CustomDataset
class CustomDataset():
  """
  - input_data: list of string
  - target_data: list of int
  """

  def __init__(self, input_data:list, target_data:list) -> None:
    self.X = input_data
    self.Y = target_data

  def __len__(self):
      return len(self.Y)

  def __getitem__(self, index):
    x = str(self.X[index])
    y = self.Y[index]

    return x, y


#- custom_collate_fn()
def custom_collate_fn(batch):
  from transformers import BertTokenizer, BertModel
  tokenizer_bert = BertTokenizer.from_pretrained("klue/bert-base")
    
  input_list, target_list = [], []

  for data, label in batch:
    input_list.append(data)
    target_list.append(label)
    tensorized_input = tokenizer_bert(input_list,
                                      return_tensors='pt',
                                      padding='longest'
                                      )
    tensorized_label = torch.tensor(target_list)

    return tensorized_input, tensorized_label


#- CustomClassifier
import torch.nn as nn
import torch.nn.functional as F
from torch.optim import AdamW
from torch.nn import CrossEntropyLoss
from transformers import BertTokenizer, BertModel

class CustomClassifier(nn.Module):

  def __init__(self, hidden_size: int, n_label: int):
    super(CustomClassifier, self).__init__()

    self.bert = BertModel.from_pretrained("klue/bert-base")

    dropout_rate = 0.1
    linear_layer_hidden_size = 32

    self.classifier = nn.Sequential(
        nn.Linear(hidden_size, linear_layer_hidden_size),
        nn.ReLU(),
        nn.Dropout(dropout_rate),
        nn.Linear(linear_layer_hidden_size, n_label)
       ) 
    
  # torch.nn에서 제공되는 Sequential, Linear, ReLU, Dropout 함수 활용


  def forward(self, input_ids=None, attention_mask=None, token_type_ids=None):

    outputs = self.bert(
        input_ids,
        attention_mask=attention_mask,
        token_type_ids=token_type_ids,
        )

  # BERT 모델의 마지막 레이어의 첫번재 토큰을 인덱싱
    cls_token_last_hidden_states = outputs['pooler_output'] # 마지막 layer의 첫 번째 토큰
                                                          # ("[CLS]") 벡터를 가져오기, shape = (1, hidden_size)
    logits = self.classifier(cls_token_last_hidden_states)

    return logits