import numpy as np
import os, time, sys
import tensorflow as tf

from tensorflow.contrib.rnn import LSTMCell
from tensorflow.contrib.crf import crf_log_likelihood
from tensorflow.contrib.crf import viterbi_decode

class BiLSTM_CRF(BaseModel):
    def __init__(self, config):
        self.batch_size = self.config.train.batch_size
        
    def load_data(self):
        """loads and preprocesses data"""
        self.dataset, self.info = DataLoader()
        self._preprocess_data()

    def _preprocess_data(self):
        pass

    def _set_training_parameters(self):
        pass

    def _normalize(self, input_image, input_mask):
        pass

    def _load_image_train(self, datapoint):
        pass

    def _load_image_test(self, datapoint):
        pass