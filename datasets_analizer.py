import snowballstemmer
from os import listdir as ls
from typing import Any



class DataSetsAnalizer():
    def __init__(self, path: str = 'datasets', lang: str ='english') -> None:
        '''Small class for easy adding datasets, without any updates in code

params:

    path: path to your datasets folder, default - "datasets" (folder from file was running)
    lang: Your datasets language, default - English. supported languages: https://pypi.org/project/snowballstemmer/

Returns:
    str - all text from all datasets'''
        self.stemmer = snowballstemmer.stemmer(lang)
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
        
        max_len = -10 * 9
        res = []
        for t in self.text.split('\n'):
            res.extend( self.stemmer.stemWords( t.split() ) )
            if len( t.split() ) >= max_len:
                max_len = len(t.split())
        self.statistic['shape'] = max_len
        self.statistic['stemmed_datasets'] = res
        return self.text
    

    def __getitem__(self, name: str) -> Any:
        return self.statistic[name]

if __name__ == '__main__':
    DSA = DataSetsAnalizer(lang='russian')
    print(str(DSA)[:10])
    print(DSA['datasets'])