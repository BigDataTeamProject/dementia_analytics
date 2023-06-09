# 치매 고위험군 웨어러블 데이터셋을 활용한 분석 및 시각화

- ### 치매 예측 모델
- ### 치매 관리 애플리케이션

---

## [0. 사용 데이터](./dementia_dataset/Demantia_DataSet.md)

### [치매 고위험군 웨어러블 라이프로그(AIHub)](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=226)

> 프로젝트에서 사용될 데이터셋 준비

---

## [1. 데이터 전처리](./data_processing/DataProcessing.md)

> 다양한 모델에 다양한 형태의 데이터 셋을 적용 시켜 정확도를 높이기 위해 기존의 데이터를 다양한 형태로 처리

#### dataset_01

- 원하는 데이터를 추출한 데이터 셋  
- EMAIL을 ID로 변환

#### dataset_02

- 원천 데이터와 라벨 데이터를 결합한 데이터 셋

#### dataset_03

- NaN 값을 같은 ID의 데이터의 평균 또는 같은 라벨링의 평균으로 채운 데이터

#### dataset_04

- NaN 값을 같은 ID의 데이터의 평균 또는 같은 라벨링의 평균으로 채운 데이터의 평균 데이터


#### dataset_05

- NaN 값을 같은 ID의 (데이터의 평균 또는 같은 라벨링의 평균)으로 채운 데이터 셋의 트레이닝 데이터와 검증 데이터를 합친 데이터

#### dataset_06

- NaN 값을 같은 ID의 (데이터의 평균 또는 같은 라벨링의 평균)으로 채운 데이터 셋의 전체 데이터의 라벨링을 기준으로 한 평균 데이터

#### dataset_07

- dataset_05와 dataset_06의 데이터에서 애플 사용자 데이터와 대응 될 수 있는 데이터만 추출

#### dataset_08

- 최종적으로 사용 될 데이터셋
- NaN값을 해당 ID의 평균으로 채운 데이터 셋에서 사용 가능한 데이터를 추출한 데이터셋과 해당 데이터셋의 라벨을 기준으로 한 평균 데이터

---

## [2. 데이터 시각화](./Visualization/README.md)

- 중요도 확인 후 feature들과 치매 정도의 상관관계 분석하기 위한 시각화


---

## [3. 모델 학습](./training/README.md)

> 프로젝트에서 사용할 모델 준비

### training/before_oversampling/
  - 다양한 모델들로 학습을 진행시켜본 코드 및 결과
  - 앙상블 학습 모델들의 성능이 뛰어난 편임을 확인하였다
### training/ 
- 아이폰 사용자가 얻을 수 있는 feature로만 학습 
  +  (그 중 feature importance가 떨어져서 제외시켜야 성능이 더 높게 나오는 feature는 제외)
- 가장 적절한 전처리 방법과 모델을 선택

#### 전처리 방법 결정 (LightGBM으로 각각 방법에 대한 validation data의 성능 지표 비교)
1. Min Max Scaler 적용해 결과 확인
2. Min Max Scaler 적용 후 SMOTE를 사용해 클래스 불균형 문제 개선
3. Min Max Scaler 적용 후 클래스 가중치를 사용해 클래스 불균형 문제 개선

=> 우리가 만드는 서비스는 치매 환자와 비슷한 수치를 가지는 사용자들에게 경고를 주는 서비스이기 때문에 Recall 을 중요시해 2번 방법 채택

#### 모델 비교 
- SMOTE를 사용해 오버샘플링된 데이터가 validation 이나 test data로 새지 않도록 해야 하기 때문에, before_oversampling 에서 좋은 성능을 보였던 앙상블 기법 중 validation set을 직접 지정할 수 있는 모델을 찾아 사용해 보고 비교
 
1. LightGBM
2. XGBoost

=> LightGBM 채택

---

## [4. 서버](https://github.com/BigDataTeamProject/dementia_analytics-server/blob/main/README.md)

> 요청에 따라 예측값과 평균값을 앱에 제공

  ### 예측값
    - 앱에서 사용자 데이터 입력 후 서버에 전송
    - 학습 모델을 이용하여 치매 유사도 예측
    - 예측값 다시 앱으로 반환
  
  ### 평균값
    - 치매,경증환자들의 평균치를 앱에서 요청에 따라 제공
    
  평균값은 get 방식을 사용했고, 사용자 데이터는 Post방식을 사용해서 요청을 받았다.

---

## [5. 치매 분석 애플리케이션](https://github.com/BigDataTeamProject/dementia_analytics-iOS/blob/main/README.md)

> 사용자의 생활 데이터를 전달하여 치매 고위험군 웨어러블 데이터셋을 활용한 모델로부터 치매 환자와의 유사도를 분석하는 애플리케이션

### 구성

| 홈                                          | 차트                                          | 설정                                             |
|--------------------------------------------|---------------------------------------------|------------------------------------------------|
| <img src="./images/Home.png" width=360/> | <img src="./images/Chart.png" width=360/> | <img src="./images/Settings.png" width=360/> |

### 사용자 건강 데이터 요청

| 아이폰의 건강 데이터 접근                               | 
|----------------------------------------------|
| <img src="./images/health.png" width=360/> |

### 사용자 건강 데이터 관리

| 건강 데이터 확인 및 관리                                   | 애플리케이션 내 데이터 확인 및 관리                              | 애플리케이션 내 데이터 추가                                   |
|--------------------------------------------------|---------------------------------------------------|---------------------------------------------------|
| <img src="./images/healthData.png" width=360 /> | <img src="./images/managedData.png" width=360/> | <img src="./images/managedData.png" width=360/> |


### 분석 및 시각화
| 사용자 데이터 분석 (정상인)                         | 사용자 데이터 분석 (치매 환자)                        | 차트                                              |
|------------------------------------------|-------------------------------------------|-------------------------------------------------|
| <img src="./images/cn.png" width=360/> | <img src="./images/dem.png" width=360/> | <img src="./images/stepChart.png" width=360/> |


### 설정
| 사용자 정보 표시                                      | 사용자 정보 설정                                     |
|------------------------------------------------|-----------------------------------------------|
| <img src="./images/Settings.png" width=360/> | <img src="./images/addUser.png" width=360/> |

### 프로필 및 권한 예외 처리

| 프로필 정보 업데이트 요청                                            | 권한 요청                                            |
|-----------------------------------------------------------|--------------------------------------------------|
| <img src="./images/needToUpdateProfile.png" width=360/> | <img src="./images/needToAuth.png" width=360/> |

