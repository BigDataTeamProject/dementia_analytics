from data_processing.processingLib.DataProcessingModel import *
from data_processing.processingLib.PathManager import *
from data_processing.processingLib.DementiaDataSet import *
import numpy as np
import re
import datetime


def extractId(x):
    pattern = r"\+([0-9]+)@"
    regex = re.compile(pattern)
    extracted_nums = [regex.search(s[0]).group(1) for s in x if regex.search(s[0]) is not None]
    x = np.array([[num] for num in extracted_nums])
    return x


def extractId2(x):
    pattern = r"\+([0-9]+)@"
    regex = re.compile(pattern)
    for i in x:
        print(i[0], regex.search(i[0]))
    extracted_nums = [regex.search(s[0]).group(1) for s in x]
    x = np.array([[num] for num in extracted_nums])
    return x


def toActivityDate(x):
    getDate = lambda d: datetime.datetime.strptime(d[:19], "%Y-%m-%dT%H:%M:%S").date()
    toStr = lambda d: d.strftime('%Y/%m/%d')
    strDates = [toStr(getDate(d[0])) for d in x]
    x = np.array([[d] for d in strDates])
    return x


def toSleepDate(x):
    getDate = lambda d: (datetime.datetime.strptime(d[:19], "%Y-%m-%dT%H:%M:%S").date() - datetime.timedelta(hours=5))
    toStr = lambda d: d.strftime('%Y/%m/%d')
    strDates = [toStr(getDate(d[0])) for d in x]
    x = np.array([[d] for d in strDates])
    return x


if __name__ == '__main__':
    # 가져올 header
    headers = ['EMAIL',
               'date',
               'activity_day_start',
               'sleep_bedtime_start',
               'activity_cal_total',
               'activity_daily_movement',
               'activity_inactivity_alerts',
               'activity_rest',
               'activity_score_meet_daily_targets',
               'activity_score_stay_active',
               'activity_steps',
               'sleep_deep',
               'sleep_duration',
               'sleep_efficiency',
               # 'sleep_hr_5min', .... <- 밖에 없음
               'sleep_hr_average',
               'sleep_hr_lowest',
               'sleep_onset_latency',
               'sleep_rem']

    pm = PathManager('../dementia_dataset/data')

    needFiles = [DementiaDataSet.train_activity,
                 DementiaDataSet.train_sleep,
                 DementiaDataSet.val_activity,
                 DementiaDataSet.val_sleep,
                 DementiaDataSet.train_label_activity,
                 DementiaDataSet.train_label_sleep,
                 DementiaDataSet.val_label_activity,
                 DementiaDataSet.val_label_sleep]

    files = [CSVFile(pm.getPath(pm.find(n.fileName())), n.value)
             for n in needFiles]

    # 데이터 추출
    dpm = DataProcessingModel(*files)
    saveBasePath = './dataset_01'
    for t in needFiles:
        dataType = t.type()
        if dataType != 'label':
            dpm.extract(t.value, names=headers)
            dpm.transform(t.value, extractId, names=['EMAIL'])
            dpm.replaceHeader(t.value, 'EMAIL', 'ID')
            if dataType == 'activity':
                dpm.replaceHeader(t.value, 'activity_day_start', 'date')
                dpm.transform(t.value, toActivityDate, names=['date'])
                dpm.move(t.value, 'date', 1)
            elif dataType == 'sleep':
                dpm.replaceHeader(t.value, 'sleep_bedtime_start', 'date')
                dpm.transform(t.value, toSleepDate, names=['date'])
        else:
            dpm.replaceHeader(t.value, 'SAMPLE_EMAIL', 'ID')
            dpm.transform(t.value, extractId, names=['ID'])
        dpm.save(t.value, f'{saveBasePath}{t.savePath()}')

    combineData = [(DementiaDataSet.train_activity,
                    DementiaDataSet.train_sleep,
                    '/training/source/train_dataset.csv',
                    ['ID', 'date']),
                   (DementiaDataSet.val_activity,
                    DementiaDataSet.val_sleep,
                    '/validation/source/val_dataset.csv',
                    ['ID', 'date']),
                   (DementiaDataSet.train_label_activity,
                    DementiaDataSet.train_label_sleep,
                    '/training/label/train_dataset_label.csv',
                    ['ID', 'DIAG_NM']),
                   (DementiaDataSet.val_label_activity,
                    DementiaDataSet.val_label_sleep,
                    '/validation/label/val_dataset_label.csv',
                    ['ID', 'DIAG_NM'])]

    for t1, t2, path, on in combineData:
        dpm.combine(t1.value, t2.value, 't', on=on)
        dpm.save('t', f'{saveBasePath}{path}')
