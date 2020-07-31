
import logging
import math
import os
import pandas as pd
import pickle
import sqlite3

from datetime import date
import numpy as np


def run_training() -> None:
    """Train the model."""
    data_preprocessing()
    split_data()
    fit_and_save_model()
    predict_test()
    measure_model_performance()


def data_preprocessing():
    print('data_preprocessing...OK.')
    pass


def split_data():
    print('split_data...OK.')
    pass


def fit_and_save_model():
    print('fit_and_save_model...OK.')
    pass


def predict_test():
    print('predict_test...OK.')
    pass


def measure_model_performance():
    print('measure_model_performance...OK.')
    pass


if __name__ == "__main__":
    #run_training()
    #run_prediction()
    data_preprocessing()
    split_data()
    fit_and_save_model()
    predict_test()
    measure_model_performance()