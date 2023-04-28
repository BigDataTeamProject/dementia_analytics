## Data Processing

---

### dataset_01

데이터 추출  
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

| 타입         | 파일                                      | 설명                                       |
|------------|-----------------------------------------|------------------------------------------|
| label      | [train_dataset_label]()                 | 트레이닝 데이터셋 라벨링 데이터                        |
|            | [train_label_activity]()                | 활동 라벨링 데이터                               |
|            | [train_label_sleep]()                   | 수면 라벨링 데이터                               |
| source     | [train_activity]()                      | 활동 원천 데이터 (데이터 추출)                       |
|            | [train_sleep]()                         | 수면 원천 데이터 (데이터 추출)                       |
|            | [train_dataset]()                       | 활동, 수면 원천 데이터 (데이터 추출)                   |
|            | [train_dataset_fill_mean]()             | 활동, 수면 원천 데이터 (데이터 추출, 평균 값)             |
|            | [train_dataset_remove_nan]()            | 활동, 수면 원천 데이터 (데이터 추출, NaN 제거)           |
| with label | [train_dataset_with_label]()            | 활동, 수면 원천 데이터 (데이터 추출) + 라벨링 데이터         |
|            | [train_dataset_with_label_fill_mean]()  | 활동, 수면 원천 데이터 (데이터 추출, 평균 값) + 라벨링 데이터   |
|            | [train_dataset_with_label_remove_nan]() | 활동, 수면 원천 데이터 (데이터 추출, NaN 제거) + 라벨링 데이터 |

**Validation**

| 타입         | 파일                                    | 설명                                       |
|------------|---------------------------------------|------------------------------------------|
| label      | [val_dataset_label]()                 | 트레이닝 데이터셋 라벨링 데이터                        |
|            | [val_label_activity]()                | 활동 라벨링 데이터                               |
|            | [val_label_sleep]()                   | 수면 라벨링 데이터                               |
| source     | [val_activity]()                      | 활동 원천 데이터 (데이터 추출)                       |
|            | [val_sleep]()                         | 수면 원천 데이터 (데이터 추출)                       |
|            | [val_dataset]()                       | 활동, 수면 원천 데이터 (데이터 추출)                   |
|            | [val_dataset_fill_mean]()             | 활동, 수면 원천 데이터 (데이터 추출, 평균 값)             |
|            | [val_dataset_remove_nan]()            | 활동, 수면 원천 데이터 (데이터 추출, NaN 제거)           |
| with label | [val_dataset_with_label]()            | 활동, 수면 원천 데이터 (데이터 추출) + 라벨링 데이터         |
|            | [val_dataset_with_label_fill_mean]()  | 활동, 수면 원천 데이터 (데이터 추출, 평균 값) + 라벨링 데이터   |
|            | [val_dataset_with_label_remove_nan]() | 활동, 수면 원천 데이터 (데이터 추출, NaN 제거) + 라벨링 데이터 |

---

### dataset_02

전체 데이터 결합

**training**

| 타입         | 파일                                      | 설명                               |
|------------|-----------------------------------------|----------------------------------|
| label      | [train_dataset_label]()                 | 트레이닝 데이터셋 라벨링 데이터                |
|            | [train_label_activity]()                | 활동 라벨링 데이터                       |
|            | [train_label_sleep]()                   | 수면 라벨링 데이터                       |
| source     | [train_activity]()                      | 활동 원천 데이터                        |
|            | [train_sleep]()                         | 수면 원천 데이터                        |
|            | [train_dataset]()                       | 활동, 수면 원천 데이터                    |
|            | [train_dataset_fill_mean]()             | 활동, 수면 원천 데이터 (평균 값)             |
|            | [train_dataset_remove_nan]()            | 활동, 수면 원천 데이터 (NaN 제거)           |
| with label | [train_dataset_with_label]()            | 활동, 수면 원천 데이터  + 라벨링 데이터         |
|            | [train_dataset_with_label_fill_mean]()  | 활동, 수면 원천 데이터 (평균 값) + 라벨링 데이터   |
|            | [train_dataset_with_label_remove_nan]() | 활동, 수면 원천 데이터 (NaN 제거) + 라벨링 데이터 |

**validation**

| 타입         | 파일                                    | 설명                               |
|------------|---------------------------------------|----------------------------------|
| label      | [val_dataset_label]()                 | 트레이닝 데이터셋 라벨링 데이터                |
|            | [val_label_activity]()                | 활동 라벨링 데이터                       |
|            | [val_label_sleep]()                   | 수면 라벨링 데이터                       |
| source     | [val_activity]()                      | 활동 원천 데이터                        |
|            | [val_sleep]()                         | 수면 원천 데이터                        |
|            | [val_dataset]()                       | 활동, 수면 원천 데이터                    |
|            | [val_dataset_fill_mean]()             | 활동, 수면 원천 데이터 (평균 값)             |
|            | [val_dataset_remove_nan]()            | 활동, 수면 원천 데이터 (NaN 제거)           |
| with label | [val_dataset_with_label]()            | 활동, 수면 원천 데이터  + 라벨링 데이터         |
|            | [val_dataset_with_label_fill_mean]()  | 활동, 수면 원천 데이터 (평균 값) + 라벨링 데이터   |
|            | [val_dataset_with_label_remove_nan]() | 활동, 수면 원천 데이터 (NaN 제거) + 라벨링 데이터 |

---

### dataset_03

**training**

| 타입 | 파일                                             | 설명                                  |
|----|------------------------------------------------|-------------------------------------|
| -  | [train_dataset_with_label_fill_user_mean]()    | 활동, 수면 원천 데이터(같은 ID값의 평균) + 라벨링 데이터 |
| -  | [train_dataset_with_label_fill_DIAG_NM_mean]() | 활동, 수면 원천 데이터(같은 라벨링의 평균) + 라벨링 데이터 |

**validation**

| 타입 | 파일                                           | 설명                                  |
|----|----------------------------------------------|-------------------------------------|
| -  | [val_dataset_with_label_fill_user_mean]()    | 활동, 수면 원천 데이터(같은 ID값의 평균) + 라벨링 데이터 |
| -  | [val_dataset_with_label_fill_DIAG_NM_mean]() | 활동, 수면 원천 데이터(같은 라벨링의 평균) + 라벨링 데이터 |
