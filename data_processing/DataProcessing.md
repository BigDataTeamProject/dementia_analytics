## Data Processing

---

### dataset_01

### 원하는 데이터를 추출한 데이터 셋  
#### + EMAIL을 ID로 변환

**추출된 데이터**  
공통 데이터  
'EMAIL',
'date'
'activity_day_start',

활동 데이터  
'activity_cal_total',
'activity_daily_movement',
'activity_inactivity_alerts',
'activity_rest',
'activity_score_meet_daily_targets',
'activity_score_stay_active',
'activity_steps'

수면 데이터  
'sleep_bedtime_start',
'sleep_deep',
'sleep_duration',
'sleep_efficiency',
'sleep_hr_average',
'sleep_hr_lowest',
'sleep_onset_latency',
'sleep_rem'

**Training**

| 타입         | 파일                                                                                                   | 설명                                       |
|------------|------------------------------------------------------------------------------------------------------|------------------------------------------|
| label      | [train_dataset_label](./dataset_01/training/label/train_dataset_label.csv)                           | 트레이닝 데이터셋 라벨링 데이터                        |
|            | [train_label_activity](./dataset_01/training/label/train_label_activity.csv)                         | 활동 라벨링 데이터                               |
|            | [train_label_sleep](./dataset_01/training/train_label_sleep.csv)                                     | 수면 라벨링 데이터                               |
| source     | [train_activity](./dataset_01/training/source/train_activity.csv)                                    | 활동 원천 데이터 (데이터 추출)                       |
|            | [train_sleep](./dataset_01/training/source/train_sleep.csv)                                          | 수면 원천 데이터 (데이터 추출)                       |
|            | [train_dataset](./dataset_01/training/source/train_dataset.csv)                                      | 활동, 수면 원천 데이터 (데이터 추출)                   |
|            | [train_dataset_fill_mean](./dataset_01/training/source/train_dataset_fill_mean.csv)                  | 활동, 수면 원천 데이터 (데이터 추출, 평균 값)             |
|            | [train_dataset_remove_nan](./dataset_01/training/source/train_dataset_remove_nan.csv)                | 활동, 수면 원천 데이터 (데이터 추출, NaN 제거)           |
| with label | [train_dataset_with_label](./dataset_01/training/train_dataset_with_label.csv)                       | 활동, 수면 원천 데이터 (데이터 추출) + 라벨링 데이터         |
|            | [train_dataset_with_label_fill_mean](./dataset_01/training/train_dataset_with_label_fill_mean.csv)   | 활동, 수면 원천 데이터 (데이터 추출, 평균 값) + 라벨링 데이터   |
|            | [train_dataset_with_label_remove_nan](./dataset_01/training/train_dataset_with_label_remove_nan.csv) | 활동, 수면 원천 데이터 (데이터 추출, NaN 제거) + 라벨링 데이터 |

**Validation**

| 타입         | 파일                                                                                                 | 설명                                       |
|------------|----------------------------------------------------------------------------------------------------|------------------------------------------|
| label      | [val_dataset_label](./dataset_01/validation/label/val_dataset_label.csv)                           | 트레이닝 데이터셋 라벨링 데이터                        |
|            | [val_label_activity](./dataset_01/validation/label/val_label_activity.csv)                         | 활동 라벨링 데이터                               |
|            | [val_label_sleep](./dataset_01/validation/label/val_label_sleep.csv)                               | 수면 라벨링 데이터                               |
| source     | [val_activity](./dataset_01/validation/source/val_activity.csv)                                    | 활동 원천 데이터 (데이터 추출)                       |
|            | [val_sleep](./dataset_01/validation/source/val_sleep.csv)                                          | 수면 원천 데이터 (데이터 추출)                       |
|            | [val_dataset](./dataset_01/validation/source/val_dataset.csv)                                      | 활동, 수면 원천 데이터 (데이터 추출)                   |
|            | [val_dataset_fill_mean](./dataset_01/validation/source/val_dataset_fill_mean.csv)                  | 활동, 수면 원천 데이터 (데이터 추출, 평균 값)             |
|            | [val_dataset_remove_nan](./dataset_01/validation/source/val_dataset_remove_nan.csv)                | 활동, 수면 원천 데이터 (데이터 추출, NaN 제거)           |
| with label | [val_dataset_with_label](./dataset_01/validation/val_dataset_with_label.csv)                       | 활동, 수면 원천 데이터 (데이터 추출) + 라벨링 데이터         |
|            | [val_dataset_with_label_fill_mean](./dataset_01/validation/val_dataset_with_label_fill_mean.csv)   | 활동, 수면 원천 데이터 (데이터 추출, 평균 값) + 라벨링 데이터   |
|            | [val_dataset_with_label_remove_nan](./dataset_01/validation/val_dataset_with_label_remove_nan.csv) | 활동, 수면 원천 데이터 (데이터 추출, NaN 제거) + 라벨링 데이터 |

---

### dataset_02

#### 원천 데이터와 라벨 데이터를 결합한 데이터 셋

**training**

| 타입         | 파일                                                                                                   | 설명                               |
|------------|------------------------------------------------------------------------------------------------------|----------------------------------|
| label      | [train_dataset_label](./dataset_02/training/label/train_dataset_label.csv)                           | 트레이닝 데이터셋 라벨링 데이터                |
|            | [train_label_activity](./dataset_02/training/label/train_label_activity.csv)                         | 활동 라벨링 데이터                       |
|            | [train_label_sleep](./dataset_02/training/label/train_label_sleep.csv)                               | 수면 라벨링 데이터                       |
| source     | [train_activity](./dataset_02/training/source/train_activity.csv)                                    | 활동 원천 데이터                        |
|            | [train_sleep](./dataset_02/training/source/train_sleep.csv)                                          | 수면 원천 데이터                        |
|            | [train_dataset](./dataset_02/training/source/train_dataset.csv)                                      | 활동, 수면 원천 데이터                    |
|            | [train_dataset_fill_mean](./dataset_02/training/source/train_dataset_fill_mean.csv)                  | 활동, 수면 원천 데이터 (평균 값)             |
|            | [train_dataset_remove_nan](./dataset_02/training/source/train_dataset_remove_nan.csv)                | 활동, 수면 원천 데이터 (NaN 제거)           |
| with label | [train_dataset_with_label](./dataset_02/training/train_dataset_with_label.csv)                       | 활동, 수면 원천 데이터  + 라벨링 데이터         |
|            | [train_dataset_with_label_fill_mean](./dataset_02/training/train_dataset_with_label_fill_mean.csv)   | 활동, 수면 원천 데이터 (평균 값) + 라벨링 데이터   |
|            | [train_dataset_with_label_remove_nan](./dataset_02/training/train_dataset_with_label_remove_nan.csv) | 활동, 수면 원천 데이터 (NaN 제거) + 라벨링 데이터 |

**validation**

| 타입         | 파일                                                                                                 | 설명                               |
|------------|----------------------------------------------------------------------------------------------------|----------------------------------|
| label      | [val_dataset_label](./dataset_02/validation/label/val_dataset_label.csv)                           | 트레이닝 데이터셋 라벨링 데이터                |
|            | [val_label_activity](./dataset_02/validation/label/val_label_activity.csv)                         | 활동 라벨링 데이터                       |
|            | [val_label_sleep](./dataset_02/validation/label/val_label_sleep.csv)                               | 수면 라벨링 데이터                       |
| source     | [val_activity](./dataset_02/validation/source/val_activity.csv)                                    | 활동 원천 데이터                        |
|            | [val_sleep](./dataset_02/validation/source/val_sleep.csv)                                          | 수면 원천 데이터                        |
|            | [val_dataset](./dataset_02/validation/source/val_dataset.csv)                                      | 활동, 수면 후 데이터                     |
|            | [val_dataset_fill_mean](./dataset_02/validation/source/val_dataset_fill_mean.csv)                  | 활동, 수면 원천 데이터 (평균 값)             |
|            | [val_dataset_remove_nan](./dataset_02/validation/source/val_dataset_remove_nan.csv)                | 활동, 수면 원천 데이터 (NaN 제거)           |
| with label | [val_dataset_with_label](./dataset_02/validation/)                                                 | 활동, 수면 원천 데이터  + 라벨링 데이터         |
|            | [val_dataset_with_label_fill_mean](./dataset_02/validation/val_dataset_with_label_fill_mean.csv)   | 활동, 수면 원천 데이터 (평균 값) + 라벨링 데이터   |
|            | [val_dataset_with_label_remove_nan](./dataset_02/validation/val_dataset_with_label_remove_nan.csv) | 활동, 수면 원천 데이터 (NaN 제거) + 라벨링 데이터 |

---

### dataset_03

#### NaN 값을 같은 ID의 데이터의 평균 또는 같은 라벨링의 평균으로 채운 데이터

**training**

| 타입 | 파일                                                                                                                 | 설명                                  |
|----|--------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| -  | [train_dataset_with_label_fill_user_mean](./dataset_03/training/train_dataset_with_label_fill_user_mean.csv)       | 활동, 수면 훈련 데이터(같은 ID값의 평균) + 라벨링 데이터 |
| -  | [train_dataset_with_label_fill_DIAG_NM_mean](./dataset_03/training/train_dataset_with_label_fill_DIAG_NM_mean.csv) | 활동, 수면 훈련 데이터(같은 라벨링의 평균) + 라벨링 데이터 |

**validation**

| 타입 | 파일                                                                                                               | 설명                                  |
|----|------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| -  | [val_dataset_with_label_fill_user_mean](./dataset_03/validation/val_dataset_with_label_fill_user_mean.csv)       | 활동, 수면 검증 데이터(같은 ID값의 평균) + 라벨링 데이터 |
| -  | [val_dataset_with_label_fill_DIAG_NM_mean](./dataset_03/validation/val_dataset_with_label_fill_DIAG_NM_mean.csv) | 활동, 수면 검증 데이터(같은 라벨링의 평균) + 라벨링 데이터 |

---

### dataset_04

#### NaN 값을 같은 ID의 데이터의 평균 또는 같은 라벨링의 평균으로 채운 데이터의 평균

**training**

| 타입 | 파일                                                                                                                   | 설명                                       |
|----|----------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| -  | [train_dataset_with_label_find_mean](./dataset_04/training/train_dataset_with_label_find_mean.csv)                   | 활동, 수면 훈련 데이터의 평균 (NaN값을 해당 ID의 평균으로 채움) |
| -  | [train_dataset_with_label_find_mean_with_nan](./dataset_04/training/train_dataset_with_label_find_mean_with_nan.csv) | 활동, 수면 훈련 데이터의 평균 (NaN값을 포함하지 않고 평균을 구함) |

**validation**

| 타입 | 파일                                                                                                                 | 설명                                               |
|----|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| -  | [val_dataset_with_label_find_mean](./dataset_04/validation/val_dataset_with_label_find_mean.cav)                   | 활동, 수면 검증 데이터의 평균 (평균 NaN값을 해당 ID의 평균으로 채움)      |
| -  | [val_dataset_with_label_find_mean_with_nan](./dataset_04/validation/val_dataset_with_label_find_mean_with_nan.csv) | 활동, 수면 검증 데이터의 평균 (데이터의 평균 NaN값을 포함하지 않고 평균을 구함) |

### dataset_05

#### NaN 값을 같은 ID의 데이터의 평균 또는 같은 라벨링의 평균으로 채운 데이터 셋의
#### 트레이닝 데이터와 검증 데이터를 합친 데이터

**dataset**

| 타입 | 파일                                                                                            | 설명                                    |
|----|-----------------------------------------------------------------------------------------------|---------------------------------------|
| -  | [dataset_with_label_fill_user_mean](./dataset_05/dataset_with_label_fill_user_mean.csv)       | 전체 데이터 (평균 NaN값을 해당 ID의 평균으로 채움)      |
| -  | [dataset_with_label_fill_DIAG_NM_mean](./dataset_05/dataset_with_label_fill_DIAG_NM_mean.csv) | 전체 데이터 (데이터의 평균 NaN값을 포함하지 않고 평균을 구함) |
| -  | [dataset_with_label_remove_nan](./dataset_05/dataset_with_label_remove_nan.csv)               | 전체 데이터 (NaN이 있는 데이터를 삭제한 데이터셋을 이ㅊㄴㅍ)  |


### dataset_06

#### NaN 값을 같은 ID의 (데이터의 평균 또는 같은 라벨링의 평균)으로 채운 데이터 셋의
#### 전체 데이터의 라벨링 기준 평균