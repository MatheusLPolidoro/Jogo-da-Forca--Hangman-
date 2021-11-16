import sqlite3
from sqlite3 import Error
import os

pasta_app = os.path.dirname(__file__) + '\\banco\\'

class Db:

    def __init__(self, nome_banco):
        self.caminho = pasta_app + nome_banco + ".db"
        self.conexao = None
        try:
            self.conexao = sqlite3.connect(self.caminho)
            self.cursor = self.conexao.cursor()
        except Error as ex:
            print(ex)
        return

    def executar(self, sql):
        try:
            self.cursor.execute(sql)
            self.conexao.commit()
        except Error as ex:
            print(ex)
    
    def consultar(self, sql):
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        return resultado

    # ATENÇÃO esse metodo deleta o banco.
    def close(self):
        if os.path.isfile(self.caminho):
            os.remove(self.caminho)