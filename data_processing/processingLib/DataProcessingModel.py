import numpy as np
import pandas as pd


class CSVFile:
    def __init__(self,
                 path: str,
                 name: str | None = None,
                 usecolsType: dict | None = None,
                 header: int | None = 0,
                 names: list | None = None,
                 dtype: dict | None = None,
                 index_col: int = None):
        self.path = path
        fileComponents = path.split('/')
        self.fileComponents = fileComponents
        if name is None:
            self.name = fileComponents[-1].split('.')[0] if len(fileComponents) > 0 else ''
        else:
            self.name = name
        self.header = header
        self.names = names
        if usecolsType is not None:
            self.usecols = usecolsType.keys()
            self.dtype = usecolsType
        else:
            self.usecols = None
            self.dtype = dtype
        self.index_col = index_col

    def load(self):
        data = pd.read_csv(self.path,
                           header=self.header,
                           dtype=self.dtype,
                           names=self.names,
                           usecols=self.usecols,
                           index_col=self.index_col)
        return {'header': np.array(data.columns.values.tolist()), 'data': data.to_numpy()}


class DataProcessingModel:
    files = None
    data = {}

    def __init__(self, *files: CSVFile):
        self.files = files
        for file in files:
            self.data[file.name] = file.load()

    def print_data(self, name = None):
        if name is not None:
            print(self.data[name])
        else:
            print(self.data)

    def transform(self, filename: str, f, names=None, cols=None):
        if cols is None:
            cols = []
        if names is None:
            names = []

        if filename not in self.data.keys():
            return

        if len(names) != 0:
            cols = np.argwhere(np.isin(self.data[filename]['header'], np.array(names))).flatten()

        if len(cols) != 0:
            self.data[filename]['data'][:, cols] = f(self.data[filename]['data'][:, cols])
        else:
            self.data[filename]['data'] = f(self.data[filename]['data'])

    def extract(self, filename: str, names=None, cols=None):
        if cols is None:
            cols = []
        if names is None:
            names = []

        if filename not in self.data.keys():
            return

        if len(names) != 0:
            cols = np.argwhere(np.isin(self.data[filename]['header'], np.array(names))).flatten()

        if len(cols) != 0:
            self.data[filename]['header'] = self.data[filename]['header'][cols]
            self.data[filename]['data'] = self.data[filename]['data'][:, cols]

    def save(self, filename, path):
        if filename not in self.data.keys():
            return
        try:
            pd.DataFrame(self.data[filename]['data'], columns=self.data[filename]['header']) \
                .to_csv(path, encoding="UTF-16", mode="w", index=False)
        except KeyError:
            print(f"KeyError: {filename}")

    def replaceHeader(self, filename, originHeader, newHeader):
        if filename not in self.data.keys():
            return
        self.data[filename]['header'][self.data[filename]['header'] == originHeader] = newHeader

    def move(self, filename, header, col):
        if filename not in self.data.keys():
            return
        i = np.argwhere(self.data[filename]['header'] == header).flatten()
        indexes = np.arange(0, len(self.data[filename]['header']))
        indexes = np.delete(indexes, i)
        indexes = np.concatenate([indexes[:col], i, indexes[col:]])
        self.data[filename]['header'] = self.data[filename]['header'][indexes]
        self.data[filename]['data'] = self.data[filename]['data'][:, indexes]

    def combine(self, name1, name2, fileName, on, keyF=None):
        if name1 not in self.data.keys():
            return
        if name2 not in self.data.keys():
            return
        header1 = self.data[name1]['header']
        header2 = self.data[name2]['header']
        data1 = self.data[name1]['data']
        data2 = self.data[name2]['data']
        if keyF is not None:
            header1 = np.concatenate([['key'], self.data[name1]['header']])
            masking2 = np.where(np.isin(self.data[name2]['header'], header1), False, True)
            header2 = np.concatenate([['key'], self.data[name2]['header'][masking2]])
            data1 = np.concatenate([keyF(self.data[name1]['data']), self.data[name1]['data']], axis=1)
            data2 = np.concatenate([keyF(self.data[name2]['data']), self.data[name2]['data'][:, masking2]], axis=1)
        file1 = pd.DataFrame(data1, columns=header1)
        file2 = pd.DataFrame(data2, columns=header2)

        newData = pd.merge(file1, file2, how='outer', on=on, right_index=False)
        if keyF is not None:
            newData = pd.merge(file1, file2, how='outer', on='key', right_index=False).drop(labels='key', axis=1)

        self.data[fileName] = {'header': np.array(newData.columns.values.tolist()), 'data': newData.to_numpy()}
