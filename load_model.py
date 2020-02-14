import os
import pymongo
import openpyxl
from strcountup import str_count
import pandas as pd
from joblib import dump, load
import io



clf = load('tree.joblib') 
label_names =["貨名","產地","PO","料號"]


strTTEst="你好"
count=str_count(strTTEst)
print(count)
my_prediction = clf.predict(count)
bingo=my_prediction[0]
print(label_names[bingo])