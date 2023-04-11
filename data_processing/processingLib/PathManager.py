import os
import hashlib


class PathData:
    id = None
    name = None
    parentId = None
    childIds = []

    def __init__(self, id, name, parentId):
        self.id = id
        self.name = name
        self.parentId = parentId

    def __str__(self):
        return f"id: {self.id}\n" \
               f"name: {self.name}\n" \
               f"parentId: {self.parentId}\n"


class PathManager:
    pathDataTable = {}  # { hash: PathData }
    nameDataTable = {}  # { name: hash }

    def __init__(self, basePath):
        self.basePath = basePath
        for root, dirs, files in os.walk(basePath):
            rootPath = root.replace(basePath, 'basePath')
            component = rootPath.split('/')
            parentId = self.toHash('/'.join(component[:-1])) if len(component) > 1 else None
            pathId = self.toHash(rootPath)
            self.pathDataTable[pathId] = PathData(pathId, component[-1], parentId)
            if parentId is not None:
                self.pathDataTable[parentId].childIds.append(pathId)
            for fileName in files:
                fileId = self.toHash(rootPath + f'/{fileName}')
                self.pathDataTable[fileId] = PathData(fileId, fileName, pathId)
                self.pathDataTable[pathId].childIds.append(fileId)

    @staticmethod
    def toHash(s):
        return hashlib.md5(s.encode('utf-8')).hexdigest()

    def register(self, name, path):
        path = path.replace(self.basePath, 'basePath')
        self.nameDataTable[name] = self.toHash(path)

    def getPath(self, customName: str):
        pathHash = self.nameDataTable[customName]
        pathData = self.pathDataTable[pathHash]
        path = []
        while pathData is not None:
            path.append(pathData.name)
            if pathData.parentId is None:
                break
            pathData = self.pathDataTable[pathData.parentId]
        return '/'.join(list(reversed(path))).replace('basePath', self.basePath)

    def getPath(self, path: PathData):
        pathData = path
        path = []
        while pathData is not None:
            path.append(pathData.name)
            if pathData.parentId is None:
                break
            pathData = self.pathDataTable[pathData.parentId]
        return '/'.join(list(reversed(path))).replace('basePath', self.basePath)

    def find(self, name):
        for key in self.pathDataTable.keys():
            if self.pathDataTable[key].name == name:
                return self.pathDataTable[key]
        return None

    def find_all(self, name):
        result = []
        for key in self.pathDataTable.keys():
            if self.pathDataTable[key].name == name:
                result.append(self.pathDataTable[key])
        return result
