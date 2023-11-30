"""Este programa tem como objetivo realizar uma matriz esparsa (definição de
matriz esparasa https://pt.wikipedia.org/wiki/Matriz_esparsa), sendo assim uma
ferramenta de trabalho para várias áreas do conhecimento."""

__author__ = "ist1103239@tecnico.ulisboa.pt"
__version__ = "0.1"
__all__ = ['cria_posicao', 'eh_posicao', 'posicao_linha',
       'posicao_coluna', 'posicao_igual', 'posicao_str',
       'cria_matriz', 'eh_matriz', 'matriz_zero', 'matriz_copia',
       'matriz_posicao', 'matriz_valor', 'matriz_dimensao',
       'matriz_densidade', 'matriz_nulo', 'matriz_str', 'matriz_linha',
       'matriz_coluna', 'matriz_diagonal']

# funcoes auxiliares -----------------------------------------------------------

def funcao_geral(mat):
    """Definir algumas características para variáveis de outras funções.
       mat : list donde vão ser extraido as características.
       retorno: tuple(tuplo_das_posicoes, tuplo_dos_valores, maior_posicao) e
                list(linhas, colunas, matriz_final)
                características do mat necessárias para outras funções.
    """
    if len(mat[0]) ==0:
        return (),(),(),(),[],(),()
    tuplo_das_posicoes = tuple(key for key in mat[0].keys())
    # adicionar as posicoes
    tuplo_dos_valores = tuple(matriz_valor(mat,tuplo_das_posicoes[i]) \
                              for i in range(0, len(tuplo_das_posicoes)))

    # adicionar os valores
    linhas = [posicao_linha(tuplo_das_posicoes[pos]) for pos in \
              range(0, len(tuplo_das_posicoes))]
    colunas = [posicao_coluna(tuplo_das_posicoes[pos]) for pos in \
               range(0, len(tuplo_das_posicoes))]

    linhas.sort()
    colunas.sort()
    # ordenar de forma crescente ambas as listas
    maior_posicao = (linhas[-1],colunas[-1])
    # elemento mais em baixo e a direita
    menor_posicao = (linhas[0],colunas[0])

    matriz_final = [[] for cada_linha in range(0, maior_posicao[0])]
    # criar as linhas
    for cada_linha in range(0, len(matriz_final)):
        matriz_final[cada_linha] = [matriz_zero(mat) for cada_coluna\
                                    in range(0, maior_posicao[1])]

    for zeros in range(0, len(tuplo_das_posicoes)):
        # substituir os zeros por valores
        linh = tuplo_das_posicoes[zeros][0]
        col = tuplo_das_posicoes[zeros][1]
        matriz_final[linh - 1][col - 1] = float(tuplo_dos_valores[zeros])

    return tuplo_das_posicoes,tuplo_dos_valores, linhas, colunas, matriz_final,\
            maior_posicao, menor_posicao

def verifica_linhas_e_colunas(mat):
    """Definir a matriz mas apenas entre a dimensão mínima e a máxima.
       mat : list (daqui vai se verificar se há colunas e linhas desnessárias
             para algumas funções).
       retorno : list- matriz_final definida em função_geral só que apenas entre
                 a dimensão mínima e a dimensão máxima.
    """
    if len(mat[0]) == 0:
        return []
    maior_pos = funcao_geral(mat)[5]
    menor_pos = funcao_geral(mat)[6]
    matriz_final = funcao_geral(mat)[4]
    matriz_final1 = []
    for linhas in range(menor_pos[0] - 1, maior_pos[0]):
        matriz_final1.append([])
    c = 0
    #este c irá percorrer as linhas
    for linhas in range(menor_pos[0] - 1, maior_pos[0]):
        for colunas in range(menor_pos[1] - 1, maior_pos[1]):
            matriz_final1[c].append(matriz_final[linhas][colunas])
        c += 1
    return matriz_final1


# 2.1.1 ------------------------------------------------------------------------

def cria_posicao(linha, coluna):
    """Criar uma posição para o programa se respeitar as condições definidas.
       linha: int(corresponde à linha que se pretender criar a posição)
       coluna:int(corresponde à coluna que se pretende criar posição)
       retorno: tuple(linha,coluna)
    """

    if isinstance(linha, int) is False \
            or isinstance(coluna, int) is False or linha < 0 or coluna < 0:
        raise ValueError('\033[1;32mcria_posição: argumentos inválidos\033[m')

    return (linha, coluna)


# 2.1.2 ------------------------------------------------------------------------

def eh_posicao(pos):
    """Avalia se o argumento dado pode gerar uma posição ou não.
       arg1(pos): tuple e aqui deve ser colocado o que nós queremos verificar se
                  pode ser considerado função
       retorno: bool(True se pode ser considerado uma posição. False caso
                contrário)
    """
    if isinstance(pos, tuple) is True and len(pos) == 2:
        # tem que cumprir estes requisitos
        for elemento in range(0,2):
            if isinstance(pos[elemento], int) is False or pos[elemento]<0:
                return False
        return True
    return False



# 2.1.3 ------------------------------------------------------------------------

def posicao_linha(pos):
    """Esta função recebe uma posição e devolve a sua linha.
       pos: tuple
       retorno: int(a linha do tuplo(elemento de index 0))
    """
    if eh_posicao(pos) is True:
        return pos[0]
    return None


# 2.1.4 ------------------------------------------------------------------------

def posicao_coluna(pos):
    """Esta função recebe uma posição e devolve a sua coluna.
       pos: tuple
       retorno: int(a coluna do tuplo (elemento de index 1))
    """
    if eh_posicao(pos) is True:
        return pos[1]
    return None


# 2.1.5 ------------------------------------------------------------------------

def posicao_igual(pos1, pos2):
    """Esta função avalia se duas posicções são iguais ou não.
       pos1: tuple(uma das posições que vai ser comparada)
       pos2: tuple(outra das posições que vai ser comparada)
       retorno: bool(True se forem iguais. False caso contrario)
    """
    if eh_posicao(pos1) is True and eh_posicao(pos2) is True:
        return pos1 == pos2
    return False


# 2.1.6 ------------------------------------------------------------------------

def posicao_str(pos):
    """Esta função serve para vizualizarmos o tuplo da posição pretendida.
       pos: tuple
       retorno: str(posição dada como argumento)
    """

    if eh_posicao(pos) is True:
        return f'{pos}'
    return None


# 2.2.1 ------------------------------------------------------------------------

def cria_matriz(*num):
    """Esta função serve para criar uma matriz vazia.
       num: int => tuple (numero que queremos atribuir ao valor nulo da matriz)
       retorno: list deste aspeto [dict,valor_nulo]
    """
    valor_nulo = float(0)
    if num != ():
        valor_nulo = float(num[0])
    return [{}, valor_nulo]  # matriz vazia com valor nulo float(0)


# 2.2.2 ------------------------------------------------------------------------

def eh_matriz(mat):
    """Serve para verificar se o argumento pode ser considerado uma matriz
       mat: list - deve ser aqui colocada a matriz que queremos verificar
       retorno: bool(True se é considerada uma matriz. False caso contrário.)
    """
    if isinstance(mat, list) is False:
        return False
    if len(mat) != 2 or isinstance(mat[0], dict) is False \
            or isinstance(mat[1],float) is False:
        return False

    posicoes = funcao_geral(mat)[0]
    valores = funcao_geral(mat)[1]
    if len(posicoes) != 0:
        for l in range(len(posicoes)):
            if eh_posicao(posicoes[l]) is False or\
            isinstance(valores[l],float) is False or matriz_zero(mat) in valores:
                return False
        return True
    return True


# 2.2.3 ------------------------------------------------------------------------

def matriz_zero(mat):
    """Serve para verificarmos qual o valor nulo da matriz a considerar.
       mat: list - deve-se colocar aqui a matriz a considerar.
       retorno: float - valor nulo
    """
    return mat[1]



# 2.2.4 ------------------------------------------------------------------------

def matriz_copia(mat):
    """Esta função serve para copiarmos a matriz dada como argumento.
       mat: list - deve-se colocar aqui a matriz a considerar.
       retorno: dict - copia do argumento dado.
    """
    if eh_matriz(mat) is True:
        return mat


# 2.3.1 ------------------------------------------------------------------------

def matriz_posicao(mat, pos, num):
    """Serve para na matriz pretendida atribuir a uma posição um valor.
       mat: list - deve-se colocar aqui a matriz a considerar.
       pos: tuple - posição
       retorno: float - valor ou valor nulo
    """

    num = float(num)

    if pos not in mat[0]:  # se y nao estiver no dic de x (matriz)
        if num == matriz_zero(mat):
            return matriz_zero(mat)
        mat[0][pos] = num
        return matriz_zero(mat)
    if num == matriz_zero(mat):
        valor = mat[0].get(pos)
        mat[0].pop(pos)  # se z for 0 "apaga" o valor que estava em y
        return valor

    valor = mat[0].get(pos)
    mat[0][pos] = num  # se z for diferente de 0 substitui-se z em y
    return valor

# 2.3.2 ------------------------------------------------------------------------

def matriz_valor(mat, pos):
    """Esta função serve para vermos qual o valor de uma posição da matriz
       mat: list - deve-se colocar aqui a matriz a considerar.
       pos : tuple - deve-se colocar neste argumento o valor que queremos
       retorno: tuple - valor da posição ou float - valor nulo
    """
    if pos in mat[0]:
        return mat[0][pos]  # se y tiver valor, devolvê-lo
    return mat[1]  # se nao tiver valor, devolver valor nulo


# 2.3.3 ------------------------------------------------------------------------
def matriz_dimensao(mat):
    """Serve para vermos quais as coordenadas máximas e mínimas de mat.
       mat: list - deve-se colocar aqui a matriz a considerar.
       retorno: tuple  - com a coordenada mínima e máxima.
    """

    tuplo_final = ()  # tuplo final que vamos dar return
    tuplo_das_posicoes = list(mat[0].keys())
    if len(tuplo_das_posicoes) == 0:
        return ()
    if len(tuplo_das_posicoes) == 1:
        # aqui sera o maior e menor ao mesmo tempo
        tuplo_final += (tuplo_das_posicoes[0],)
        tuplo_final += (tuplo_das_posicoes[0],)
    else:
        tuplo_final += (funcao_geral(mat)[6],funcao_geral(mat)[5])


    return tuplo_final  # serve para podermos atribuir o tuplo final à variavel


# 2.3.4 ------------------------------------------------------------------------
def matriz_densidade(mat):
    """Devolve o quociente entre o nº de elementos não nulos e a dimensão total.
       mat: list - deve-se colocar aqui a matriz a considerar.
       retorno: float - quociente entre o nº de elementos não nulos e a dimensão
                        total.
    """
    if len(mat[0]) == 0:
        return float(0)
    matriz_final = verifica_linhas_e_colunas(mat)
    n_de_linhas = len(matriz_final)
    n_de_colunas = len(matriz_final[0])
    dimensao_total = n_de_linhas * n_de_colunas
    n_de_valores_n_nulos = len(mat[0])
    quociente = n_de_valores_n_nulos / dimensao_total

    return quociente


# 2.3.5 ------------------------------------------------------------------------

def matriz_nulo(mat, nulo):
    """Esta função serve para substituirmoso valor nulo existente por um novo.
       mat: list - deve-se colocar aqui a matriz a considerar.
       nulo: float - o novo valor nulo.
       retorno: list - devolve a matriz com o novo valor nulo.
    """
    nulo = float(nulo)
    mat[1] = nulo
    keys = funcao_geral(mat)[0]
    values = funcao_geral(mat)[1]
    for d in range(0, len(values)):
        if values[d] == nulo:
            del mat[0][keys[d]]

    return mat


# 2.4.1 ------------------------------------------------------------------------

def matriz_str(mat, casas):
    """Esta função serve para vizualizarmos a matriz.
       mat: list - deve-se colocar aqui a matriz a considerar.
       casas: str - número de casas decimais que queremos que o valor de cada
                    posição tenha.
       retorno: str - devolve a matriz "agradável" visualmente.
    """
    # irar-se-à considerar a matriz obtida em funcao_geral(mat)
    matriz_final = verifica_linhas_e_colunas(mat)

    for d in range(0,len(matriz_final)):
        for c in range(0,len(matriz_final[0])):
            matriz_final[d][c] = casas % matriz_final[d][c]

    string = ''
    for linhas_mat_f in range(0, len(matriz_final)):  # desenhar a matriz
        for colunas_mat_f in range(0, len(matriz_final[0])):
            if colunas_mat_f == 0:
                string += f'{matriz_final[linhas_mat_f][colunas_mat_f]}'
            else:
                string += f' {matriz_final[linhas_mat_f][colunas_mat_f]}'
        if linhas_mat_f == len(matriz_final) - 1 \
                and colunas_mat_f == len(matriz_final[0]) - 1:
            pass
        else:
            string += '\n'

    return string


# 2.4.2 ------------------------------------------------------------------------

def matriz_linha(mat, linha):
    """Serve para "vermos" quais os elementos da linha da nossa matriz.
       mat: list - deve-se colocar aqui a matriz a considerar.
       linha: int - com este argumento escolhe-se a linha que se quer "ver".
       retorno: tuple -tuplo_das_linhas (contém os elementos da linha desejada).
    """

    linha = int(linha)
    matriz_final = funcao_geral(mat)[4]
    if matriz_final == []:
        return ()
    if linha > 0 and posicao_linha(matriz_dimensao(mat)[0]) <=linha \
            <= posicao_linha(matriz_dimensao(mat)[1]):
        tuplo_das_linhas = tuple(matriz_final[linha - 1][elemento]\
                           for elemento in range(0, len(matriz_final[0])))
                            # adicionar os elementos da linha y
    else:
        tuplo_das_linhas = ()

    return tuplo_das_linhas


# 2.4.3 ------------------------------------------------------------------------

def matriz_coluna(mat, coluna):
    """Serve para "vermos" quais os elementos da coluna da nossa matriz.
       mat: list - deve-se colocar aqui a matriz a considerar.
       linha: int - com este argumento escolhe-se a coluna que se quer "ver".
       retorno: tuple-tuplo_das_colunas(contém os elementos da coluna desejada).
    """
    coluna = int(coluna)
    matriz_final = funcao_geral(mat)[4]
    if matriz_final == []:
        #se a mat for uma matriz vazia
        return ()
    if coluna > 0 and posicao_coluna(matriz_dimensao(mat)[0]) <= coluna\
            <= posicao_coluna(matriz_dimensao(mat)[1]):
        tuplo_das_colunas = tuple(matriz_final[elemento][coluna - 1] \
                            for elemento in range(0, len(matriz_final)))
    else:
        tuplo_das_colunas = ()

    return tuplo_das_colunas


# 2.4.4 ------------------------------------------------------------------------

def matriz_diagonal(mat):
    """Serve para "vermos" quais os elementos da diagonal da nossa matriz.
       mat: list - deve-se colocar aqui a matriz a considerar.
       retorno: tuple - tuplo_final (contém os elementos da diagonal).
    """
    matriz_final = verifica_linhas_e_colunas(mat)
    if matriz_final == []:
        #se a mat for uma matriz vazia
        return ()
    if len(matriz_final) != len(matriz_final[0]):
        raise ValueError('matriz_diagonal: matriz não quadrada')
    posicao = [0,0]
    tuplo_final = ()  # posicao começa em [0,0]
    while posicao[0] != len(matriz_final):
        tuplo_final += (matriz_final[posicao[0]][posicao[1]],)
        posicao[0] += 1
        posicao[1] += 1  # +1 em cada elementoda posicao