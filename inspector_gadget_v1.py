#!/bin/python3
from Esparsa import Esparsa
from Matriz import Matriz
from Posicao import Posicao

import cProfile
__all__ = ["test_eye()", "test_thin()"]

def test_eye():
	m = Esparsa.eye(100)
	m.compress()

def test_thin():
	m = Esparsa()
	m.posicao(Posicao(0, 2), -1)
	for i in range(100):
		m.posicao(Posicao(i, 0), i)
	m.compress()

for func in __all__:
	print("Running " + func + ":")
	cProfile.run(func, sort = 1)
	print("-" * 69 + "\n")

print("🎵 Go Gadget, go! 🎶")