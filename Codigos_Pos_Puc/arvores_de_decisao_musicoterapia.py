# -*- coding: utf-8 -*-
"""
Created on Tue May 30 07:54:07 2023

@author: nepor
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix


base = pd.read_csv('D:\Codigos_VSCODE\Programas_didaticos_Inteigencia_artifical\machine_learning\mxmh_survey_results.csv')
#Eliminando colunas que considero desnecessaria para estudo(como indices etc)

base = base.drop(columns = ['Timestamp', 'Primary streaming service', 'Exploratory', 'Permissions'])

base = base.dropna()


X = base.iloc[:, [x  for x in range (28)]].values 
y = base.iloc[:,28].values


labelEncoder = LabelEncoder()

for i in range(X.shape[1]):
    X[:,i] = labelEncoder.fit_transform(X[:,i])
    
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X, y,
                                                                  test_size= 0.3,
                                                                  random_state = 0)


modelo1 = DecisionTreeClassifier(criterion= 'entropy')
modelo1.fit(X_treinamento, y_treinamento)
export_graphviz(modelo1, out_file = 'modelo1_musicoterapia.dot')#gera esse arquivo.dot

#PREVISOES

previsoes1 = modelo1.predict(X_teste)
accuracy_score(y_teste, previsoes1) #comparar previsão com dados y obtidos
confusao1 = ConfusionMatrix(modelo1) # gerar confusão
confusao1.fit(X_treinamento, y_treinamento)#treino
confusao1.score(X_teste, y_teste)#teste
confusao1.poof()
#plotar matriz de confusao

#MODA

ocorrencias = base.groupby(['Fav genre']).size()
ocorrencias.sort_values(ascending=False)

quem_escuta_rock_com_menos_de_36_anos_efeito_ansiedade = (base.loc[(base['Fav genre'] == 'Rock') & (base['Age'] < 36.0) & (base['Anxiety'] != 0)])

df_rock_ansiedade_36_anos = quem_escuta_rock_com_menos_de_36_anos_efeito_ansiedade.iloc[:, [0,24,28]]

df_rock_ansiedade_36_anos.groupby(['Music effects']).size()

df_jazz_de_vez_em_quando_trabalho = (base.loc[(base['Frequency [Jazz]'] == 'Sometimes') & (base['While working'] == 'Yes')])
df_jazz_de_vez_em_quando_trabalho.groupby(['Music effects']).size()
df_ansiedade_jazz = (df_jazz_de_vez_em_quando_trabalho.loc[df_jazz_de_vez_em_quando_trabalho['Anxiety']!= 0])
df_ocd_jazz = (df_jazz_de_vez_em_quando_trabalho.loc[df_jazz_de_vez_em_quando_trabalho['OCD']!= 0])
df_insomnia_jazz = (df_jazz_de_vez_em_quando_trabalho.loc[df_jazz_de_vez_em_quando_trabalho['Insomnia']!= 0])
df_depression_jazz = (df_jazz_de_vez_em_quando_trabalho.loc[df_jazz_de_vez_em_quando_trabalho['Depression']!= 0])
df_ansiedade_jazz.groupby(['Music effects']).size()
df_ocd_jazz.groupby(['Music effects']).size()
df_insomnia_jazz.groupby(['Music effects']).size()
df_depression_jazz.groupby(['Music effects']).size()
df_instrumental_work = (base.loc[(base['Instrumentalist'] == 'Yes') & (base['While working'] == 'Yes')])
df_instrumental_work.groupby(['Music effects']).size()