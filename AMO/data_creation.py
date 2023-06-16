# -*- coding: utf-8 -*-
"""AMO_1_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uMJOK3tuhBFY0MVymkQUoASYnHyo8O60
"""

!pip install faker

from faker import Faker
fake = Faker()

import random

import random

def temperature(date):
    if(date.month<=2 or date.month>=12):
        return random.randint(-35,0)
    elif(date.month>=3 and date.month<6):
        return random.randint(-10,25)
    elif(date.month>=6 and date.month<9):
        return random.randint(10,40)
    elif(date.month>=9 and date.month<12):
        return random.randint(-20,10)

def nebulosity(precipitation):
    if(precipitation):
        return random.randint(60,100)
    else:
        return random.randint(0,100)

def ultraviolet(nebulosity):
    if (nebulosity) < 20:
      return random.randint(10,15)
    else:
      return random.randint(0,10)

import pandas as pd

df_train = pd.DataFrame(
    [
        {

            "date": fake.date_this_century(),
            "speed": random.randint(0,25),
            "time": fake.time(),
            "nebulosity": 0,
            "precipitation": fake.boolean(),
            "temperature": 0,
            "ultraviolet": 0,
        }
        for _ in range(1000)
    ]
)

df_train['temperature'] = df_train['date'].apply(lambda x: temperature(x))
df_train['nebulosity'] = df_train['precipitation'].apply(lambda x: nebulosity(x))
df_train['ultraviolet'] = df_train['nebulosity'].apply(lambda x: ultraviolet(x))

import os
if not os.path.isdir("train"):
     os.mkdir("train")

df_train.to_csv (r'train/train.csv', index= False )

df_test = pd.DataFrame(
    [
        {

            "date": fake.date_this_century(),
            "speed": random.randint(0,25),
            "time": fake.time(),
            "nebulosity": 0,
            "precipitation": fake.boolean(),
            "temperature": 0,
            "ultraviolet": 0,
        }
        for _ in range(250)
    ]
)

df_test['temperature'] = df_test['date'].apply(lambda x: temperature(x))
df_test['nebulosity'] = df_test['precipitation'].apply(lambda x: nebulosity(x))
df_test['ultraviolet'] = df_test['nebulosity'].apply(lambda x: ultraviolet(x))

if not os.path.isdir("test"):
     os.mkdir("test")

df_test.to_csv (r'test/test.csv', index= False )