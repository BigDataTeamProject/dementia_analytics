## [치매 고위험군 웨어러블 라이프로그](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=226)

> 헬스케어 웨어러블 디바이스를 통한 원천 데이터로부터 정제 및 라벨링을 통하여 치매 진행 단계별 라이프로그 빅데이터 구축 및 인공지능 치매조기 예측모델을 활용하여 치매 걸릴 확률정보를 제공함.
>
---

### 1. 걸음 걸이

| **Training**                                                  | **Validation**                                                  |
|---------------------------------------------------------------|-----------------------------------------------------------------|
| [원천 데이터](./data/1.Training/원천데이터/1.걸음걸이/train_activity.csv)   | [원천 데이터](./data/2.Validation/원천데이터/1.걸음걸이/train_activity.csv)   |
| [라벨링 데이터](./data/1.Training/라벨링데이터/1.걸음걸이/train_label_activity.csv) | [라벨링 데이터](./data/2.Validation/라벨링데이터/1.걸음걸이/training_label.csv) |

| No | 항목                                | Comment         | Type         |
|----|-----------------------------------|-----------------|--------------|
| 1  | email                             | 이메일             | varchar(200) |
| 2  | date                              | 요약 날짜           | varchar(10)  |
| 3  | check                             | 착용 여부 체크        | varchar(20)  |
| 4  | nonwear                           | 미착용 시간 체크       | varchar(20)  |
| 5  | activity_average_met              | 하루간 평균 MET      | varchar(10)  |
| 6  | activity_cal_active               | 하루간 활동 칼로리      | varchar(10)  |
| 7  | activity_cal_total                | 하루간 총 사용 칼로리    | varchar(10)  |
| 8  | activity_class_5min               | 하루간 5분당 활동 로그   | BLOB         |
| 9  | activity_daily_movement           | 매일 움직인 거리       | varchar(10)  |
| 10 | activity_day_end                  | 활동 종료 시간        | varchar(30)  |
| 11 | activity_day_start                | 활동 시작 시간        | varchar(30)  |
| 12 | activity_high                     | 고강도 활동 시간       | varchar(10)  |
| 13 | activity_inactive                 | 비활동 시간          | varchar(10)  |
| 14 | activity_inactivity_alerts        | 비활동 알람 횟수       | varchar(10)  |
| 15 | active_low                        | 저강도 활동 시간       | varchar(10)  |
| 16 | activity_medium                   | 중강도 활동 시간       | varchar(10)  |
| 17 | activity_met_1min                 | 하루간 1분 당 MET 로그 | BLOB         |
| 18 | activity_met_min_high             | 하루간 고강도 활동 MET  | varchar(10)  |
| 19 | activity_met_min_inactive         | 하루간 비활동 MET     | varchar(10)  |
| 20 | activity_met_min_low              | 하루간 저강도 활동 MET  | varchar(10)  |
| 21 | activity_met_min_medium           | 하루간 중강도 활동 MET  | varchar(10)  |
| 22 | activity_non_wear                 | 미착용 시간          | varchar(10)  |
| 23 | activity_rest                     | 휴식 시간           | varchar(10)  |
| 24 | activity_score                    | 활동 점수           | varchar(10)  |
| 25 | activity_score_meet_daily_targets | 활동 목표달성 점수      | varchar(10)  |
| 26 | activity_score_move_every_hour    | 매 시간 당 활동유지 점수  | varchar(10)  |
| 27 | activity_score_recovery_time      | 회복시간 점수         | varchar(10)  |
| 28 | activity_score_stay_active        | 활동 유지 점수        | varchar(10)  |
| 29 | activity_score_training_frequency | 운동 빈도 점수        | varchar(10)  |
| 30 | activity_score_training_volume    | 운동 빈도 점수        | varchar(10)  |
| 31 | activity_steps                    | 매일 걸음 수         | varchar(10)  |
| 32 | activity_total                    | 활동 총 시간(분)      | varchar(10)  |

---

### 2. 수면

| **Training**                                                | **Validation**                                           |
|-------------------------------------------------------------|----------------------------------------------------------|
| [원천 데이터](./data/1.Training/원천데이터/2.수면/train_sleep.csv)      | [원천 데이터](./data/2.Validation/원천데이터/2.수면/val_sleep.csv)   |
| [라벨링 데이터](./data/1.Training/라벨링데이터/2.수면/train_label_sleep.csv) | [라벨링 데이터](./data/2.Validation/라벨링데이터/2.수면/val_label_sleep.csv) |

| No | 항목                                | Comment       | Type         |
|----|-----------------------------------|---------------|--------------|
| 1  | email                             | 이메일           | varchar(200) |
| 2  | sleep_awake                       | 깬 시간          | varchar(10)  |
| 3  | sleep_bedtime_end                 | 잠 종료시간        | varchar(30)  |
| 4  | sleep_bedtime_start               | 잠 시작시간        | varchar(30)  |
| 5  | sleep_breatj_average              | 분단 평균 호흡 수    | varchar(10)  |
| 6  | sleep_deep                        | 깊은 수면 시간      | varchar(10)  |
| 7  | sleep_duration                    | 잠 시간          | varchar(10)  |
| 8  | sleep_efficiency                  | 수면 효율         | varchar(10)  |
| 9  | sleep_hr_5min                     | 5분 당 심박동 로그   | BLOB         |
| 10 | sleep_hr_average                  | 분당 평균 심박동 수   | varchar(10)  |
| 11 | sleep_hr_lowest                   | 분당 낮은 심박동 수   | varchar(10)  |
| 12 | sleep_hypnogram_5min              | 수면 상태 로그      | BLOB         |
| 13 | sleep_is_longest                  | 본 수면 여부       | varchar(10)  |
| 14 | sleep_light                       | 가벼운 수면 시간     | varchar(10)  |
| 15 | sleep_midpoint_at_delta           | 수면 중간점 시간 델타  | varchar(10)  |
| 16 | sleep_midpoint_time               | 수면 중간점 시간     | varchar(10)  |
| 17 | sleep_onset_latency               | 수면 잠복 시간      | varchar(10)  |
| 18 | sleep_period_id                   | 수면 식별 아이디     | varchar(10)  |
| 19 | sleep_rem                         | 램수면 시간        | varchar(10)  |
| 20 | sleep_restless                    | 뒤척임 비율        | varchar(10)  |
| 21 | sleep_rmssd                       | 평균 심박동변동      | varchar(10)  |
| 22 | sleep_rmssd_5min                  | 5분 당 심박동변동 로그 | BLOB         |
| 23 | sleep_score                       | 수면 종합 점수      | varchar(10)  |
| 24 | sleep_score_alignment             | 수면 시기 점수      | varchar(10)  |
| 25 | sleep_score_deep                  | 깊은 수면 점수      | varchar(10)  |
| 26 | sleep_score_disturbances          | 수면 방해 점수      | varchar(10)  |
| 27 | sleep_score_efficiency            | 수면 효율 점수      | varchar(10)  |
| 28 | sleep_score_latency               | 수면 잠복 점수      | varchar(10)  |
| 29 | sleep_score_rem                   | 램수면 점수        | varchar(10)  |
| 30 | sleep_score_total                 | 수면 시간 기여 점수   | varchar(10)  |
| 31 | sleep_temperature_delta           | 피부 온도 편차      | varchar(10)  |
| 32 | sleep_temperature_deviation       | 피부 온도 편차      | varchar(10)  |
| 33 | sleep_temperature_trend_deviation | 피부 온도 경향 편차   | varchar(10)  |
| 34 | timezone                          | 시간 장소 정보      | varchar(10)  |
| 35 | sleep_total                       | 수면 시간         | varchar(10)  |

---

### 3. 인지 기능

| **Training**                                                  | **Validation**                                             |
|---------------------------------------------------------------|------------------------------------------------------------|
| [원천 데이터](./data/1.Training/원천데이터/3.인지기능/train_mmse.csv)       | [원천 데이터](./data/2.Validation/원천데이터/3.인지기능/val_mmse.csv)    |
| [라벨링 데이터](./data/1.Training/라벨링데이터/3.인지기능/train_label_mmse.csv) | [라벨링 데이터](./data/2.Validation/라벨링데이터/3.인지기능/val_label_mmse.csv) |

| No | 항목            | Comment                                                                                                                                                                          | Type         |
|----|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 1  | SAMPLE_EMAIL  | 연구대상자 이메일                                                                                                                                                                        | VARCHAR(200) |
| 2  | DIAG_SEQ      | 차수                                                                                                                                                                               | INT(3)       |
| 3  | DIAG_NIM      | 진단명                                                                                                                                                                              | VARCHAR(30)  |
| 4  | DOCTOR_NM     | 진단자                                                                                                                                                                              | VARCHAR(50)  |
| 5  | MMSE_NUM      | 횟수                                                                                                                                                                               | INT          |
| 6  | MMSE_KIND     | 친절도                                                                                                                                                                              | VARCHAR(10)  |
| 7  | Q01           | 올해가 몇 년 이지요?                                                                                                                                                                     | VARCHAR(1)   |
| 8  | Q02           | 지금은 어떤 계절이지요?                                                                                                                                                                    | VARCHAR(1)   |
| 9  | Q03           | 오늘은 며칠입니까?                                                                                                                                                                       | VARCHAR(1)   |
| 10 | Q04           | 오늘은 무슨 요일인가요?                                                                                                                                                                    | VARCHAR(1)   |
| 11 | Q05           | 오늘이 몇 월입니까?                                                                                                                                                                      | VARCHAR(1)   |
| 12 | Q06           | 지금 우리가 있는 이곳은 어느 나라입니까?                                                                                                                                                          | VARCHAR(1)   |
| 13 | Q07           | 우리가 지금 무슨 시(도)에 있습니까?                                                                                                                                                            | VARCHAR(1)   |
| 14 | Q08           | 지금 우리가 있는 여기는 어디입니까? (지금 계시는 이곳을 무엇이라고 부릅니까?)                                                                                                                                    | VARCHAR(1)   |
| 15 | Q09           | 지금 우리가 있는 이곳은 몇 층입니까?                                                                                                                                                            | VARCHAR(1)   |
| 16 | Q10           | 여기에서는 어떤 일을 하나요?                                                                                                                                                                 | VARCHAR(1)   |
| 17 | Q11_1         | 자, 잘 들으세요. 제가 지금부터 물건 이름 세 개를 불러드리겠습니다. 세 가지를 다 들으시고 나서 그대로 외워서 저에게 말씀해주세요. 준비되셨습니까? 자, 제가 무어라고 했지요? 말씀해보세요. 지금 불러드린 그 물건 이름들을 잘 기억하고 계세요. 제가 조금 있다가 다시 외워보시라고 할겁니다. 비행기(1초감 멈춤) | VARCHAR(1)   |
| 18 | Q11_2         | 연필(1초간 멈춤)                                                                                                                                                                       | VARCHAR(1)   |
| 19 | Q11_3         | 소나무                                                                                                                                                                              | VARCHAR(1)   |
| 20 | Q12_1         | 100에서 7을 빼면 얼마가 됩니까?                                                                                                                                                             | VARCHAR(2)   |
| 21 | Q12_2         | 거기에서 7을 빼면 얼마가 됩니까?                                                                                                                                                              | VARCHAR(2)   |
| 22 | Q12_3         | 거기에서 7을 빼면 얼마가 됩니까?                                                                                                                                                              | VARCHAR(2)   |
| 23 | Q12_4         | 거기에서 7을 빼면 얼마나 됩니까?                                                                                                                                                              | VARCHAR(2)   |
| 24 | Q12_5         | 거기에서 7을 빼면 얼마가 됩니까?                                                                                                                                                              | VARCHAR(2)   |
| 25 | Q12_TOTAL     | INT                                                                                                                                                                              |              |
| 26 | Q13_1         | 좀 전에 제가 외우고 계시라고 했던 물건 이름 세가지 기억나세요? 비행기                                                                                                                                         | VARCHAR(1)   |
| 27 | Q13_2         | 연필                                                                                                                                                                               | VARCHAR(1)   |
| 28 | Q13_3         | 소나무                                                                                                                                                                              | VARCHAR(1)   |
| 29 | Q14_1         | 이것이 무엇입니까?(시계)                                                                                                                                                                   | VARCHAR(1)   |
| 30 | Q14_2         | 이것이 무엇입니까?                                                                                                                                                                       | VARCHAR(1)   |
| 31 | Q15           | 이번에는 제가 하는 말을 그대로 따라서 말씀하시면 됩니다. (백문일 불여일견)                                                                                                                                      | VARCHAR(1)   |
| 32 | Q16_1         | 종이 뒤집기                                                                                                                                                                           | VARCHAR(1)   |
| 34 | Q16_2         | 반으로 접기                                                                                                                                                                           | VARCHAR(1)   |
| 35 | Q16_3         | 되돌려 주기                                                                                                                                                                           | VARCHAR(1)   |
| 35 | Q17           | 이 그림과 똑같이 여기에 그려주세요. (별지의 오각형 그림)                                                                                                                                                | VARCHAR(1)   |
| 36 | Q18           | 지금 보여 드리는 이 문장을 큰 소리로 읽으시고 쓰인 대로 해보세요.                                                                                                                                           | VARCHAR(1)   |
| 37 | Q19           | 여기에 오늘 날씨(또는 기분)에 대해서 문장으로 써보세요.                                                                                                                                                 | VARCHAR(1)   |
| 38 | TOTAL         | 총점                                                                                                                                                                               | INT          |
| 39 | TEST_DAY      | 검사일                                                                                                                                                                              | DATETIME     |
| 40 | FLAG          | FLAG                                                                                                                                                                             | VARCHAR(1)   |
| 41 | INSERT_DATE   | 입력일                                                                                                                                                                              | DATETIME     |
| 42 | INSERT_USERID | 입력한 ID_number                                                                                                                                                                    | INT          |
| 43 | UPDATE_DATE   | 입데이트일                                                                                                                                                                            | DATETIME     |
| 44 | UPDATE_USERID | 업데이트한 ID_number                                                                                                                                                                  | INT          |