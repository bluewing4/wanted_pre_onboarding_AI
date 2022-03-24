본파일 : https://second-chanter-c94.notion.site/3-NLG-7905961939344a2aa4e8028816231d20
### 1. Paperswithcode에서 NLG extractive summarization task에 대해서 본인 블로그에 정리해보세요. 아래 3가지 항목에 대해서 정리하세요. (각 항목 고려 사항 참고)

> 🔗Paperswithcode([https://paperswithcode.com/area/natural-language-processing](https://paperswithcode.com/area/natural-language-processing))
> 

### NLG 란?

> ****Natural Language Generation으로 컴퓨터가 Natural Language를 출력으로 생성하는 프로세스로 정의가 되며 Natural Language를 합리적인 방식으로 어떻게 생성할 지를 컴퓨터에게 가르치는 영역****
> 

자연어 생성은 구조화 된 데이터를 텍스트로 만들어 내는 과정

NLP(자연어 처리) = NLU(자연어 이해) + NLG(자연어 생성)

![출처: [https://www.kakaobrain.com/blog/118](https://www.kakaobrain.com/blog/118)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/81d809d9-d2b0-4c43-b8e5-a047b6737f7e/Untitled.jpeg)

출처: [https://www.kakaobrain.com/blog/118](https://www.kakaobrain.com/blog/118)

NLG의 활용 예시(Sub-tasks of NLG)

- Machine Translation
- Summarization
- Dialogue : task-oriented system, open-domain system(social dialogue)
- Creative writing : storytelling, poetry-generation
- Freeform Question Answering
- Image captioning

---

 1) **Extractive Summarization**

**- 문제 정의**

- 주어진 문서에서 문서의 요약을 가장 잘 나타내는 단어 또는 문장의 하위 집합

**- 데이터 소개(대표적인 데이터 1개)**

****CNN/Daily Mail****

- 데이터 CNN/Daily Mail은 각 웹사이트의 뉴스기사 생성되었고 
286,817개의 training set , 13,368개의 validation set 및 11,487개의 test set으로 구성되었으며  training set는 평균 29.74개의 문장에 766개의 단어를 가지고 있으며 요약은 53개의 단어와 3.72개의 문장으로 구성됩니다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/254c243b-ad9e-411d-a276-d19f69dadef6/Untitled.png)

**- 평가지표**

**ROUGE**

**ROUGE(Recall-Oriented Understudy for Gisting Evaluation)**란 text summarization, machine translation과 같은 generation task를 평가하기 위해 사용되는 대표적인 Metric

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/91dac035-a717-4773-afaa-b1bb2b25711c/Untitled.png)

- **ROUGE-N** :  unigram, bigram, trigram 등 문장 간 **중복되는 n-gram** 을 비교하는 지표
- ex) ROUGE-1 : unigram
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/21fc749d-f1e1-427a-b630-b0f2f7c00316/Untitled.png)
    
- ex)ROUGE-2 : bigram
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3e417e11-9f9f-4991-9bf2-5fafec37ee9f/Untitled.png)
    
- **ROUGE-L : Longest Common Subs equence로 가장 긴 Sequence의 recall을 구함(Sequence는 이어지지 않아도 됨)**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6ab54af0-c571-4ff2-a0cd-753edd1a0573/Untitled.png)
    
- **ROUGE-L의** 장점은 **ROUGE-2**와 같이 단어들의 **연속적 매칭**을 요구하지 않고, 어떻게든 **문자열** 내에서 발생하는 매칭을 측정하기 때문에 보다 유연한 성능 비교가 가능

                                                                                      출처 : [https://supkoon.tistory.com/26](https://supkoon.tistory.com/26)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f461336e-4d64-410d-81ac-356e7fd4eff1/Untitled.jpeg)

 **- SOTA(State-of-the art) 모델 소개(대표적인 모델 최소 2개 이상) 및 
   논문의 요약에서 주요 키워드**

---

- ****Neural Extractive Text Summarization with Syntactic Compression****
- ****Extractive Summarization as Text Matching****

# 1st Model

- [Lessons on Parameter Sharing across Layers in Transformers](https://paperswithcode.com/paper/lessons-on-parameter-sharing-across-layers-in)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ed48bbd-4f25-4ec1-8b4e-5e5c5330a26e/Untitled.png)

- 논문 요약

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1723414e-960a-4976-b63b-3c08b703c182/Untitled.png)

- summarization의 최근 접근방식은 selection-based extraction or generation-based abstraction의 두가지
- single-document summarization based on joint extraction and syntactic compression 제안
- 기성의 압축 모듈보다 성능이 뛰어나고 generally remains grammatical을 유지
- 주요 키워드
    - joint extraction and syntactic compression
    - generally remains grammatical을 유지

# 2nd Model

- ****[Extractive Summarization as Text Matching](https://paperswithcode.com/paper/extractive-summarization-as-text-matching)****

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d716c01-2b14-4fe8-80cb-b1caec573184/Untitled.png)

- 논문 요약

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ae1244f5-e612-4e94-a13f-fbd70fd8df0a/Untitled.png)

- 개별적으로 문장을 추출하고 문장 간의 관계를 모델링 하는 대신 추출요약작업을 의미적텍스트매칭(semantic text matching)으로 변경
- 단순한 형태의 매칭 모델로 프레임워크를 인스턴스화 하더라도 좋은 성능을 보여줌
- 주요 키워드
    - semantic text matching
