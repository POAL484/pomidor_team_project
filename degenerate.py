import numpy as np
import tensorflow as tf
from datasets_analizer import DataSetsAnalizer
import os


dsets = DataSetsAnalizer(lang='russian')


# ''.join( [ str(ord(letter)) for letter in list(c) ] )


class NLP_Models():
    def __init__(self, prompt) -> None:
        self.prompt = prompt


    class Generation_Model():
        def __init__(self) -> None:
            ...
    

    class ClasificationModel():
        def __init__(self) -> None:
            ...
    


if __name__ == '__main__':
    ...