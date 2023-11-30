import unittest
from Posicao import Posicao
from Esparsa import Esparsa
import time
class TestTranspose(unittest.TestCase):
    def test_0(self):
        print("CRAZY __H.A.M.B.U.R.G.U.E.R__: STRESS TEST!!!----------")

        m = Esparsa()
        val = []
        pos = []
        i = 0
        for n in range(10):
            pos += [(i, 1), (i, 3), (i, 4), (i, 5), (i, 7), (i + 1, 2),
                    (i + 1, 3),
                    (i + 1, 8), (i + 2, 2), (i + 2, 4)]
            i += 3
        for i in range(len(pos)):
            val += [i]

        for i in range(len(pos)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])

        start = time.time()
        c = m.compress()
        end = time.time()
        time1 = end - start
        print("time 1: " + str(end - start))

        m = Esparsa()
        val = []
        pos = []
        i = 0
        for n in range(100):
            pos += [(i, 1), (i, 3), (i, 4), (i, 5), (i, 7), (i + 1, 2),
                    (i + 1, 3),
                    (i + 1, 8), (i + 2, 2), (i + 2, 4)]
            i += 3
        for i in range(len(pos)):
            val += [i]

        for i in range(len(pos)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])

        start = time.time()
        c = m.compress()
        end = time.time()
        time2 = end - start
        print("time 2: " + str(end - start))

        m = Esparsa()
        val = []
        pos = []
        i = 0
        for n in range(150):
            pos += [(i, 1), (i, 3), (i, 4), (i, 5), (i, 7), (i + 1, 2),
                    (i + 1, 3),
                    (i + 1, 8), (i + 2, 2), (i + 2, 4)]
            i += 3
        for i in range(len(pos)):
            val += [i]

        for i in range(len(pos)):
            m.posicao(Posicao(pos[i][0], pos[i][1]), val[i])

        start = time.time()
        c = m.compress()
        end = time.time()
        time3 = end - start
        print("time 3: " + str(end - start))

        print("Número de elementos: 100,  1.000, 1.500")
        print("coeficientes de tempo: \ntime2/time1 = " + str(
            time2 / time1) + "\ntime3/time1 = " + str(time3 / time1))

if __name__ == '__main__':
    from os import getenv
    if getenv('TAD'):
        exec(f"from {getenv('TAD')} import *")
    unittest.main()