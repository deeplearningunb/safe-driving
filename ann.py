import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
from sklearn.preprocessing import MinMaxScaler
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split

def accent_remover(x):
    try:
        float(x)
        return x
    except:
        return normalize('NFKD',x).encode('ASCII', 'ignore').decode('ASCII')

# Importa os datasets
dataset_2017 = pd.read_csv('datasets/datatran2017.csv', sep= ';', encoding='ISO-8859-1').dropna().drop_duplicates()
dataset_2018 = pd.read_csv('datasets/datatran2018.csv', sep= ';', encoding='ISO-8859-1').dropna().drop_duplicates()
dataset = pd.concat([dataset_2017,dataset_2018])

dataset = dataset.transform([accent_remover])
dataset.columns = dataset.columns.droplevel(1)

# Pega as dados das colunas:
# data_inversa	dia_semana	horario	uf	br	km	condicao_metereologica	latitude	longitude
training_set = dataset.iloc[:, [1,2,3,4,5,6,13,25,26]].values

# Converte os dados de string para number
encoder = LabelEncoder()
training_set[:,0] = encoder.fit_transform(training_set[:,0])
training_set[:,1] = encoder.fit_transform(training_set[:,1])
training_set[:,2] = encoder.fit_transform(training_set[:,2])
training_set[:,3] = encoder.fit_transform(training_set[:,3])
training_set[:,4] = encoder.fit_transform(training_set[:,4])
training_set[:,5] = encoder.fit_transform(training_set[:,5])
training_set[:,6] = encoder.fit_transform(training_set[:,6])
training_set[:,7] = encoder.fit_transform(training_set[:,7])
training_set[:,8] = encoder.fit_transform(training_set[:,8])

# Converte os dados para uma mesma faixa de valores de 0 a 1
sc = MinMaxScaler(feature_range = (0, 1))
training_set_scaled = sc.fit_transform(training_set)

# Cria a estrutura do dados com 60 timesteps e 1 saida
X_train = []
y_train = []
for i in range(60, 1258):
    X_train.append(training_set_scaled[i-60:i,:])
    y_train.append(training_set_scaled[i,:])
X_train, y_train = np.array(X_train), np.array(y_train)

# Cria a RNN
regressor = Sequential()
regressor.add(LSTM(units = 50, return_sequences = True, input_shape=(60,9)))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))
regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))
regressor.add(Dense(units = 9))

# Compila
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

# Executa o treinamento
regressor.fit(X_train, y_train, epochs = 10, batch_size = 32)

# Testando os dados analisados com os de 2019
dataset_test = pd.read_csv('datasets/datatran2019.csv', sep= ';', encoding='ISO-8859-1').dropna().drop_duplicates()
dataset_test = dataset_test.transform([accent_remover])
dataset_test.columns = dataset_test.columns.droplevel(1)

real_data = dataset_test.iloc[:, [1,2,3,4,5,6,13,25,26]].values
encoder = LabelEncoder()
real_data[:,0] = encoder.fit_transform(real_data[:,0])
real_data[:,1] = encoder.fit_transform(real_data[:,1])
real_data[:,2] = encoder.fit_transform(real_data[:,2])
real_data[:,3] = encoder.fit_transform(real_data[:,3])
real_data[:,4] = encoder.fit_transform(real_data[:,4])
real_data[:,5] = encoder.fit_transform(real_data[:,5])
real_data[:,6] = encoder.fit_transform(real_data[:,6])
real_data[:,7] = encoder.fit_transform(real_data[:,7])
real_data[:,8] = encoder.fit_transform(real_data[:,8])

# Realiza a predicao dos dados
inputs = real_data
inputs = sc.fit_transform(inputs)
X_test = []
for i in range(60, 80):
    X_test.append(inputs[i-60:i,:])
X_test = np.array(X_test)
predicted_data = regressor.predict(X_test)
predicted_data = sc.inverse_transform(predicted_data)

## ANN
# Selecionando dataset Treinamento
X = []
y = []
for i in predicted_data:
	X.append(i)
	y.append(1)

X_train = X
y_train = y

# Converte os dados para uma mesma faixa de valores de 0 a 1
sc = MinMaxScaler(feature_range = (0, 1))
X_train = sc.fit_transform(X_train)

# Cria a ANN
classifier = Sequential()
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu', input_dim=9))
classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
classifier.fit(X_train, y_train, batch_size = 10, epochs = 30)

# Entrada dos dados do usuario
test = []
test.append(input("Digite a data_inversa:\nEx:'2019-01-01'\n"))
test.append(input("Digite o dia_semana:\nEx:'terça-feira'\n"))
test.append(input("Digite a horario:\nEx:'01:30:00'\n"))
test.append(input("Digite a uf:\nEx:'SP'\n"))
test.append(input("Digite a br:\nEx:'116'\n"))
test.append(input("Digite a km:\nEx:'218'\n"))
test.append(input("Digite a condicao_metereologica:\nEx:'Céu Claro'\n"))
test.append(input("Digite a latitude:\nEx:'-23,46052014'\n"))
test.append(input("Digite a longitude:\nEx:'-46,48772478'\n"))

test = pd.DataFrame({'dados': test})
test = encoder.fit_transform(test.dados)
test = np.reshape(test, (-1, 1))
test = sc.fit_transform(test[:])
test = np.reshape(test, (1, -1))

# Predicao
y_pred = classifier.predict(test)
value = round(float(y_pred[0][0])*100, 2)
print("\n\n---> Probabilidade de ocorrer acidente: ", value)