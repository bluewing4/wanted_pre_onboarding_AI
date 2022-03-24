# 3일차 p****aper 정리****

# **Attention Is All You Need**
본파일 : https://second-chanter-c94.notion.site/3-paper-63b6afe6c52b4efca9218d7f09ce5c5c
- **Abstract**
    1. 다른모델의 문제점
        
        이전의 모델은 인코더와 디코더를 포함한 복잡한 구조를 가진다.
        
    2. 모델 목표
        
        Non-recurrent sequence to sequence encoder-decoder model을 만드는 것이 목표
        
        recurrence and convolutions으로 분배하는 새롭고 단순한 network architecture.
        
- **Background**
    1. 이전 모델의 가장 큰 문제점인 먼 위치 사이의 의존성이 학습을 더 어렵게 만든다
    2. 하지만 이번 과정에서 sequence-aligned RNNs or convolution은 사용하지 않고 input과 
    output의 계산을 위한 self-attention to compute representations의 모델을 만든다.
- **Model Architecture**
    
    ![사진출처 : Attention Is All You Need paper](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0a8c357c-5208-4b00-a26a-93f67e9ff449/Untitled.png)
    
    사진출처 : Attention Is All You Need paper
    
    1. Encoder
    6개의 stack으로 구성되어있고 하나의 layer는 Self-Attention Layer와 Position-Wise Fully Connected Feed Forward Neural Network로 이루어지고 2개의 Sub-layer가 존재한다.
        - Self-Attention
            
            ![****Self-Attention 구조****](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9983776c-4861-41ed-97a9-8233d887e164/Untitled.png)
            
            ****Self-Attention 구조****
            
            ![사진 출처 : [https://wdprogrammer.tistory.com/72](https://wdprogrammer.tistory.com/72)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d5ff6fdd-218d-4661-9a6b-8997aff4bb14/Untitled.png)
            
            사진 출처 : [https://wdprogrammer.tistory.com/72](https://wdprogrammer.tistory.com/72)
            
        - Scaled Dot-Product Attention
            
            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/efa09e0f-2797-4cf6-b663-2146dcf94472/Untitled.png)
            
        
        해당 논문에서는 Scaled Dot-Product Attention 이라고 한다.
        
        input은 dimension dk, and values of dimension dv로 구성
        
        모든 query와 key에 대한 dot-product를 계산하고 각각 √dk로 나눈다.
        
        이 과정이 dot-product를 하고  √dk로 scaling하므로 Scaled Dot-Product Attention이된다.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/24afeaad-e4f3-4e46-98b4-1e29a7aa509a/Untitled.png)
        
        - Multi-Head Attention
        
        self-attention layer를 다중으로 구현한 Multi-head attention을 제시했다. multi-head attention은 self-attn 보다 두 가지 측면에서 더 좋은 성능을 보여준다.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/abd857ea-0a54-4b03-9773-4536770749f2/Untitled.png)
        
        - Positional Encoding
        
        transformer가 만들고 싶은 모델은 sequence to sequence지만, 위치 정보를 포함하고 있어야 한다. 따라서 positional encoding 기법으로 각 단어의 상대적인 위치 정보를 포함시켰다.
        
        n은 sequence length, d는 representation dimension, k는 kernelsize of convolutions, 
        
        r은 size of the neighborhood in restricted self-attention
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/165a74d8-37ac-439e-9b8d-13655622dbad/Untitled.png)
        
        positional encoding은 encoder 과 decoder stacks의 동일한 차원의 dmodel을 가지므로 두 가지를 합산할 수 있다.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bea0044e-cad7-456b-84fa-c83317ec4af4/Untitled.png)
        
    2. Decoder
        
        인코더의 가장 상단에 있는 출력은 key와 value 벡터로 바뀐다. 이 key, value 벡터가 decoder의 각 encoder-decoder attention layer에 사용된다.
        
        time-step에서는 decoder의 직전 output을 input으로 다시 Decoder stacks를 거쳐 Linear+Softmax를 한 뒤, 다시 output과정을 거쳐친다.
        
        ![자료 및 내용 출처 : [https://omicro03.medium.com/attention-is-all-you-need-transformer-paper-정리-83066192d9ab](https://omicro03.medium.com/attention-is-all-you-need-transformer-paper-%EC%A0%95%EB%A6%AC-83066192d9ab)](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/20092e8a-89f9-4e33-aa7e-572fd8600016/Untitled.png)
        
        자료 및 내용 출처 : [https://omicro03.medium.com/attention-is-all-you-need-transformer-paper-정리-83066192d9ab](https://omicro03.medium.com/attention-is-all-you-need-transformer-paper-%EC%A0%95%EB%A6%AC-83066192d9ab)
        
    
- ****Conclusion****
    1. transformer는 recurrence를 이용하지 않고도 빠르고 정확하게 sequential data를 처리할 수 있는 model로 제시되었다.
    2. 여러가지 기법이 사용됐지만, 가장 핵심적인 것은 encoder와 decoder에서 attention을 통해 query와 가장 밀접한 연관성을 가지는 value를 강조할 수 있고 병렬화가 가능해진 것이다.
