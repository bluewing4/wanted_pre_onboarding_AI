import random
import torch
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sentence_transformers.readers import InputExample
from sklearn.metrics.pairwise import paired_cosine_distances

# seed
config = {"seed":42}

np.random.seed(config['seed'])
random.seed(config['seed'])
torch.manual_seed(config['seed'])
torch.cuda.manual_seed_all(config['seed'])


# make input : predict + reference 
def rdass_pred_ref(ref_pred):
    samples = []
    for i, j in zip(ref_pred['predict'], ref_pred['reference']):
        samples.append([i,j])

    # sbert 모델에 들어가는 InputExample형식으로 변환
    pred_refer = []
    for sample in samples:
        input = InputExample(
            texts=sample
            )
        pred_refer.append(input)

    return pred_refer

# make input : predict + content
def rdass_pred_cont(ref_pred):
    samples = []
    for i, j in zip(ref_pred['predict'], ref_pred['content']):
        samples.append([i,j])

    # sbert 모델에 들어가는 InputExample형식으로 교체
    pred_cont = []
    for sample in samples:
        input = InputExample(
            texts=sample
            )
        pred_cont.append(input)

    return pred_cont


def make_embedding(SBERT, ref_pred, mode):
    assert mode in ['predict', 'reference', 'content']

    if mode == 'predict':
        embedding = SBERT.encode(ref_pred['predict'], batch_size=64,  convert_to_numpy=True)
    elif mode == 'reference':
        embedding = SBERT.encode(ref_pred['reference'], batch_size=64,  convert_to_numpy=True)
    else:
        embedding = SBERT.encode(ref_pred['content'], batch_size=64,  convert_to_numpy=True)
    
    return embedding


def cosine_similarity(embedding_pred, embedding_refer=None, embedding_cont=None):
    if embedding_refer is not None:
        cosine_sim = 1 - paired_cosine_distances(embedding_pred, embedding_refer)
    elif embedding_cont is not None:
        cosine_sim = 1 - paired_cosine_distances(embedding_pred, embedding_cont)
    else:
        raise KeyError("embedding_refer or embedding_cont is required")
    
    return cosine_sim


def metric(ref_pred, cosine_sim_pred_refer, cosine_sim_pred_cont):
    # 데이터프레임 열 추가
    ref_pred.loc[:, 'cosine_sim_pred_refer'] = cosine_sim_pred_refer
    ref_pred.loc[:, 'cosine_sim_pred_cont'] = cosine_sim_pred_cont

    ### RDASS 계산 ###
    # RDASS
    ref_pred['RDASS'] = (ref_pred['cosine_sim_pred_refer'] + ref_pred['cosine_sim_pred_refer'])/2
    
    # RDASS 평균
    avg_rdass = ref_pred['RDASS'].mean()
    
    return ref_pred, avg_rdass