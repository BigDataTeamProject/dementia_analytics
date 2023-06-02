import math

from processingLib.DataProcessingModel import *
from processingLib.PathManager import *
from processingLib.DementiaDataSet import *
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


def primary():
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


def nan_filter(x):
    return np.array([d for d in x if not math.isnan(d[2]) and not math.isnan(d[10])])


def nan_filter2(x):
    return np.array([d for d in x if not math.isnan(d[2]) and not math.isnan(d[31])])


# nan filter
def secondary():
    file = CSVFile('./dataset_01/training/source/train_dataset.csv', 't')
    file2 = CSVFile('./dataset_01/validation/source/val_dataset.csv', 'v')
    dpm = DataProcessingModel(file, file2)
    dpm.filter('t', nan_filter)
    dpm.save('t', './dataset_01/training/source/train_dataset_remove_nan.csv')

    dpm.filter('v', nan_filter)
    dpm.save('v', './dataset_01/validation/source/val_dataset_remove_nan.csv')


def thirdly():
    headers = ['activity_cal_total',
               'activity_daily_movement',
               'activity_inactivity_alerts',
               'activity_rest',
               'activity_score_meet_daily_targets',
               'activity_score_stay_active',
               'activity_steps',
               'sleep_deep',
               'sleep_duration',
               'sleep_efficiency',
               'sleep_hr_average',
               'sleep_hr_lowest',
               'sleep_onset_latency',
               'sleep_rem']
    file = CSVFile('./dataset_01/training/source/train_dataset.csv', 't')
    file2 = CSVFile('./dataset_01/validation/source/val_dataset.csv', 'v')
    dpm = DataProcessingModel(file, file2)
    dpm.fill_mean('t', names=headers)
    dpm.fill_mean('v', names=headers)
    dpm.save('t', './dataset_01/training/source/train_dataset_fill_mean.csv')
    dpm.save('v', './dataset_01/validation/source/val_dataset_fill_mean.csv')


def combineDataAndLabel():
    ts = CSVFile('./dataset_01/training/source/train_dataset.csv', 'ts')
    tl = CSVFile('./dataset_01/training/label/train_dataset_label.csv', 'tl')
    vs = CSVFile('./dataset_01/validation/source/val_dataset.csv', 'vs')
    vl = CSVFile('./dataset_01/validation/label/val_dataset_label.csv', 'vl')
    dpm = DataProcessingModel(ts, tl, vs, vl)
    dpm.combine('ts', 'tl', 't', on=['ID'])
    dpm.combine('vs', 'vl', 'v', on=['ID'])
    dpm.save('t', './dataset_01/training/train_dataset_with_label.csv')
    dpm.save('v', './dataset_01/validation/val_dataset_with_label.csv')


def combineRemoveNanDataAndLabel():
    ts = CSVFile('./dataset_01/training/source/train_dataset_remove_nan.csv', 'ts')
    tl = CSVFile('./dataset_01/training/label/train_dataset_label.csv', 'tl')
    vs = CSVFile('./dataset_01/validation/source/val_dataset_remove_nan.csv', 'vs')
    vl = CSVFile('./dataset_01/validation/label/val_dataset_label.csv', 'vl')
    dpm = DataProcessingModel(ts, tl, vs, vl)
    dpm.combine('ts', 'tl', 't', on=['ID'])
    dpm.combine('vs', 'vl', 'v', on=['ID'])
    dpm.save('t', './dataset_01/training/train_dataset_with_label_remove_nan.csv')
    dpm.save('v', './dataset_01/validation/val_dataset_with_label_remove_nan.csv.csv')


def combineDataFillMeanAndLabel():
    ts = CSVFile('./dataset_01/training/source/train_dataset_fill_mean.csv', 'ts')
    tl = CSVFile('./dataset_01/training/label/train_dataset_label.csv', 'tl')
    vs = CSVFile('./dataset_01/validation/source/val_dataset_fill_mean.csv', 'vl')
    vl = CSVFile('./dataset_01/validation/label/val_dataset_label.csv', 'vs')
    dpm = DataProcessingModel(ts, tl, vs, vl)
    dpm.combine('ts', 'tl', 't', on=['ID'])
    dpm.combine('vs', 'vl', 'v', on=['ID'])
    dpm.move('t', 'DIAG_NM', 16)
    dpm.move('v', 'DIAG_NM', 16)
    dpm.save('t', './dataset_01/training/train_dataset_with_label_fill_mean.csv')
    dpm.save('v', './dataset_01/validation/val_dataset_with_label_fill_mean.csv')


def combineAll():
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
    saveBasePath = './dataset_02'
    for t in needFiles:
        dataType = t.type()
        if dataType != 'label':
            dpm.transform(t.value, extractId, names=['EMAIL'])
            dpm.replaceHeader(t.value, 'EMAIL', 'ID')
            dpm.del_cols(t.value, names=['activity_class_5min',
                                         'activity_met_1min',
                                         'activity_day_end',
                                         'CONVERT(activity_class_5min USING utf8)',
                                         'CONVERT(activity_met_1min USING utf8)',
                                         'sleep_bedtime_end',
                                         'sleep_hr_5min',
                                         'sleep_hypnogram_5min',
                                         'sleep_rmssd_5min',
                                         'CONVERT(sleep_hr_5min USING utf8)',
                                         'CONVERT(sleep_hypnogram_5min USING utf8)',
                                         'CONVERT(sleep_rmssd_5min USING utf8)'])
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


def combineAllDataAndLabel():
    ts = CSVFile('./dataset_02/training/source/train_dataset.csv', 'ts')
    tl = CSVFile('./dataset_02/training/label/train_dataset_label.csv', 'tl')
    vs = CSVFile('./dataset_02/validation/source/val_dataset.csv', 'vs')
    vl = CSVFile('./dataset_02/validation/label/val_dataset_label.csv', 'vl')
    dpm = DataProcessingModel(ts, tl, vs, vl)
    dpm.combine('ts', 'tl', 't', on=['ID'])
    dpm.combine('vs', 'vl', 'v', on=['ID'])
    dpm.save('t', './dataset_02/training/train_dataset_with_label.csv')
    dpm.save('v', './dataset_02/validation/val_dataset_with_label.csv')


def combineAllDataAndLabelFillMean():
    file = CSVFile('./dataset_02/training/train_dataset_with_label.csv', 't')
    file2 = CSVFile('./dataset_02/validation/val_dataset_with_label.csv', 'v')
    dpm = DataProcessingModel(file, file2)
    dpm.fill_mean_all('t', excepts=[0, 1, -1])
    dpm.save('t', './dataset_02/training/train_dataset_with_label_fill_mean.csv')

    dpm.fill_mean_all('v', excepts=[0, 1, -1])
    dpm.save('v', './dataset_02/validation/val_dataset_with_label_fill_mean.csv')


def combineAllDataAndLabelRemoveNan():
    file = CSVFile('./dataset_02/training/train_dataset_with_label.csv', 't')
    file2 = CSVFile('./dataset_02/validation/val_dataset_with_label.csv', 'v')
    dpm = DataProcessingModel(file, file2)
    dpm.filter('t', nan_filter2)
    dpm.save('t', './dataset_02/training/train_dataset_with_label_remove_nan.csv')

    dpm.filter('v', nan_filter2)
    dpm.save('v', './dataset_02/validation/val_dataset_with_label_remove_nan.csv')


def fillUserMean():
    file = CSVFile('./dataset_02/training/train_dataset_with_label.csv', 'f1')
    file2 = CSVFile('./dataset_02/validation/val_dataset_with_label.csv', 'f2')
    dpm = DataProcessingModel(file, file2)
    dpm.fillWhereMean('f1', mean_where_col_name='ID')
    dpm.fillWhereMean('f2', mean_where_col_name='ID')
    dpm.save('f1', './dataset_03/training/train_dataset_with_label_fill_user_mean.csv')
    dpm.save('f2', './dataset_03/validation/val_dataset_with_label_fill_user_mean.csv')


def fillDIAG_NMMean():
    file = CSVFile('./dataset_023/training/train_dataset_with_label.csv', 'f1')
    file2 = CSVFile('./dataset_02/validation/val_dataset_with_label.csv', 'f2')
    dpm = DataProcessingModel(file, file2)
    dpm.fillWhereMean('f1', mean_where_col_name='DIAG_NM')
    dpm.fillWhereMean('f2', mean_where_col_name='DIAG_NM')
    dpm.save('f1', './dataset_03/training/train_dataset_with_label_fill_DIAG_NM_mean.csv')
    dpm.save('f2', './dataset_03/validation/val_dataset_with_label_fill_DIAG_NM_mean.csv')


def findMeanWithNan():
    file = CSVFile('./dataset_02/training/train_dataset_with_label.csv', 'f1')
    file2 = CSVFile('./dataset_02/validation/val_dataset_with_label.csv', 'f2')
    dpm = DataProcessingModel(file, file2)
    dpm.findMean('f1', mean_where_col_name='DIAG_NM', withNan=True)
    dpm.findMean('f2', mean_where_col_name='DIAG_NM', withNan=True)
    dpm.save('f1', './dataset_04/training/train_dataset_with_label_find_mean_with_nan.csv')
    dpm.save('f2', './dataset_04/validation/val_dataset_with_label_find_mean_with_nan.csv')


def findMean():
    file = CSVFile('./dataset_02/training/train_dataset_with_label.csv', 'f1')
    file2 = CSVFile('./dataset_02/validation/val_dataset_with_label.csv', 'f2')
    dpm = DataProcessingModel(file, file2)
    dpm.findMean('f1', mean_where_col_name='DIAG_NM')
    dpm.findMean('f2', mean_where_col_name='DIAG_NM')
    dpm.save('f1', './dataset_04/training/train_dataset_with_label_find_mean.csv')
    dpm.save('f2', './dataset_04/validation/val_dataset_with_label_find_mean.csv')


def combineAllData():
    file = CSVFile('./dataset_02/training/train_dataset_with_label_remove_nan.csv', 'f1')
    file2 = CSVFile('./dataset_02/validation/val_dataset_with_label_remove_nan.csv', 'f2')
    file3 = CSVFile('./dataset_03/training/train_dataset_with_label_fill_user_mean.csv', 'f3')
    file4 = CSVFile('./dataset_03/validation/val_dataset_with_label_fill_user_mean.csv', 'f4')
    file5 = CSVFile('./dataset_03/training/train_dataset_with_label_fill_DIAG_NM_mean.csv', 'f5')
    file6 = CSVFile('./dataset_03/validation/val_dataset_with_label_fill_DIAG_NM_mean.csv', 'f6')
    dpm = DataProcessingModel(file, file2, file3, file4, file5, file6)
    dpm.add('f1', 'f2')
    dpm.add('f3', 'f4')
    dpm.add('f5', 'f6')
    dpm.save('f1', './dataset_05/dataset_with_label_remove_nan.csv')
    dpm.save('f3', './dataset_05/dataset_with_label_fill_user_mean.csv')
    dpm.save('f5', './dataset_05/dataset_with_label_fill_DIAG_NM_mean.csv')


def allDataMean():
    file = CSVFile('./dataset_05/dataset_with_label_remove_nan.csv', 'f1')
    file2 = CSVFile('./dataset_05/dataset_with_label_fill_user_mean.csv', 'f2')
    file3 = CSVFile('./dataset_05/dataset_with_label_fill_DIAG_NM_mean.csv', 'f3')
    dpm = DataProcessingModel(file, file2, file3)

    dpm.findMean('f1', mean_where_col_name='DIAG_NM')
    dpm.findMean('f2', mean_where_col_name='DIAG_NM')
    dpm.findMean('f3', mean_where_col_name='DIAG_NM')

    dpm.save('f1', './dataset_06/dataset_mean_with_label_remove_nan.csv')
    dpm.save('f2', './dataset_06/dataset_mean_with_label_fill_user_mean.csv')
    dpm.save('f3', './dataset_06/dataset_mean_with_label_fill_DIAG_NM_mean.csv')

def extractData():
    availableHeaders=['activity_cal_active', 'activity_cal_total', 'activity_daily_movement', 'activity_steps',
                      'sleep_awake','sleep_bedtime_end','sleep_bedtime_start','sleep_breath_average','sleep_deep','sleep_duration','sleep_hr_5min','sleep_hr_average','sleep_hr_lowest','sleep_rem', 'DIAG_NM']
    mustCheckHeaders=['activity_day_end' ,'activity_day_start', 'activity_high', 'activity_inactive', 'active_low','activity_medium','activity_met_1min','activity_met_min_high','activity_met_min_inactive','activity_met_min_low','activity_met_min_medium','activity_rest','activity_total'
                      'sleep_is_longest','sleep_temperature_delta','sleep_temperature_deviation','sleep_temperature_trend_deviation','sleep_total']
    file = CSVFile('./dataset_06/dataset_mean_with_label_remove_nan.csv', 'f1')
    file2 = CSVFile('./dataset_06/dataset_mean_with_label_fill_user_mean.csv','f3')
    file3 = CSVFile('./dataset_06/dataset_mean_with_label_fill_DIAG_NM_mean.csv','f5')
    dpm = DataProcessingModel(file, file2, file3)
    dpm.copy('f1','f2')
    dpm.copy('f3', 'f4')
    dpm.copy('f5', 'f6')
    dpm.extract('f1', names=availableHeaders)
    dpm.extract('f2', names=availableHeaders+mustCheckHeaders)
    dpm.extract('f3', names=availableHeaders)
    dpm.extract('f4', names=availableHeaders+mustCheckHeaders)
    dpm.extract('f5', names=availableHeaders)
    dpm.extract('f6', names=availableHeaders+mustCheckHeaders)
    dpm.save('f1', './dataset_07/dataset_mean_with_label_remove_nan_extract_available_headers.csv')
    dpm.save('f2', './dataset_07/dataset_mean_with_label_remove_nan_extract_must_check_header.csv')
    dpm.save('f3', './dataset_07/dataset_mean_with_label_fill_user_mean_extract_available_headers.csv')
    dpm.save('f4', './dataset_07/dataset_mean_with_label_fill_user_mean_extract_must_check_header.csv')
    dpm.save('f5', './dataset_07/dataset_mean_with_label_fill_DIAG_NM_mean_extract_available_headers.csv')
    dpm.save('f6', './dataset_07/dataset_mean_with_label_fill_DIAG_NM_mean_extract_must_check_header.csv')

def final_dataset():
    availableHeaders = ['activity_cal_active', 'activity_cal_total', 'activity_daily_movement', 'activity_steps',
                        'sleep_awake', 'sleep_bedtime_end', 'sleep_bedtime_start', 'sleep_breath_average', 'sleep_deep',
                        'sleep_duration', 'sleep_hr_5min', 'sleep_hr_average', 'sleep_hr_lowest', 'sleep_rem',
                        'DIAG_NM']

    file = CSVFile('./dataset_03/training/train_dataset_with_label_fill_user_mean.csv', 'f1')
    file2 = CSVFile('./dataset_03/validation/val_dataset_with_label_fill_user_mean.csv', 'f2')
    file3 = CSVFile('./dataset_03/training/train_dataset_with_label_fill_DIAG_NM_mean.csv', 'f3')
    file4 = CSVFile('./dataset_03/validation/val_dataset_with_label_fill_DIAG_NM_mean.csv', 'f4')
    dpm = DataProcessingModel(file, file2, file3, file4)
    dpm.add('f1','f2')
    dpm.add('f3','f4')
    dpm.extract('f1', names=availableHeaders)
    dpm.extract('f2', names=availableHeaders)
    dpm.copy('f1', 'f5')
    dpm.copy('f2','f6')
    dpm.findMean('f5', mean_where_col_name='DIAG_NM')
    dpm.findMean('f6', mean_where_col_name='DIAG_NM')
    dpm.save('f1', './dataset_08/dataset_fill_user_mean.csv')
    dpm.save('f2', './dataset_08/dataset_fill_DIAG_NM_mean.csv')
    dpm.save('f5', './dataset_08/dataset_mean_fill_user_mean.csv')
    dpm.save('f6', './dataset_08/dataset_mean_fill_DIAG_NM_mean.csv')



if __name__ == '__main__':
    final_dataset()
