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
        text = ''
        for dataset in self.dbs:
            with open(dataset) as f:
                text += f.read()
        return text
    
    def __getitem__(self, name: str) -> Any:
        return self.statistic[name]
    

