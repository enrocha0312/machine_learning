# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:38:48 2023

@author: nepor
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

base = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Inteigencia_artifical\machine_learning\mxmh_survey_results.csv')
#Eliminando colunas que considero desnecessaria para estudo(como indices etc)

base = base.drop(columns = ['Timestamp', 'Primary streaming service', 'Permissions'])

base = base.dropna()
#PRIMEIRO PREVER SE HÁ DE MANEIRA GERAL ALGUMA MELHORIA

X = base.iloc[:, [x  for x in range (29)]].values 
y = base.iloc[:,29].values


base_improve = base.loc[base['Music effects'] == 'Improve']
base_worsen = base.loc[base['Music effects'] == 'Worsen']
base_noEffect = base.loc[base['Music effects'] == 'No effect']


#transformar os dados, pois estão em categorias
#precisamos transformá-los em numéricos


labelEncoder = LabelEncoder()

for i in range(X.shape[1]):
    X[:,i] = labelEncoder.fit_transform(X[:,i])
    
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y,
                                                                  test_size= 0.3,
                                                                  random_state = 0)


#70% da tabela pra probabilidade
#30% para teste
#random_state usa sempre os mesmos dados de execução
#14000 registros com a tabela de probabilidade
#30% para teste 

modelo = GaussianNB()
modelo.fit(X_treinamento, y_treinamento)#cria tabela de modelo



previsoes =  modelo.predict(X_teste)#previsao

accuracy_score(y_teste,previsoes)#mostra taxa de acerto do algoritmo

confusao = ConfusionMatrix(modelo, classes = ['Improve', 'No effect', 'Worsen'])
confusao.fit(X_treinamento, y_treinamento)
confusao.score(X_teste, y_teste)
confusao.poof()
