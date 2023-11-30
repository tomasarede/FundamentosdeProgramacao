from esparsa_proj1 import *
from Esparsa import *
from Posicao import *
from Matriz import *


def conta_colunas(mat,num):
    if not eh_matriz(mat) or not isinstance(num,(int,float)):
        raise ValueError('Argumentos inválidos.')
    min_col = matriz_dimensao(mat)[0][1]
    min_lin = matriz_dimensao(mat)[0][0]
    max_lin = matriz_dimensao(mat)[1][0]
    k = 0
    for l in range(min_col, num):
        for d in range(min_lin,max_lin+1):
            if cria_posicao(d,l) in mat[0]:
                k += 1

    return k
class TP(Esparsa):
    def __init__(self,num = 0.0):
        super().__init__(float(num))
    def __itruediv__(self, other):
        if not isinstance(self,TP) or not isinstance(other,(Esparsa,TP)):
            raise ValueError('Argumentos inválidos.')
        dim_s = self.dimensao()
        dim_o = other.dimensao()
        if self.dimensao() == () and other.dimensao() == ():
            return Esparsa(self.zero())
        if dim_s != dim_o:
            raise ValueError('Operandos incompatíveis.')
        m = Esparsa()
        pos_s = [u for u in self]
        pos_o = [d for d in other]
        for l in pos_s:
            if l in pos_o:
                m.posicao(l,self.valor(l)/other.valor(l))
            else: m.posicao(l,self.valor(l))

        return m

mat = cria_matriz()
matriz_posicao(mat,(1,1),2.0)
matriz_posicao(mat,(1,2),2.0)
matriz_posicao(mat,(2,1),2.0)
matriz_posicao(mat,(2,2),2.0)
matriz_posicao(mat,(3,3),2.0)
print(mat)
print(conta_colunas(mat,3))


a = TP()
b = Esparsa()
pos_a = ((1, 2), (1, 3), (2, 4), (2, 5), (3, 1))
val_a = (1.2, 1.3, 2.4, 2.5, 3.1)
pos_b = ((1,1),(1,2),(3,5))
valb = (1.1,1.2,3.5)
for d in range(0, len(pos_a)):
    a.posicao(Posicao(pos_a[d][0], pos_a[d][1]), val_a[d])
b.posicao(Posicao(1,1),1.1)
b.posicao(Posicao(1,2),1.2)
b.posicao(Posicao(3,5),3.5)
print(b)
print(a)
a /= b
print('-' * 30)
print(a)