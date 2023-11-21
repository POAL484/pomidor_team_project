from os import listdir as ls
from typing import Any

class DataSetsAnalizer():
    def __init__(self, path: str = 'datasets') -> None:
        '''Small class for easy adding datasets, without any updates in code
params:
    path: path to your datasets folder, default - "datasets" (folder from file was running)

returns:
    str - all text from all datasets'''
        self.path = path
        self.dbs = [f'{path}/{ds}' for ds in ls(path)]
        self.statistic = {'count': len(self.dbs),
                     'datasets': self.dbs,
                     'path': path}

    def __str__(self) -> str:
        self.text = ''
        for dataset in self.dbs:
            with open(dataset, encoding='utf-8') as f:
                self.text += f.read()
        return self.text
    

    def __getitem__(self, name: str) -> Any:
        return self.statistic[name]

if __name__ == '__main__':
    DSA = DataSetsAnalizer()
    print(str(DSA)[:10])
    print(DSA['datasets'])