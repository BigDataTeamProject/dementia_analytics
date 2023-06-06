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

# 데이터 불균형 문제 해결 시도 + 사용 가능한 데이터만 사용
### 1. train_test_split 시 label 별로 균등하게 분배되도록 시도
LightGBM_with_DataPreprocessing.ipynb 파일을 확인해 보면 데이터 전처리 과정이 자세하게 나와있다.
* 사용자로부터 얻을 수 없는 feature를 제거하고 모델 학습을 진행하였다.
* 기존의 방법에서 LightGBM의 accuracy가 낮게 나오고, test data에서 오히려 accuracy가 높게 나오는 경향이 있는 것이 이상해서 test 데이터의 분포와 test data로 prediction한 결과의 분포를 확인해 보니,      
  ![image](https://github.com/BigDataTeamProject/dementia_analytics/assets/90085690/61df643e-0385-4048-af26-786b0e1c67c7)     
  데이터가 균일하지 않아 모델이 모든 데이터에 대해 하나의 라벨로만 분류하는 모습을 확인할 수 있었다.
* 따라서 Train-Test 데이터셋을 합친 후 sklearn의 MinMaxScaler를 사용해 train 데이터에 맞춰진 scaler를 만들고 이에 전체 원천 데이터를 scaling하였다.
* 그리고 train_test_split 을 사용할 stratify를 사용하여 라벨 별로 균등하게 데이터를 분리하였다.
* 이와 같이 전처리가 완료된 데이터를 사용하여 LightGBM으로 train과 test를 해본 결과 accuracy가 많이 개선되었고, test prediction도 다양하게 나타났다.     
![image](https://github.com/BigDataTeamProject/dementia_analytics/assets/90085690/fe1793ce-699e-4a0f-8c8e-6d9c7e8aa89b)     

### 2. SMOTE를 사용한 오버샘플링
train과 test 데이터를 균등하게 분배한다고 해도, 전체 데이터셋에서도 데이터 불균형이 있기 때문에 오버샘플링을 train data에 적용해보았다.     
![image](https://github.com/BigDataTeamProject/dementia_analytics/assets/90085690/0a7f22e4-8b04-4650-8a47-6616b063851d)     
하지만 그 결과 성능이 더 좋아지지는 않았다.

### 3. 클래스 가중치
오버샘플링 대신 데이터 개수가 적은 클래스에 더 높은 가중치를 주어 학습해보고자 하였다.     
![image](https://github.com/BigDataTeamProject/dementia_analytics/assets/90085690/1a6c5a97-e6a9-4a15-9dd9-6fb526b76033)        
클래스 가중치가 데이터 개수에 반비례하도록  하여 적용하였지만 이 또한 성능을 더 높이지 못했다.

### 각 시도에 대한 테스트 결과

|  | Scaling  | Scaling + train test 균등 | Scaling + train test 균등 + 오버샘플링 | Scaling + train test 균등 + 클래스 가중치 설정 |
| --- | --- | --- | --- | --- |
| test prediction | 하나의 라벨로만 predict | 골고루 predict | 골고루 predict | 골고루 predict |
| accuracy | 0.7860560492139439 | 0.7866549604916594 | 0.7704126426690079 | 0.7673397717295873 |
| precision | 0.26201868307131465 | 0.8064685479616706 | 0.7282679357125437 | 0.7399033940895526 |
| recall | 0.3333333333333333 | 0.7340414455421468 | 0.7679857247318678 | 0.7820258345363534 |
| f1 score | 0.2934047710167113 | 0.7636371852563455 | 0.7460160196972794 | 0.7581407749395169 |

# 최종 모델 선정
: Scaling과 Train Test를 균등하게 나눈 후 LightGBM, XGBoost, RandomForest, NaiveBayes 등 시도 (Final_Data_Modeling.ipynb)

|  | LightGBM | XGBoost | RandomForest | KNN | Naive Bayes | Extra Trees Classifier |
| --- | --- | --- | --- | --- | --- | --- |
| accuracy | 0.7866549604916594 | 0.8129938542581212 | 0.7848990342405618 | 0.7822651448639157 | 0.5877963125548727 | 0.5992098331870062 |
| precision | 0.8064685479616706 | 0.8420549170968195 | 0.8315403139250638 | 0.7806524723411624 | 0.46481039050719025 | 0.1997366110623354 |
| recall | 0.7340414455421468 | 0.7504858831366544 | 0.7098051706747359 | 0.7314065146323211 | 0.44401108319761895 | 0.3333333333333333 |
| f1 score | 0.7636371852563455 | 0.7872799913951146 | 0.7546042797893552 | 0.7531385038945523 | 0.43385245538134615 | 0.24979412572056 |
     
-> 결과, XGBoost가 제일 좋게 나오는 것을 확인하였다.

# XGBoost 하이퍼파라미터 튜닝
위에서 성능이 가장 좋았던 XGBoost에 하이퍼파라미터 튜닝을 시도해 보았다. (Final_Data_Modeling.ipynb)
```
best f1_macro :  0.7852
best param :  {'colsample_bytree': 0.9, 'gamma': 0, 'learning_rate': 0.15, 'max_depth': 15, 'n_estimators': 500}
```
```
Accuracy: 0.8244073748902546
Precision: 0.8416233659789031
Recall: 0.7727108795832498
F1 Score: 0.8020239575298093
```

* 이 결과대로 튜닝된 XGBoost를 최종 모델로 사용하기로 결정하고, Final_Model.ipynb에서 이를 프로그래밍했다.
* 이 모델을 테스트해보는 코드는 load_and_predict_FinelModel.ipynb에도 있다.
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
예측: [0]
실제: [0]

1200 번째:
예측: [2]
실제: [2]

1300 번째:
예측: [1]
실제: [1]

1400 번째:
예측: [0]
실제: [0]

...
```

# 학습된 모델 저장 및 복원
* .pkl 로 모델과 scaler 저장
* .pkl 로 저장된 모델과 scaler 복원해 사용하는 코드는 load_and_predict_FinalModel.ipynb 에 있다.
