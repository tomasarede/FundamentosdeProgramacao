import unittest
from Posicao import Posicao
from Matriz import Matriz
from Esparsa import Esparsa
from random import randint

class TestTranspose(unittest.TestCase):
    print('-' * 50)
    print('\033[1;32mtestTranspose\033[m\nautor: ist1103239@tecnico.ulisboa.pt\n'
          'introdução: Este programa tem como objetivo\n           '
          ' testar o método transpose '
          'da classe \n            '
          'Esparsa do projeto 2.')
    print('-' * 50)
    print(' '*25 +'|\n'+' '*25 +'|\n'+' '*25 + '|\n'+ ' '*25+'|\n'+' '*25+'V')

    def test1(self): #ver se dá erro fazer a transposta de uma matriz vazia
        a = Esparsa()
        c = a.transpose()
        b = Esparsa()
        self.assertEqual(print(c),print(b))
        self.assertEqual(c.dimensao(),())
        self.assertAlmostEqual(c.densidade(),0.0)


    def test2(self): #ver se as diagonais mantém-se iguais em matriz quadrada
        a = Esparsa()
        for d in range(0,10):
            a.posicao(Posicao(d,d),d)
        b = a.transpose()
        self.assertEqual(b.diagonal(),a.diagonal())

    def test3(self): #transposta de uma matriz só com um elemento
        a = Esparsa()
        a.posicao(Posicao(1,1),1.1)
        val_b = [1.1]
        c = a.transpose()
        posicoes = [u for u in c]
        for d in range(len(val_b)):
            v = c.valor(posicoes[d])
            self.assertEqual(v,val_b[d])

    def test4(self): #linha de uma transposta
        k = 0
        while k!=10:
            a = Esparsa()
            b = Esparsa()
            num1 = randint(2,20)
            linha = 0
            for d in range(0,num1):
                if d == 1:
                    num2 = randint(0,20)
                    num3 = randint(0,20)
                    num4 = randint(0,20)
                    a.posicao(Posicao(num2,num3),num4)
                    b.posicao(Posicao(num3,num2),num4)
                    linha += num2
                else:
                    num2 = randint(0, 20)
                    num3 = randint(0, 20)
                    num4 = randint(0, 20)
                    a.posicao(Posicao(num2, num3), num4)
                    b.posicao(Posicao(num3, num2), num4)
            self.assertEqual(a.transpose().coluna(linha),b.coluna(linha))
            k += 1


    def test5(self): #coluna de uma transposta
        k = 0
        while k!=10:
            a = Esparsa()
            b = Esparsa()
            num1 = randint(2, 20)
            coluna = 0
            for d in range(0, num1):
                if d == 1:
                    num2 = randint(0, 20)
                    num3 = randint(0, 20)
                    num4 = randint(0, 20)
                    a.posicao(Posicao(num2, num3), num4)
                    b.posicao(Posicao(num3, num2), num4)
                    coluna += num3
                else:
                    num2 = randint(0, 20)
                    num3 = randint(0, 20)
                    num4 = randint(0, 20)
                    a.posicao(Posicao(num2, num3), num4)
                    b.posicao(Posicao(num3, num2), num4)
            self.assertEqual(a.transpose().linha(coluna), b.linha(coluna))
            k += 1

    def test6(self): #diagonal de uma transposta
        k = 0
        while k!= 10:
            a = Esparsa()
            a.posicao(Posicao(0,0),1)
            a.posicao(Posicao(20,20),1)
            b = Esparsa()
            b.posicao(Posicao(0,0),1)
            b.posicao(Posicao(20,20),1)
            num1 = randint(2, 20)
            for d in range(0, num1):
                num2 = randint(2, 19)
                num3 = randint(2, 19)
                num4 = randint(2, 19)
                a.posicao(Posicao(num2, num3), num4)
                b.posicao(Posicao(num2, num3), num4)
            self.assertEqual(a.transpose().diagonal(), b.diagonal())
            k += 1

    def test7(self): #testar transposta para valores negativos
        a = Esparsa()
        pos_a = ((1,2),(1,3),(2,4),(2,5),(3,1))
        val_a = (-1.2,1.3,-2.4,2.5,-3.1)
        val_b = (-3.1,-1.2,1.3,-2.4,2.5)
        for d in range(0,len(pos_a)):
            a.posicao(Posicao(pos_a[d][0],pos_a[d][1]),val_a[d])
        c = a.transpose()
        posicoes = [u for u in c]
        for d in range(len(val_b)):
            v = c.valor(posicoes[d])
            self.assertEqual(v,val_b[d])

    def test8(self): #transposta de uma copia
        a = Esparsa()
        pos_a = ((1, 2), (1, 3), (2, 4), (2, 5), (3, 1))
        val_a = (1.2, 1.3, 2.4, 2.5, 3.1)
        val_b = (3.1, 1.2, 1.3, 2.4, 2.5)
        for d in range(0, len(pos_a)):
            a.posicao(Posicao(pos_a[d][0], pos_a[d][1]), val_a[d])
        c = a.copia().transpose()
        posicoes = [u for u in c]
        for d in range(len(val_b)):
            v = c.valor(posicoes[d])
            self.assertEqual(v, val_b[d])


    def test9(self): #copia da transposta
        a = Esparsa()
        pos_a = ((1, 2), (1, 3), (2, 4), (2, 5), (3, 1))
        val_a = (1.2, 1.3, 2.4, 2.5, 3.1)
        val_b = (3.1, 1.2, 1.3, 2.4, 2.5)
        for d in range(0, len(pos_a)):
            a.posicao(Posicao(pos_a[d][0], pos_a[d][1]), val_a[d])
        c = a.transpose().copia()
        posicoes = [u for u in c]
        for d in range(len(val_b)):
            v = c.valor(posicoes[d])
            self.assertEqual(v, val_b[d])


    def test10(self): #ordem aleatoria das posicoes
        a = Esparsa()
        pos_a = ((2, 4), (2, 5), (1, 2), (1, 3), (3, 1))
        val_a = (-1.2, 1.3, -2.4, 2.5, -3.1)
        val_b = (-3.1, -2.4, 2.5, -1.2, 1.3)
        for d in range(0, len(pos_a)):
            a.posicao(Posicao(pos_a[d][0], pos_a[d][1]), val_a[d])
        c = a.transpose()
        posicoes = [u for u in c]
        for d in range(len(val_b)):
            v = c.valor(posicoes[d])
            self.assertEqual(v, val_b[d])

    def test11(self): #testar a propriedade (A^T)^T = A
        a = Esparsa()
        pos1 = ((1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (4, 1), (4, 3),(5, 1))
        val1 = (1.1, 1.2, 1.3, 2.1, 2.2, 4.1, 4.3, 5.1)
        for i in range(len(val1)):
            a.posicao(Posicao(pos1[i][0], pos1[i][1]), val1[i])
        c = a.transpose().transpose()
        posicoes = [u for u in c]
        for d in range(len(val1)):
            v = c.valor(posicoes[d])
            self.assertEqual(v,val1[d])
    def test12(self): #testar matrizes triangulares sup. e inf.
        a = Esparsa()
        b = Esparsa()
        posa = ((1,1),(2,2),(3,3),(1,2),(1,3),(2,3))
        posb = ((1,1),(2,2),(3,3),(3,1),(3,2),(2,1))
        vala = (1.1,2.2,3.3,1.2,1.3,2.3)
        valb = (1.1,2.2,3.3,3.1,3.2,2.1)

        for d in range(len(posa)):
            a.posicao(Posicao(posa[d][0],posa[d][1]),vala[d])
            b.posicao(Posicao(posb[d][0], posb[d][1]), valb[d])
        c = a.transpose()
        posc = [u for u in c]
        d = b.transpose()
        posd = [u for u in d]
        valc = (1.1,1.2,2.2,1.3,2.3,3.3)
        vald = (1.1,2.1,3.1,2.2,3.2,3.3)
        for l in range(len(valc)):
            v = c.valor(posc[l])
            w = d.valor(posd[l])
            self.assertEqual(v,valc[l])
            self.assertEqual(w,vald[l])
    def test13(self): #testar a transposta para uma matriz esparsa com elevada densidade
        a = Esparsa()
        pos = ((1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(3,4))
        val = (1.1,1.2,1.3,1.4,2.1,2.2,2.3,3.1,3.2,3.3,3.4)
        for d in range(len(pos)):
            a.posicao(Posicao(pos[d][0],pos[d][1]),val[d])
        c = a.transpose()
        posicoes = [u for u in c]
        valores = (1.1,2.1,3.1,1.2,2.2,3.2,1.3,2.3,3.3,1.4,3.4)
        for l in range(len(valores)):
            v = c.valor(posicoes[l])
            self.assertEqual(v,valores[l])

    def test14(self): #testar a transposta para uma matriz esparsa com densidade baixa
        a = Esparsa()
        pos = ((1, 1),(3,3))
        val = (1.1,3.3)
        for d in range(len(pos)):
            a.posicao(Posicao(pos[d][0], pos[d][1]), val[d])
        c = a.transpose()
        posicoes = [u for u in c]
        valores = (1.1,3.3)
        for l in range(len(valores)):
            v = c.valor(posicoes[l])
            self.assertEqual(v, valores[l])
    def test15(self): #testar a transposta para uma matriz simétrica
        a = Esparsa()
        pos = ((1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2,1), (2, 3), (3, 1), (3, 2))
        val = (1.1, 2.2, 3.3, 1.2, 1.3, 1.2, 2.3, 1.3, 2.3)
        for d in range(len(pos)):
            a.posicao(Posicao(pos[d][0], pos[d][1]), val[d])
        c = a.transpose()
        posicoes = [u for u in c]
        valores = (1.1, 1.2,1.3,1.2,2.2,2.3,1.3,2.3,3.3)
        for l in range(len(valores)):
            v = c.valor(posicoes[l])
            self.assertEqual(v, valores[l])

    def test16(self): #testar a transposta para várias matrizes esparsa aleatorias
        k = 0
        while k != 10:
            a = Esparsa()
            b = Esparsa()
            num1 = randint(2,20)
            for d in range(0,num1):
                num2 = randint(0,20)
                num3 = randint(0,20)
                num4 = randint(0,20)
                a.posicao(Posicao(num3,num2),num4)
                b.posicao(Posicao(num2,num3),num4)
            val_b = [b.valor(e) for e in b]
            c = a.transpose()
            posicoes = [u for u in c]
            for d in range(len(val_b)):
                v = c.valor(posicoes[d])
                self.assertEqual(v,val_b[d])
            k+=1


if __name__ == '__main__':
    unittest.main()