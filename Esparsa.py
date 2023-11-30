from Posicao import Posicao
from Matriz import Matriz

__author__ = "ist1103239@tecnico.ulisboa.pt"
__version__ = "0.1"
__all__ = ['Esparsa']


class Esparsa(Matriz):
    """Este programa tem como objetivo realizar operações com a matriz definida nas
    classes anteriores.
    """
    def __init__(self,num = 0.0):
        super().__init__(float(num))
    def __str__(self):
        """Este método pega numa matriz e devolve uma string que representará a
        matriz como estamos habituados a ver, com todos os valores entre a posi-
        ção mínima e máxima, sendo eles valores nulos ou nao."""
        _out = ""
        _dim = self.dimensao()
        if not _dim: return _out
        _minlin, _mincol = _dim[0].linha(), _dim[0].coluna()
        _maxlin, _maxcol = _dim[1].linha(), _dim[1].coluna()
        for lin in range(_minlin, _maxlin + 1):
            line = ""
            for col in range(_mincol, _maxcol + 1):
                pos = Posicao(lin, col)
                if line: line += " "
                if round(self.valor(pos)) - self.valor(pos) != 0.0:
                    line += str(self.valor(pos))
                else:
                    line += str(int(self.valor(pos)))
            _out += line + "\n"
        return _out[:-1]
    def linha(self,n_linha):
        """Este método devole um tuplo com a linha da matriz, dada como argu-
        mento. Este argumento deverá ser um inteiro. Se a linha dada como argu-
        mento nao estiver na dimensão da matriz, é devolvido um tuplo vazio.
        """
        _dim = self.dimensao()
        _out = ()
        if not _dim: return _out
        _minlin, _mincol = _dim[0].linha(), _dim[0].coluna()
        _maxlin, _maxcol = _dim[1].linha(), _dim[1].coluna()
        for col in range(_minlin, _maxcol + 1):
            pos = Posicao(n_linha, col)
            _out += self.valor(pos),
        return _out
    def coluna(self,n_coluna):
        """Este método devole um tuplo com a coluna da matriz, dada como argu-
        mento. Este argumento deverá ser um inteiro. Se a coluna dada como argu-
        mento nao estiver na dimensão da matriz, é devolvido um tuplo vazio.
        """
        _dim = Matriz.dimensao(self)
        _out = ()
        if not _dim: return _out
        _minlin, _mincol = _dim[0].linha(), _dim[0].coluna()
        _maxlin, _maxcol = _dim[1].linha(), _dim[1].coluna()
        for lin in range(_minlin, _maxlin + 1):
            pos = Posicao(lin, n_coluna)
            _out += self.valor(pos),
        return _out
    def diagonal(self):
        """Este método devolve um tuplo que corresponde à diagonal de uma matriz
        quadrada. Se a matriz não for quadrada é levantado um erro.
        """
        _dim = self.dimensao()
        _out = ()
        if not _dim: return _out
        _minlin, _mincol = _dim[0].linha(), _dim[0].coluna()
        _maxlin, _maxcol = _dim[1].linha(), _dim[1].coluna()
        if _maxlin - _minlin != _maxcol - _mincol:  
            raise ValueError('matriz_diagonal: matriz não quadrada')
        col = _mincol
        for lin in range(_minlin, _maxlin + 1):
            pos = Posicao(lin, col)
            _out += self.valor(pos),
            col += 1
        return _out

    @classmethod
    def eye(cls,dim,valor_unit = 1.0,nulo = 0.0):
        """Este classmethod recebe 4 argumentos e tem como objetivo devolver a
        identidade de uma matriz. A classe, a dim (que deverá ser um tuplo com 2
        tuplos dentro dele, o primeiro indicando a dimensão mínima e o segundo
        indicando a dimensão máxima), o valor_unit (que deverá ser um float. Por
        omissão será considerado 1.0) e o valor_nulo (que deverá ser também um
        float. Por omissão será considerado 0.0).
        """
        if isinstance(dim,int) and isinstance(valor_unit,(int,float)) and\
           isinstance(nulo,(int,float)):
            m = Esparsa(float(nulo))
            for d in range(1,dim+1):
                m.posicao(Posicao(d,d),float(valor_unit))
            return m
        raise ValueError('Argumentos inválidos.')

    def __iter__(self):
        """ Este método tem como objetivo permitir iterar sobre a um objeto da
        classe. Assim, retorna self e na variável self.__posicoes guarda as
        posicoes não nulas da matriz.
        """
        _min_lin, _max_lin = self.dimensao()[0].linha(), \
                           self.dimensao()[1].linha()
        _min_col, _max_col = self.dimensao()[0].coluna(), \
                           self.dimensao()[1].coluna()
        self.__posicoes = []
        for d in range(_min_lin, _max_lin + 1):
            self.__posicoes += [Posicao(d, k) for k in range(_min_col, _max_col + 1) \
                                if self.valor(Posicao(d, k)) != self.zero()]
        self.__start = -1
        return self

    def __next__(self):
        """Este método percorre a lista self.__posicoes indicada no metodo next.
        Retorna uma lista com as posições. Quando a lista chegar ao fim é levan-
        tado um StopIteration que acabará com o loop.
        """
        self.__start += 1
        if self.__start<len(self.__posicoes):
            return self.__posicoes[self.__start]
        raise StopIteration

    def transpose(self):
        """Este método tem como objetivo realizar a propriedade algébrica da
        transposta. Assim recebe uma matriz e devolve a transposta dela.
        """
        if self.dimensao() != ():
            k = Esparsa(self.zero())
            for d in self:
                k.posicao(Posicao(d.coluna(),d.linha()),self.valor(d))
            return k
        return Esparsa(self.zero())

    def __add__(self, other):
        """Este método tem como argumento other (float) e soma a cada valor va-
        lor de cada posicao esse float. É retornada a matriz, proveniente desta
        soma.
        """
        if isinstance(other,(int,float)):
            other = float(other)
            if self.dimensao() == (): return Esparsa(self.zero())
            m = Esparsa(self.zero())
            for d in self:
                m.posicao(d,Matriz.valor(self,Posicao(d.linha(),d.coluna())) + other)
            return m
        raise ValueError('Argumentos inválidos.')

    def __mul__(self, other):
        """ Este método recebe o argumento other (matriz) e permite realizar a
        multiplicação entre 2 matrizes. Se uma das matrizes for vazia e a _outra
        não devolve um erro. Se ambas as matrizes forem vazias devolve uma ma-
        triz vazia. Caso contrário realiza a multiplicação se o número de colu-
        nas da primeira for igual ao número de linhas da segunda. Se não for, é
        originado um erro. Por fim, é retornada uma matriz com a multiplicação
        já feita.
        """
        def mat_lista(self):
            """ Este método é um método auxiliar do método __mul__. Tem como objeti-
            vo pegar numa matriz esparsa e retornar essa matriz em forma de lista,
            isto é, onde todas as posições serão representadas, incluindo as nulas.
            """
            _dim = self.dimensao()
            posicoes = [u for u in self]
            lista = [[self.zero() for k in
                      range(_dim[0].coluna(), _dim[1].coluna() + 1)] \
                     for u in range(_dim[0].linha(), _dim[1].linha() + 1)]
            for d in posicoes:
                lista[d.linha() - _dim[0].linha()][
                    d.coluna() - _dim[0].coluna()] = self.valor(d)
            return lista

        def analisa_lista(lista):
            """ Este método é _outro método auxiliar do __mul__. Tem objetivo contrá-
            rio do método mat_lista. Assim, este método pega numa lista (list) e é
            retornado uma matriz esparsa de novo.
            """
            m = Esparsa(self.zero())
            _dim = self.dimensao()
            for l in range(len(lista)):
                for k in range(len(lista[0])):
                    if lista[l][k] != self.zero():
                        m.posicao(
                            Posicao(l + _dim[0].linha(), k + _dim[0].coluna()),
                            lista[l][k])
            return m

        if type(other) != Esparsa: raise ValueError('Argumentos inválidos')
        else:
            if self.dimensao() == () and other.dimensao() == (): return Esparsa(self.zero())
            if self.dimensao() != () and other.dimensao() != ():
                _dim_m, _dim_o = self.dimensao(), other.dimensao()
                list_m,list_o = mat_lista(self), mat_lista(other)
                if _dim_m[1].coluna()-_dim_m[0].coluna() == _dim_o[1].linha() -_dim_o[0].linha()\
                    and self.zero() == other.zero():
                    result = [[sum(a * b for a, b in zip(la, cb)) for cb in zip(*list_o)]
                               for la in list_m]
                    final = analisa_lista(result)
                    return final
                raise ValueError('matrizes incompatíveis')
            raise ValueError('matrizes incompatíveis')

    def compress(self):
        """ Este método comprime uma matriz esparsa num conjunto de vetores. É
        devolvido um tuplo com três tuplos: um tuplo de valores, um tuplo de ín-
        dices e um tuplo de deslocamentos. Se a densidade da matriz for superior
        a 0.5 é gerado uma exceção ValueError com a mensagem matriz densa.
        """
        def todas_posicoes():
            """ Este método é uma função auxiliar do método compress e serve sim-
            plesmente para evitar chamar tantas vezes o método valor da classe Ma-
            triz no método compress. Recebe uma matriz esparsa e retorna todas as
            suas posições entre a dimensão mínima e a dimensão máxima. Retorna um
            dicionário com essas posições e com os valores que a cada uma correspon-
            de. Assim, às posições nulas atribuirá o valor do valor nulo e às outras
            posições o seu valor normal. Desta forma, o objetivo deste método é no
            fundo diminuir o tempo de execução do programa.
            """
            _min_col, _max_col = self.dimensao()[0].coluna(), self.dimensao()[
                1].coluna()
            _min_lin, _max_lin = self.dimensao()[0].linha(), self.dimensao()[
                1].linha()
            dic = {}
            for d in range(_min_lin, _max_lin + 1):
                for l in range(_min_col, _max_col + 1):
                    dic[(d, l)] = self.valor(Posicao(d, l))
            return dic

        def mais_densa(self):
            """ Este método é um método auxiliar do método compress. Tem como obje-
            tivo ver qual a linha mais densa de uma matriz esparsa. É retornado um
            um inteiro que corresponde à linha mais densa.
            """
            linhas = [d.linha() for d in self]
            linhas_final = list(set(linhas))
            conta = [linhas.count(l) for l in linhas_final]
            return linhas_final[conta.index(max(conta))]

        def decrescente():
            """ Este método é um método auxiliar do método compress. Tem como obje-
            tivo ordenar por ordem decrescente a densidade de linhas de uma matriz
            esparsa. É devolvido uma lista com as linhas ordenadas por ordem decres-
            cente.
            """
            lin, mat_cop, dens_decr = list(
                                set(d.linha() for d in self)), self.copia(), []
            for d in range(len(lin)):
                linha_densa = mais_densa(mat_cop)
                dens_decr.append(linha_densa)
                for l in mat_cop:
                    if l.linha() == linha_densa:
                        mat_cop.posicao(l, self.zero())
            return dens_decr

        def conf_pos(lista, lin):
            """ Este método é _outro método auxiliar do método compress. Tem como
            objetivo calcular qual o deslocamento percorrido. Tem como argumentos a
            lista (list), onde se irá analisar os valores (uma lista do género da
            lista value do método compress) e o argumento lin(int), que corresponde
            à linha que nós vamos querer ver o deslocamento. No final é devolvido um
            inteiro que corresponde ao deslocamento percorrido.
            """
            def conf_pos_aux(lin):
                """Este método é um método auxiliar do método conf_pos e tem como obje-
                tivo devolver uma lista com os indexs que as posicoes da linha (int) da-
                da como argumento deveriam ocupar na lista. Assim, é retornado uma lis-
                ta com esses indexs.
                """
                _min_col, _max_col = self.dimensao()[0].coluna(), \
                                     self.dimensao()[1].coluna()
                pos = [u for u in self if u.linha() == lin]
                col_index = [l.coluna() - _min_col for l in pos]
                return col_index

            col_index = conf_pos_aux(lin)
            zero = self.zero()
            k = 0
            while len(lista) > k:
                l = k
                for d in col_index:
                    if d + k < len(lista) and lista[d + k] != zero: k += 1
                if l == k: break
            return k

        if self.densidade() > 0.5: raise ValueError('matriz densa')
        if self.densidade() == 0.0: return (),(),()
        _min_col, _max_col = self.dimensao()[0].coluna(),self.dimensao()[1].coluna()
        _min_lin, _max_lin = self.dimensao()[0].linha(),self.dimensao()[1].linha()
        linhas = list(u for u in range(_min_lin,_max_lin+1))
        zero = self.zero()
        value,index,offset = [],[],[0 for u in range(len(linhas))]
        dens_decr,dic = decrescente(),todas_posicoes()
        for p in range(0,len(dens_decr)):
            posi = [(dens_decr[p],u) for u in range(_min_col,_max_col+1)]
            k = conf_pos(value,dens_decr[p])
            offset[linhas.index(dens_decr[p])] = k
            for d in range(0,len(posi)):
                if d+k < len(value):
                    if value[d+k] == zero:
                        value[d + k] = dic[posi[d]]
                        if dic[posi[d]] != zero:
                            index[d+k] = dens_decr[p]
                else:
                    for l in posi[d:]:
                        value.append(dic[l])
                        if dic[l] == zero: index.append(-1)
                        else: index.append(dens_decr[p])
        return tuple(value),tuple(index),tuple(offset)


    @staticmethod
    def doi(zero,pos,tuplo,linha,coluna):
        """Este staticmethod recebe zero(float), pos(tuplo) , tuplo(tuplo com
        tuplos lá dentro (originado pelo compress)), linha(int) e coluna(int).
        Retorna o valor da matriz na posição i (linha) e j (coluna) indicados
        respetivamente nos dois últimos argumentos.
        """
        value,index,offset = tuplo[0],tuplo[1],tuplo[2]
        _min_lin,_min_col = pos.linha(),pos.coluna()
        try: desl = offset[linha-_min_lin]
        except IndexError: return zero
        if len(index) > desl + coluna - _min_col:
            if linha not in index or coluna < _min_col:return zero
            return value[coluna-_min_col+desl] if index[coluna-_min_col+\
                                                  desl] == linha else zero
        return zero