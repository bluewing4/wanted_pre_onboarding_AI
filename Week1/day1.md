### 1. 본인이 본 강의를 수강하는 목적에 대해서 자유롭게 적어보세요.

AI 및 DATA 분야에서 좀 더 세밀한 과정을 통하여 기술적인 경험을 통하여 한단계 발전할 수있도록 노력하겠습니다.

### 2. Paperswithcode에서 NLP sub task 중에 2개를 선택하여 본인 블로그에 정리해보세요. task 별로 아래 3가지 항목에 대해서 정리하세요. (각 항목 고려 사항 참고)

> 🔗Paperswithcode([https://paperswithcode.com/area/natural-language-processing](https://paperswithcode.com/area/natural-language-processing))
> 

### NLP 란?

> **Natural Language Processing(자연어처리)으로 텍스트에서 의미있는 정보를 분석, 추출하고 이해하는 일련의 기술집합**
> 

![출처: [https://www.kakaobrain.com/blog/118](https://www.kakaobrain.com/blog/118)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1415fcf9-25d0-4ce3-b27f-c8944d2dfddb/Untitled.jpeg)

출처: [https://www.kakaobrain.com/blog/118](https://www.kakaobrain.com/blog/118)

NLP 의 활용 예시(Sub-tasks of NLP)

- 텍스트 요약 (ex: Summly)
- 자동 질의응답 시스템 (ex: Wolfram Alpha)
- 대화 시스템 (ex: Apple Siri)
- 기계 번역 (ex: Google Translate)

 1) ****Document Summarization****

**- 문제 정의**

- 문서의 중요한 내용을 유지하면서 문서를 짧은 형식으로 보여주는 작업
- extractive approaches(추출식 접근) 와 abstractive approaches(추상적 접근)이 있고 추출식 접근은 원본의 일부를 추출하여 요약하는 반면 추상적 접근은 원본에 없는 새로운 단어나 구를 생성할 수 있도록 되어있습니다.

**- 데이터 소개(대표적인 데이터 1개)**

- 데이터 CNN/Daily Mail은 각 웹사이트의 뉴스기사 생성되었고 
286,817개의 training set , 13,368개의 validation set 및 11,487개의 test set으로 구성되었으며  training set는 평균 29.74개의 문장에 766개의 단어를 가지고 있으며 요약은 53개의 단어와 3.72개의 문장으로 구성됩니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/254c243b-ad9e-411d-a276-d19f69dadef6/Untitled.png)

 **- SOTA(State-of-the art) 모델 소개(대표적인 모델 1개)**

- [All NLP Tasks Are Generation Tasks: A General Pretraining Framework](https://paperswithcode.com/paper/all-nlp-tasks-are-generation-tasks-a-general)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bac8c67b-5707-4009-bfa9-b52c4f68d7fc/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/68b7f557-5cde-4e41-b702-dfab571cb4a7/Untitled.png)

- GLM-XXLarge모델로 논문의 내용으로 GLM은 동일한 양의 pre-training data로 SuperGLUE natural language understanding benchmark에서 BERT를 훨씬 능가한다고 나와있습니다.
- 주요 키워드는 pretraining framework GLM (General Language Model), ERT-like models on classification due to improved pretrain-finetune, same amount of pre-training data

 **2) Text Classification**

**- 문제 정의**

- 문장이나 문서를 적절한 범주로 지정하는 작업
- 범주는 선택한 데이터 세트에 따라 다르며 주제 범위가 다양할 수 있습니다.

**- 데이터 소개(대표적인 데이터 1개)**

- AG News(AG의 News Corpus)는 4가지의 가장 큰 클래스(“World”, “Sports”, “Business”, “Sci/Tech”)로 구성되어있고 각 클래스당 30,000개의 training set 및 1,900개의 test set입니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/beb546c5-9d0f-44fb-996b-03d83e43922e/Untitled.jpeg)

 **- SOTA(State-of-the art) 모델 소개(대표적인 모델 1개)**

- ****[XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://paperswithcode.com/paper/xlnet-generalized-autoregressive-pretraining)****
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1d869585-6aa8-4274-b72c-1f3313ab5764/Untitled.png)
    
- 
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/53d7e8d6-400b-45e6-8479-176bc3e778d9/Untitled.png)
    
- **XLNet**모델로 autoregressive pretraining 방법으로 구현되었으며 이는 BERT의 한계를 극복하고 질문 답변, 자연어 추론, 감정 분석 및 문서 순위를 포함하여 종종 큰 차이로 20가지 작업에서 보다 뛰어난 결과를 보였습니다.
- 주요 키워드는 autoregressive pretraining, XLNet outperforms BERT on 20 tasks, natural language inference, sentiment analysis, and document ranking
