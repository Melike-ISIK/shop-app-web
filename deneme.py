import pandas as pd 
import numpy as np 
import matplotlib.pylob as plt
import matplotlib.patches as mpatches
from keras.layers.core import Dense,Activation,Dropout,Flatten,Reshape
from keras.layers import LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

data_orjinal = pd.read_csv('AirPassengers.csv')
data_orjinal = data_orjinal['#Passengers']