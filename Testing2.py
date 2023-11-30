import unittest
from Posicao import Posicao
from Esparsa import Esparsa

class TestTranspose(unittest.TestCase):
    print("TESTES H.A.M.B.U.R.G.U.E.R------")
    def test_0(self):
        m = Esparsa()
        pos = ((5, 5), (5, 6), (6, 7), (7, 4),(7,5),(7,8))
        val = (5.5,5.6,6.7,7.4,7.5,7.8)
        for i in range(len(val)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])
        c = m.compress()
        print("")
        print(m)
        print("")
        print(c)
        self.assertEqual(c, ((7.4, 7.5, 5.5, 5.6, 7.8, 6.7, 0),
                            (7, 7, 5, 5, 7, 6, -1), (1, 2, 0)), "matriz stor")
    def test_1(self):
        m = Esparsa(1)
        pos = ((5, 5), (5, 6), (6, 7), (7, 4),(7,5),(7,8))
        val = (5.5,5.6,6.7,7.4,7.5,7.8)
        for i in range(len(val)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])
        c = m.compress()
        print("")
        print(m)
        print("")
        print(c)
        self.assertEqual(c, ((7.4, 7.5, 5.5, 5.6, 7.8, 6.7, 1),
                            (7, 7, 5, 5, 7, 6, -1), (1, 2, 0)), "matriz stor "
                                                                "zero 1")

    def test_2(self):
        m = Esparsa()
        pos = ((1, 1), (2, 2), (3, 3), (4, 4))
        val = (1, 2, 3, 4)
        for i in range(len(val)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])
        c = m.compress()
        print("")
        print(m)
        print("")
        print(c)
        self.assertEqual(c, ((1,2,3,4),(1,2,3,4),(0,0,0,0)), "matriz diagonal")

    def test_3(self):
        m = Esparsa()
        pos = ((1, 1), (3, 2), (4, 3), (5, 4))
        val = (1, 2, 3, 4)
        for i in range(len(val)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])
        c = m.compress()
        print("")
        print(m)
        print("")
        print(c)
        self.assertEqual(c, ((1, 2, 3, 4), (1, 3, 4, 5), (0, 0, 0, 0, 0)),
                         "matriz diagonal com uma linha de zeros")
    def test_4(self):
        m = Esparsa()
        pos = ((0, 0), (3, 2), (3, 3), (4, 3), (4, 4), (5, 4))
        val = (1, 2, 3, 4, 5, 6)
        for i in range(len(val)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])
        c = m.compress()
        print("")
        print(m)
        print("")
        print(c)
        self.assertEqual(c, ((1, 0, 2, 3, 4, 5, 6), (0, -1, 3, 3, 4, 4, 5),
                    (0, 0, 0, 0, 1, 2)), "matriz 2x linhas de zeros e overlaps")

    def test_5(self):
        m = Esparsa()
        pos = ((1, 1), (1, 2), (1, 4), (2, 2), (2, 4), (3, 2), (4, 1), (4, 4))
        val = (1, 2, 3, 4, 5, 6, 7, 8)
        for i in range(len(val)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])
        c = m.compress()
        print("")
        print(m)
        print("")
        print(c)
        self.assertEqual(c,((1, 2, 4, 3, 5, 7, 6, 0, 8),
                            (1, 1, 2, 1, 2, 4, 3, -1, 4),
                            (0, 1, 5, 5)), "matriz dificil1")
    def test_6(self):
        m = Esparsa()
        pos = ((1, 1), (1, 2), (1, 4), (2, 2), (2, 4), (3, 1), (4, 1), (4, 4))
        val = (1, 2, 3, 4, 5, 6, 7, 8)
        for i in range(len(val)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])
        c = m.compress()
        print("")
        print(m)
        print("")
        print(c)
        self.assertEqual(c, ((1, 2, 4, 3, 5, 7, 6, 0, 8, 0),
                             (1, 1, 2, 1, 2, 4, 3, -1, 4, -1),
                             (0, 1, 6, 5)), "matriz dificil1.2")
    def test_7(self):
        m = Esparsa()
        pos = ((5, 5), (5, 6), (6, 7), (7, 4), (7, 5), (7, 8))
        val = (5.5, 5.6, 6.7, 7.4, 7.5, 7.8)
        for i in range(len(val)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])
        c = m.compress()
        print("")
        print(m)
        print("")
        print(c)
        print(Esparsa.doi(0, m.dimensao()[0], c, 7, 11))
        print(Esparsa.doi(0, m.dimensao()[0], c, 7, 12))
        print(Esparsa.doi(0, m.dimensao()[0], c, 7, 13))
        print(Esparsa.doi(0, m.dimensao()[0], c, 7, 14))
        self.assertEqual(Esparsa.doi(0, m.dimensao()[0], c, 7, 11), 0)
        self.assertEqual(Esparsa.doi(0, m.dimensao()[0], c, 7, 12), 0)
        self.assertEqual(Esparsa.doi(0, m.dimensao()[0], c, 7, 13), 0)
        self.assertEqual(Esparsa.doi(0, m.dimensao()[0], c, 7, 14), 0)
    if __name__ == '__main__':
        unittest.main()