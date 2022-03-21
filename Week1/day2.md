### 1. Paperswithcode에서 NLU sub task 중 하나를 선택하여 본인 블로그에 정리해보세요. 아래 3가지 항목에 대해서 정리하세요. (각 항목 고려 사항 참고)

> 🔗Paperswithcode([https://paperswithcode.com/task/natural-language-understanding](https://paperswithcode.com/task/natural-language-understanding))
> 

### NLU 란?

> ****Natural Language Understanding으로 텍스트 분류, 자연어 추론 및 이야기 이해와 같은 다양한 작업을 포함하는 자연어 처리의 중요한 분야****
> 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1124610c-cef6-47f4-9215-91e5a98aa3c0/Untitled.jpeg)

출처: [https://www.kakaobrain.com/blog/118](https://www.kakaobrain.com/blog/118)

NLU의 활용 예시(Sub-tasks of NLU)

- Simple profanity filters(비속어를 제거하는 필터 역할)
- Sentiment detection(감정분석)
- Topic classification(주제 분류)
- Entity detection(개체명 검출

---

 1) ****Sentiment Analysis****

**- 문제 정의**

- 감정분석은 주어진 텍스트의 극성을 분류하는 작업
- 예를 들어 텍스트 기반 트윗은 "긍정적", "부정적" 또는 "중립"으로 분류
- 텍스트와 함께 제공되는 레이블이 주어지면 모델이 올바른 감정을 예측하도록 훈련
- 머신 러닝 접근 방식, 어휘 기반 접근 방식, 심지어 하이브리드 방식으로 분류
- 감정 분석 연구의 일부 하위 범주에는 다중 모드 감정 분석, 측면 기반 감정 분석, 세분화된 의견 분석, 언어별 감정 분석이 포함
- 감성 분석 시스템을 평가하기 위해 SST, GLUE 및 IMDB 영화 리뷰와 같은 벤치마크 데이터 세트가 사용

**- 데이터 소개(대표적인 데이터 1개)**

- ****MRPC (Microsoft Research Paraphrase Corpus)****
- newswire articles에서 수집된 5201개의 문장이 의역인지 여부에 따라 human annotators에 의해 label이 구성
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e5b95b71-0e36-495d-a362-343c3684cbea/Untitled.jpeg)
    
- 4076개의 문장 중 2753개가 의역인 training set 으로구성
- 1725개의 문장 중 1147개가 의역인 test set 으로구성

 **- SOTA(State-of-the art) 모델 소개(대표적인 모델 최소 2개 이상) 및 
   논문의 요약에서 주요 키워드**

$$
Accuracy = {TN+TP \over TN+TP+FN+FP}

$$

True Positive(TP) : 실제 True인 정답이 True라고 예측(정답)
False Positive(FP) : 실제 False 인 정답이 True라고 예측(오답)
False Negative(FN) : 실제 True인 정답이 False 라고 예측(오답)
True Negative(TN) : 실제 False 인 정답이 False 라고 예측(정답)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3a432dee-d27c-4b03-866d-ad14284c74dd/Untitled.png)

---

# 1st Model

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7b795df1-a42b-4ad9-b1fa-0421457a2901/Untitled.png)

- ****[SMART: Robust and Efficient Fine-Tuning for Pre-trained Natural Language Models through Principled Regularized Optimization](https://paperswithcode.com/paper/smart-robust-and-efficient-fine-tuning-for)****
- Accuracy : 93.7%
- 논문 요약
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/49e4907f-2274-45c8-ae4d-d3cdf619c849/Untitled.png)
    
- 기존의 모델은 first pre-trained on a large text corpus에서 fine-tuned on downstream tasks 작업을 하게되면 종종 데이터의 과적합이 발생하거나 pre-trained된 모델에 대한 지식을 잊어버리는 경우가 발생하는것을 확인하였고 그를 방지하기 위한 new computational framework를 시행
- Bregman proximal point optimization은 trust-region methods이며 지식을 망각하는 것을 예방
- 주요 키워드
    - Smoothness-inducing regularization, which effectively manages the capacity of the model
    - Bregman proximal point optimization

# 2nd Model

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/36ca4aa0-a570-4e31-9cf1-cf732874afd1/Untitled.png)

- ****[Synthesizer: Rethinking Self-Attention in Transformer Models](https://paperswithcode.com/paper/synthesizer-rethinking-self-attention-in)****
- Accuracy : 91.2%
- 논문 요약
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8cddedaa-cb27-42cd-9161-4db81a3ab80e/Untitled.png)
    
- product-based self-attention mechanism이 Transformer 모델의 성능에 미치는 중요성과 기여도를 조사하였고 매우 경쟁력 있는 성능을 달성
- 주요 키워드
    - self-attention
    - Random Synthesizer
    - 60% faster
    - simple factorized Synthesizers
