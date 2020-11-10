import pandas as pd

data_set2017 = pd.read_csv('datasets/datatran2017.csv', sep= ';', encoding='ISO-8859-1').dropna().drop_duplicates()
data_set2018 = pd.read_csv('datasets/datatran2018.csv', sep= ';', encoding='ISO-8859-1').dropna().drop_duplicates()
data_set2019 = pd.read_csv('datasets/datatran2019.csv', sep= ';', encoding='ISO-8859-1').dropna().drop_duplicates()
dataset_train = pd.concat([data_set2017,data_set2018,data_set2019])
    
