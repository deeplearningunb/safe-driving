import pandas as pd

dataset_2017 = pd.read_csv('datasets/datatran2017.csv', sep= ';', encoding='ISO-8859-1', header=0 , infer_datetime_format=True, parse_dates=['data_inversa'], index_col=['data_inversa']).dropna().drop_duplicates()
dataset_2018 = pd.read_csv('datasets/datatran2018.csv', sep= ';', encoding='ISO-8859-1', header=0 , infer_datetime_format=True, parse_dates=['data_inversa'], index_col=['data_inversa']).dropna().drop_duplicates()
dataset_2019 = pd.read_csv('datasets/datatran2019.csv', sep= ';', encoding='ISO-8859-1', header=0 , infer_datetime_format=True, parse_dates=['data_inversa'], index_col=['data_inversa']).dropna().drop_duplicates()
dataset_2020 = pd.read_csv('datasets/datatran2020.csv', sep= ';', encoding='ISO-8859-1', header=0 , infer_datetime_format=True, parse_dates=['data_inversa'], index_col=['data_inversa']).dropna().drop_duplicates()
dataset_train = pd.concat([dataset_2017,dataset_2018,dataset_2019])
dataset_test = dataset_2020
