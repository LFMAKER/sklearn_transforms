from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing

import pandas as pd

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class ConvertColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        le = preprocessing.LabelEncoder()
        data['Local de trabalho'] = le.fit_transform(data['Local de trabalho'])
        data['Departmento'] = le.fit_transform(data['Departmento'])
        data['Educacao'] = le.fit_transform(data['Educacao'])
        data['Area'] = le.fit_transform(data['Area'])
        data['Genero'] = le.fit_transform(data['Genero'])
        data['Cargo'] = le.fit_transform(data['Cargo'])
        data['Estado civil'] = le.fit_transform(data['Estado civil'])
        data['Necessita de hora extra'] = le.fit_transform(data['Necessita de hora extra'])
        data['Contratar'] = le.fit_transform(data['Contratar'])
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data

