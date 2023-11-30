"""Este programa tem como objetivo criar as posicoes que servirão para as
 seguintes classes.
"""

__author__ = "ist1103239@tecnico.ulisboa.pt"
__version__ = "0.1"
__all__ = ['Posicao']

class Posicao:
    def __init__(self,lin,col):
        self.__lin= lin
        self.__col = col
        if isinstance(self.__lin, int) is False \
        or isinstance(self.__col, int) is False \
        or self.__lin < 0 or self.__col < 0:
            raise ValueError('Posição: argumentos inválidos')
        else:
            self.__pos = (self.__lin,self.__col)
    def __repr__(self):
        "Este método serve para visualizarmos a posição."
        return f'{self.__pos}'
    def linha(self):
        "Este método serve para nos retornar a linha de uma posição."
        return self.__lin
    def coluna(self):
        "Este método serve para nos retornar a coluna de uma posição."
        return self.__col
    def __eq__(self, other):
        "Este método serve para verificar se duas posições são iguais ou não."
        return self.__pos == (other.linha(),other.coluna())