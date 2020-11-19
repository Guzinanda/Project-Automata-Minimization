
# Convertir NFA sin transiciones vacias a DFA 


# 01. El usuario nos da la tabla de NFA:

nfa = {'A':{'1':['A','B'],         '0':['A']}, 
       'B':{'1':['A','B'],         '0':['A','B','C']}, 
       'C':{'1':['A','B','D'],     '0':['A','B','C']}, 
       'D':{'1':['A','B'],         '0':['A','B','C']}}

# Estado inicial del NFA:
nfa_initial_state = ['A']
# Estado final del NFA:
nfa_final_state = ['D']  


# ////////////////////////////////////////////////////////////////////////////////////////////////

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

encontrar_transiciones('A')
#encontrar_transiciones('ABC')



'''
dfa = {'A'   : {'1':['AB'],    '0':['A']}, 
       'AB'  : {'1':['AB'],    '0':['ABC']}, 
       'ABC' : {'1':['ABD'],   '0':['ABC']}, 
       'ABD' : {'1':['AB'],    '0':['ABC']}}
'''
