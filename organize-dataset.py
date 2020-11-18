import pandas as pd
from unicodedata import normalize
def accent_remover(x):

    try:
        float(x)
        return x
    except:
        return normalize('NFKD',x).encode('ASCII', 'ignore').decode('ASCII')

dataset_2017 = pd.read_csv('datasets/datatran2017.csv', sep= ';', encoding='ISO-8859-1').dropna().drop_duplicates()
dataset_2018 = pd.read_csv('datasets/datatran2018.csv', sep= ';', encoding='ISO-8859-1').dropna().drop_duplicates()
dataset_2019 = pd.read_csv('datasets/datatran2019.csv', sep= ';', encoding='ISO-8859-1').dropna().drop_duplicates()
dataset = pd.concat([dataset_2017,dataset_2018,dataset_2019])

dataset = dataset.transform([accent_remover])
dataset.columns = dataset.columns.droplevel(1)

