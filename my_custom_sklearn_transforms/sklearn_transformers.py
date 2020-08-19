import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.base import BaseEstimator, TransformerMixin

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

class ConverterColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        data["INGLES"] = pd.to_numeric(data["INGLES"])
        data["FALTAS"] = pd.to_numeric(df_data_3["FALTAS"])
        data["REPROVACOES_DE"] = pd.to_numeric(data["REPROVACOES_DE"])
        data["REPROVACOES_EM"] = pd.to_numeric(data["REPROVACOES_EM"])
        data["REPROVACOES_MF"] = pd.to_numeric(data["REPROVACOES_MF"])
        data["REPROVACOES_GO"] = pd.to_numeric(data["REPROVACOES_GO"])
        data["TAREFAS_ONLINE"] = pd.to_numeric(data["TAREFAS_ONLINE"])
        data["H_AULA_PRES"] = pd.to_numeric(data["H_AULA_PRES"])
        data["NOTA_DE"] = pd.to_numeric(data["NOTA_DE"], downcast="float")
        data["NOTA_EM"] = pd.to_numeric(data["NOTA_EM"], downcast="float")
        data["NOTA_MF"] = pd.to_numeric(data["NOTA_MF"], downcast="float")
        data["NOTA_GO"] = pd.to_numeric(data["NOTA_GO"], downcast="float")
        return data;


class SetIndex(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.set_index(self.columns, inplace=True)
