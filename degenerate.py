import numpy as np
import tensorflow as tf
from datasets_analizer import DataSetsAnalizer
import os
import time


dsets = DataSetsAnalizer(lang='russian')


# ''.join( [ str(ord(letter)) for letter in list(c) ] )


class NLP_Models():
    def __init__(self, prompt) -> None:
        self.prompt = prompt


    class Generation_Model():
        def __init__(selfg) -> None:
            text = dsets['stemmed_datasets']
            vocab = sorted(set(text))
            all_ids = ids_from_chars(tf.strings.unicode_split(' '.join(text), 'UTF-8'))
            ids_from_chars = tf.keras.layers.StringLookup(vocabulary=list(vocab), mask_token=None)
    
    class ClasificationModel():
        def __init__(selfc) -> None:
            ...
    


if __name__ == '__main__':
    ...