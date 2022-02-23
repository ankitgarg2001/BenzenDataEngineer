import pandas as pd 
import matplotlib.pyplot as plt
import numpy as

data = pd.read_csv('2022_02_08-02_30_31_AM.csv')
# Ques1
print(data['price_string'].isnull().sum())
