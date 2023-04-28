## Data Processing

---

### dataset_01

**Training**

| 타입         | 파일                                      | 설명                                       |
|------------|-----------------------------------------|------------------------------------------|
| label      | [train_dataset_label]()                 | training dataset                         |
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
| label      | [val_dataset_label]()                 | training dataset                         |
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

| 타입     | 파일                                      | 설명                               |
|--------|-----------------------------------------|----------------------------------|
| label  | [train_dataset_label]()                 | training dataset                 |
|        | [train_label_activity]()                | 활동 라벨링 데이터                       |
|        | [train_label_sleep]()                   | 수면 라벨링 데이터                       |
| source | [train_activity]()                      | 활동 원천 데이터                        |
|        | [train_sleep]()                         | 수면 원천 데이터                        |
|        | [train_dataset]()                       | 활동, 수면 원천 데이터                    |
|        | [train_dataset_fill_mean]()             | 활동, 수면 원천 데이터 (평균 값)             |
|        | [train_dataset_remove_nan]()            | 활동, 수면 원천 데이터 (NaN 제거)           |
|        | [train_dataset_with_label]()            | 활동, 수면 원천 데이터  + 라벨링 데이터         |
|        | [train_dataset_with_label_fill_mean]()  | 활동, 수면 원천 데이터 (평균 값) + 라벨링 데이터   |
|        | [train_dataset_with_label_remove_nan]() | 활동, 수면 원천 데이터 (NaN 제거) + 라벨링 데이터 |