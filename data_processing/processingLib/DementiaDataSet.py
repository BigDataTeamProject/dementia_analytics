from enum import Enum


class DementiaDataSet(Enum):
    train_activity = 'train_activity'
    train_sleep = 'train_sleep'
    train_mmse = 'train_mmse'
    train_label_activity = 'train_label_activity'
    train_label_sleep = 'train_label_sleep'
    train_label_mmse = 'train_label_mmse'

    val_activity = 'val_activity'
    val_sleep = 'val_sleep'
    val_mmse = 'val_mmse'
    val_label_activity = 'val_label_activity'
    val_label_sleep = 'val_label_sleep'
    val_label_mmse = 'val_label_mmse'

    def fileName(self):
        return f"{self.value}.csv"

    def type(self):
        if self.value.find('label') != -1:
            return 'label'
        elif self.value.find('activity') != -1:
            return 'activity'
        elif self.value.find('sleep') != -1:
            return 'sleep'
        elif self.value.find('mmse') != -1:
            return 'mmse'
        else:
            return ''

    def savePath(self):
        paths = []
        if self.value.find('val') != -1:
            paths.append('validation')
        else:
            paths.append('training')

        if self.value.find('label') != -1:
            paths.append('label')
        else:
            paths.append('source')

        paths.append(self.fileName())
        return '/' + '/'.join(paths)
