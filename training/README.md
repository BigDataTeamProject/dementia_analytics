# 기본적인 전처리 방법
Classification의 경우, 라벨 인코더를 사용하여 `CN : 0, Dem : 1, MCI : 2` 로 바꾸어 사용하였다.
Regression의 경우, CN은 0, MCI는 0.5, Dem은 1 와 같이 치매율를 나타내어 사용하였다.    
<img width="326" alt="image" src="https://github.com/BigDataTeamProject/dementia_analytics/assets/90085690/3f6143a6-8333-4436-a06e-b3453633c13b">    

<img width="371" alt="image" src="https://github.com/BigDataTeamProject/dementia_analytics/assets/90085690/74b861a4-9408-4820-9b32-a56235505c2e">

# 학습시킨 모델
# Oversampling 등 데이터 전처리 전
* KNN (Classification)
  + train accuracy : 0.75
  + test accuracy  : 0.58
* Linear Regression (Regression)
  + test r2_score  : -0.1
* Naive Bayes (Classification)
  + train accuracy : 0.58
  + test accuracy  : 0.51
* RandomForest (Classification)
  + train accuracy : 0.65
  + test accuracy  : 0.72
* LightGBM (Classification)
  + train accuracy : 0.59
  + test accuracy  : 0.79

# 중간발표 이후 전처리 시도 + 사용 가능한 데이터만 사용

* LightGBM_with_DataPreprocessing.ipynb 에 자세한 코드와 실행 결과가 나타나 있다.
* 먼저 전체 데이터 중 test로 사용할 데이터를 분리하여 사용하지 않았다.
* 레이블 인코딩을 하고, train 데이터를 다시 train과 validation 데이터로 나누었다.
* validation 데이터는 여러 전처리 방법의 결과를 확인할 용도의 데이터이다.
* train 데이터를 다시 t, v 로 나누었는데, v는 LGBM.fit() 을 할 때 eval_set에 설정해 학습 중 validation data로 사용할 데이터이다.
* train_test_split()을 사용할 때 항상 라벨 별로 균등하게 나니도록 `stratify` flag를 사용하였다.

### 1. Min Max Scaler 적용
* sklearn의 MinMaxScaler를 사용해 t 데이터에 맞춰진 scaler를 만들고 이에 맞게 전체 원천 데이터를 scaling하였다.

### 2. SMOTE를 사용한 오버샘플링

`stratify` 를 사용해서 데이터가 균등하게 나뉘어졌음에도 t 데이터의 분포가 불균형했다. 이를 개선하기 위해 SMOTE를 적용해 보았다.

<img width="175" alt="image" src="https://github.com/BigDataTeamProject/dementia_analytics/assets/90085690/304aee55-68f2-4c00-b47a-3b276a7d2da5">

### 3. 클래스 가중치
오버샘플링 대신 데이터 개수가 적은 클래스에 더 높은 가중치를 주어 학습해보고자 하였다.     

### 각 시도에 대한 테스트 결과

|  | Scaling | Scaling + 오버샘플링 | Scaling +  클래스 가중치 설정 |
| --- | --- | --- | --- |
| accuracy | 0.7712561711464618 | 0.7652221612726275 | 0.5990126165660998 |
| precision | 0.8003337140776301 | 0.7395748360728578 | 0.19967087218869994 |
| recall | 0.705312722704027 | 0.7510934047165931 | 0.3333333333333333 |
| f1 score | 0.7414412837415935 | 0.7451593756932641 | 0.24974271012006863 |


MinMaxScaler만 사용한 경우와 SMOTE까지 적용한 경우 성능 차이가 크게 나지는 않지만, 우리가 만드는 서비스는 치매 환자와 비슷한 수치를 가지는 사용자들에게 경고를 주는 서비스이기 때문에 recall 점수가 가장 중요하기 때문에 SMOTE까지 사용하기로 결정하였다.

# 최종 모델 선정
: SMOTE를 사용해 오버샘플링된 데이터가 validation 혹은 test로 사용되지 않도록 하기 위해, 중간 발표 당시 성능이 좋았던 앙상블 모델 중에서 validation data를 직접 지정할 수 있는 모델을 찾아 validation 결과를 비교해 보았다.

|  | LightGBM | XGBoost |
| --- | --- | --- |
| accuracy | 0.7652221612726275 | 0.7185957213384531 |
| precision | 0.7395748360728578 | 0.676744492771816 |
| recall | 0.7510934047165931 | 0.7284604016488073 |
| f1 score | 0.7451593756932641 | 0.6988499773771236 |


-> 결과, LightGBM이 제일 좋게 나오는 것을 확인하였다.

* 이 LGBM을 최종 모델로 사용하기로 결정하고, pkl 형식으로 저장해 백엔드에서 사용할 수 있도록 하였다.
* 이 모델을 test  테스트해보는 코드는 load_and_predict_FinelModel.ipynb에 있다.
```
0 번째:
예측: [0]
실제: [0]

100 번째:
예측: [0]
실제: [2]

200 번째:
예측: [2]
실제: [2]

300 번째:
예측: [0]
실제: [0]

400 번째:
예측: [0]
실제: [0]

500 번째:
예측: [0]
실제: [0]

600 번째:
예측: [2]
실제: [2]

700 번째:
예측: [0]
실제: [0]

800 번째:
예측: [2]
실제: [2]

900 번째:
예측: [0]
실제: [0]

1000 번째:
예측: [0]
실제: [0]

1100 번째:
예측: [2]
실제: [0]

1200 번째:
예측: [0]
실제: [2]

1300 번째:
예측: [1]
실제: [1]

1400 번째:
예측: [0]
실제: [0]

1500 번째:
예측: [2]
실제: [2]

1600 번째:
예측: [2]
실제: [2]

1700 번째:
예측: [0]
실제: [0]

1800 번째:
예측: [0]
실제: [0]

1900 번째:
예측: [2]
실제: [2]

2000 번째:
예측: [2]
실제: [2]

2100 번째:
예측: [2]
실제: [0]

2200 번째:
예측: [0]
실제: [0]
```
```
Accuracy: 0.7726075504828798
Precision: 0.7308847434425226
Recall: 0.7808662772477639
F1 Score: 0.7526889999748554
```
<img width="367" alt="image" src="https://github.com/BigDataTeamProject/dementia_analytics/assets/90085690/67b75ecf-7f0c-4bb7-a489-ea7963d36163">

    
-> 정상과 경도인지장애를 혼동한 경우가 대부분임을 확인할 수 있었다.

# 참고한 자료:
[https://tensorflow.blog/파이썬-머신러닝/2-3-2-k-최근접-이웃/](https://tensorflow.blog/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D/2-3-2-k-%EC%B5%9C%EA%B7%BC%EC%A0%91-%EC%9D%B4%EC%9B%83/)

[https://zzinnam.tistory.com/entry/하이퍼파라미터-Serching-with-파이썬-GridSearchCV-함수](https://zzinnam.tistory.com/entry/%ED%95%98%EC%9D%B4%ED%8D%BC%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-Serching-with-%ED%8C%8C%EC%9D%B4%EC%8D%AC-GridSearchCV-%ED%95%A8%EC%88%98) 

[https://skillmemory.tistory.com/entry/머신러닝-분류-사이킷런을-활용한-나이브-베이즈-분류](https://skillmemory.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EB%B6%84%EB%A5%98-%EC%82%AC%EC%9D%B4%ED%82%B7%EB%9F%B0%EC%9D%84-%ED%99%9C%EC%9A%A9%ED%95%9C-%EB%82%98%EC%9D%B4%EB%B8%8C-%EB%B2%A0%EC%9D%B4%EC%A6%88-%EB%B6%84%EB%A5%98)

https://injo.tistory.com/30

[https://john-analyst.medium.com/smote로-데이터-불균형-해결하기-5ab674ef0b32](https://john-analyst.medium.com/smote%EB%A1%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%88%EA%B7%A0%ED%98%95-%ED%95%B4%EA%B2%B0%ED%95%98%EA%B8%B0-5ab674ef0b32)

[https://romg2.github.io/mlguide/03_머신러닝-완벽가이드-04.-분류-XGBoost/](https://romg2.github.io/mlguide/03_%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-%EC%99%84%EB%B2%BD%EA%B0%80%EC%9D%B4%EB%93%9C-04.-%EB%B6%84%EB%A5%98-XGBoost/)

https://m.blog.naver.com/wideeyed/221330321950
