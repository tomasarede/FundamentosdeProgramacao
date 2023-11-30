"""Este programa tem como objetivo preparar a matriz que servirá para a próxima
classe.
"""
from Posicao import Posicao

__author__ = "ist1103239@tecnico.ulisboa.pt"
__version__ = "0.1"
__all__ = ['Matriz']

class Matriz:
    def __init__(self,num = 0.0):
        self.__valor_nulo = float(num)
        self.__matt = {}
    def zero(self):
        """Este método retorna o valor nulo."""
        return self.__valor_nulo
    def copia(self):
        """Esta função retorna uma cópia de uma matriz."""
        copia = type(self)(self.__valor_nulo)
        copia.__matt = self.__matt.copy()
        return copia
    def posicao(self,pos,val):
        """Este método vai à matriz e coloca na posição da como argumento e atri-
        bui-lhe o valor dado também como argumento, se esse valor for diferente
        do valor nulo, e devolve o valor nulo. Se a posição dada já existir na
        matriz simplesmente, substitui esse valor pelo novo e devolve o valor
        antigo."""

        _tuplo_pos = (pos.linha(),pos.coluna())

        if _tuplo_pos in self.__matt:
            old = self.__matt[_tuplo_pos]
            if float(val) == self.zero():
                del self.__matt[_tuplo_pos]
            else:
                self.__matt[_tuplo_pos] = val
            return old
        else:
            if val == self.zero(): return self.zero()
            self.__matt[_tuplo_pos] = val
            return self.zero()

    def valor(self,pos):
        """Este método retorna o valor a que corresponde a posição dada como
        argumento."""
        _tuplo_pos = (pos.linha(), pos.coluna())
        return self.__matt[_tuplo_pos] if _tuplo_pos in self.__matt else self.zero()
    def dimensao(self):
        """Este método devolve um tuplo com a posição mínima e a posição máxima
         da matriz. Se a matriz for vazia retorna apenas um tuplo vazio."""

        if self.__matt == {}:
            return ()
        _minlin = _mincol = _maxlin = _maxcol = None
        for pos in self.__matt:
            lin = pos[0]
            col = pos[1]
            if _minlin == None:
                _minlin = _maxlin = lin
                _mincol = _maxcol = col
            else:
                if _minlin > lin: _minlin = lin
                if _mincol > col: _mincol = col
                if _maxlin < lin: _maxlin = lin
                if _maxcol < col: _maxcol = col
        return (Posicao(_minlin, _mincol),Posicao(_maxlin, _maxcol))
    def densidade(self):
        """Este método devolve a densidade da matriz, isto é, o númeo racional
        (float) proveniente da razão entre os valores não nulos da matriz e a
        dimensão total da matriz."""
        dim = self.dimensao()
        if not dim: return 0.0
        _minlin, _mincol = dim[0].linha(),dim[0].coluna()
        _maxlin, _maxcol = dim[1].linha(),dim[1].coluna()
        nelems = (_maxlin - _minlin + 1) * (_maxcol - _mincol + 1)
        return len(self.__matt) / nelems
    def nulo(self,val):
        """Este método substitui o valor nulo da matriz pelo valor dado no argu-
        mento, e se houver valores na matriz iguais ao novo valor nulo, esses são
        "apagados"."""
        dic = {}
        for pos in self.__matt:
            if self.__matt[pos] != float(val):
                dic[pos] = self.__matt[pos]
        self.__valor_nulo = float(val)
        self.__matt = dic