twe     ={ 'A':{'0':'A','1':''},
           'B':{'0':'C','1':'B'},
           'C':{'0':'','1':'D'},
           'D':{'0':'C','1':''}}


def lectura_1(uno):
    return twe[uno]['1']


def lectura_2(cero):
    return twe[cero]['0']

def construccion(estado_1):
    transicion_1 = lectura_1(estado_1)
    if (transicion_1 == ''):
        relleno = '0'
    else:
        twe ={ 'A':{'0':'A','1':''},
               'B':{'0':'C','1':'B'},
               'C':{'0':'','1':'D'},
               'D':{'0':'C','1':''}}

def lectura_1(uno):
    return twe[uno]['1']
    
def lectura_2(cero):
    return twe[cero]['0']

def construccion(estado_1):
    transicion_1 = lectura_1(estado_1)
    if (transicion_1 == ''):
        relleno = '0'
    else:
        relleno = estado_1
    return relleno

def construccion_2(estado_2):
    transicion_2 = lectura_2(estado_2)
    if (transicion_2 == ''):
        relleno_2 = '0'
    else:
        relleno_2 = estado_2
    return relleno_2

def tabla():
    for estados in twe.keys():
        for transiciones in twe[estados].keys():
            if twe[estados][transiciones] == '': twe[estados][transiciones] = '0'

tabla()
print(twe)

nfa = twe


# estados_afd = ['A','AB','ABC','ABD']
estados_afd = []


def encontrar_transiciones(estado):

       # 01. Recibe estado: 'ABC'

       # 02. Lo separa individualmente: estados = ['A','B','C']

       # 03. Recupera los master keys que coinsidan con los estados:
       #     'A': ->  '1': ['A','B']          '0': ['A']
       #     'B': ->  '1': ['A','B']          '0': ['A','B','C']
       #     'C': ->  '1': ['A','B','D']      '0': ['A','B','C']

       # 04. Crea un set de elementos de 1's y un set de los elementos de 0's:
       #     '1': ['A','B','D']          '0': ['A','B','C']
       
       # 05. Regresa un diccionario de las transiciones del estado pedido:
       #     'ABC':{'1': ['ABD'],        '0': ['ABC']}
       
       estados = list(estado)

       lista_1s = []
       lista_0s = []

       vacio1 = ''
       vacio0 = ''

       for caracter in estados:
              vacio1 = vacio1 + ''.join(nfa[caracter]['1'])
              vacio0 = vacio0 + ''.join(nfa[caracter]['0'])
       
       lista_1s = set(list(vacio1))
       lista_0s = set(list(vacio0))
       
       print(lista_1s)
       print(lista_0s)

encontrar_transiciones('ABC')
#encontrar_transiciones('ABC')