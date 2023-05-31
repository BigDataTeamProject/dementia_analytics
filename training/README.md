# 학습시킨 모델
## Oversampling 등 데이터 전처리 전
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

## Oversampling 등 데이터 전처리 후
LightGBM_with_DataPreprocessing.ipynb 파일을 확인해 보면 데이터 전처리 과정이 자세하게 나와있다.
1. accuracy가 낮게 나오고, test data에서 오히려 accuracy가 높게 나오는 경향이 있는 것이 이상해서 test 데이터의 분포와 test data로 prediction한 결과의 분포를 확인해 보니, 데이터가 균일하지 않아 모델이 모든 데이터에 대해 하나의 라벨로만 분류하는 모습을 확인할 수 있었다.
2. 따라서 Train-Test 데이터셋을 합쳐 전체 데이터셋의 분포를 확인해보았다. 전체 데이터에서도 데이터 불균형이 있는 것을 확인하여 sklearn의 MinMaxScaler를 사용해 train 데이터에 맞춰진 scaler를 만들고 이에 전체 원천 데이터를 scaling하였다.
3. 그리고 SMOTE를 사용하여 oversampling을 하였다.
4. 그 다음으로 train_test_split을 사용할 때 stratify를 사용하여 라벨 별로 균등하게 데이터를 분리하였다.
5. 이와 같이 전처리가 완료된 데이터를 사용하여 LightGBM으로 train과 test를 해본 결과 accuracy가 많이 개선되었다.

* Scaling + Train-Test를 각 라벨 별로 균등하게 분배 -> LightGBM 사용
  + train accuracy : 0.93
  + test accuracy  : 0.83
* Scaling + Oversampling + 라벨 별로 균등하게 분배 -> LightGBM 사용
  + train accuracy : 0.95
  + test accuracy  : 0.91
