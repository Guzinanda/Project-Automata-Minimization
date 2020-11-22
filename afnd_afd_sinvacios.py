'''
CONVERTIDOR DE AFND a AFD 

Input:
nfa = {'A'   : { '1':['A','B'],       '0':['A']}, 
       'B'   : { '1':['A','B'],       '0':['A','B','C']}, 
       'C'   : { '1':['A','B','D'],   '0':['A','B','C']}, 
       'D'   : { '1':['A','B'],       '0':['A','B','C']}}

Output:
dfa = {'A'   : { '1':['AB'],          '0':['A']}, 
       'AB'  : { '1':['AB'],          '0':['ABC']}, 
       'ABC' : { '1':['ABD'],         '0':['ABC']}, 
       'ABD' : { '1':['AB'],          '0':['ABC']}}
'''





#? El usuario nos da la tabla del NFA sin E y sin vacios _______________________________________________

'''
nfa = {'A':{'1':['A','B'],         '0':['A']}, 
       'B':{'1':['A','B'],         '0':['A','B','C']}, 
       'C':{'1':['A','B','D'],     '0':['A','B','C']}, 
       'D':{'1':['A','B'],         '0':['A','B','C']}}
'''

nfa = {'A':{'1':['B','C'],         '0':['E']}, 
       'B':{'1':['A'],             '0':['']}, 
       'C':{'1':['D'],             '0':['']}, 
       'D':{'1':[''],              '0':['A']},
       'E':{'1':[''],              '0':['']}}

dfa = {}

'''
Output:
dfa = {'A'   : { '1':['BC'],          '0':['E']}, 
       'BC'  : { '1':['AD'],          '0':['E']}, 
       'AD'  : { '1':['BC'],          '0':['AE']}, 
       'E'   : { '1':['N'],           '0':['N']}, 
       'AE'  : { '1':['BC'],          '0':['E']}}
'''





# Estado inicial del NFA:
estado_inicial = 'A'
# Estado final del NFA:
estado_aceptacion = 'D'  


#? Algoritmo para encontrar trandisiones de estados ____________________________________________________

# estados_afd = ['A','AB','ABC','ABD']
estados_afd = [estado_inicial]

# Estados validados
validados = []

romper = bool

# @  Recibe estado: 
#    'ABC'

# @  Genera sus transiciones con '1' y '0'
#    lista1s = 'ABD'  y  lista0s = 'ABC'

# @ TODO: Agrega a diccionario el estado y sus transiciones:
#   nfa = {'ABC': {'1':['ABD'], '0':['ABC']}}

# @  Agrega los nuevos estados a la lista de estados_afd si no estaba antes
#    lista1s = 'ABD'  y  lista0s = 'ABC'
#               ---
#    estados_afd = ['A','AB','ABC']
#    estados_afd = ['A','AB','ABC','ABD']
#                                   ---


#? Algoritmo para remover las transiciones Epsilon del autómata ________________________________________
#Esto valida las transiciones vacías (inexistentes, no confundir con transiciones Epsilon)
def quitar_vacios():
       adelita_sensual = 0
       for estados in nfa.keys():
              for transiciones in nfa[estados].keys():
                     if nfa[estados][transiciones] == ['']:
                            adelita_sensual = 1 
                            nfa[estados][transiciones] = 'N'  
       if adelita_sensual == 1:
              nfa['N'] = {}
              nfa['N']['0'] = 'N'  
              nfa['N']['1'] = 'N'  


'''
nfa = {'A'   : { '1':['A','B'],       '0':['']}, 
       'B'   : { '1':['A','B'],       '0':['A','B','C']}, 
       'C'   : { '1':['A','B','D'],   '0':['A','B','C']}, 
       'D'   : { '1':['A','B'],       '0':['A','B','C']}}

nfa = {'A'   : { '1':['A','B'],       '0':['N']}, 
       'B'   : { '1':['A','B'],       '0':['A','B','C']}, 
       'C'   : { '1':['A','B','D'],   '0':['A','B','C']}, 
       'D'   : { '1':['A','B'],       '0':['A','B','C']}}
'''
# TODO: Agregar caso con vacio.

def encontrar_transiciones(estado_inicial):

       no_romper = True

       while no_romper:

              for sta in estados_afd:
              
                     # 01. Recibe siempre el estado inicial:
                     if (sta in estados_afd) and (sta not in validados):

                            # 02. Lo separa individualmente: estados = ['A','B','C']
                            sta = list(sta)

                            # 03. Itera individualmente cada key del dictionario (estados), en este caso A, B y C
                            #     creando un str de cada conjunto de estados por transicion1 y trandicion0:
                            
                            #     For 'A'  ->  transicion1 = 'AB'          transicion0 = 'A'
                            #     For 'B'  ->  transicion1 = 'AB'          transicion0 = 'ABC'
                            #     For 'C'  ->  transicion1 = 'ABD'         transicion0 = 'ABC'

                            #     Juntando por cada iteracion en cadenas grandes por transicion1 y transicion0
                            #     For 'ABC': ->  transicion1 = 'ABABABD'     transicion0 = 'AABCABC'

                            transicion1 = ''
                            transicion0 = ''

                            for caracter in sta:
                                   transicion1 = transicion1 + ''.join(nfa[caracter]['1'])
                                   transicion0 = transicion0 + ''.join(nfa[caracter]['0'])
                            

                            # 04. Crea sets de transicion1 y transicion0 para eliminar elementos repetidos y 
                            #     al final los trasforma en strings y los ordena alfabeticamente:
                            
                            #     lista1s = set('ABABABD')         lista0s = set('AABCABC')
                            #     lista1s = ['A','B','D']          lista0s = ['A','B','C']
                            #     lista1s = 'ABD'                  lista0s = 'ABC'

                            lista1s = ''.join(sorted(set(list(transicion1))))
                            lista0s = ''.join(sorted(set(list(transicion0))))


                            # 05. Vuelve a coombinar el estado incial en un str 
                            sta = ''.join(sta)


                            # 05. Imprime el estado que se ingresó y a los estados a los que llega con transicion 1 y 0

                            dfa = {}
                            print(f'Transiciones de {sta}:  1:{lista1s}  0:{lista0s}')

                            # TODO: Algoritmo para repetir hasta que no se verifiquen todos _________________________________________


                            '''
                            Output:
                            dfa = {'A'   : { '1':['BC'],          '0':['E']}, 
                                   'BC'  : { '1':['AD'],          '0':['E']}, 
                                   'AD'  : { '1':['BC'],          '0':['AE']}, 
                                   'E'   : { '1':['N'],           '0':['N']}, 
                                   'AE'  : { '1':['BC'],          '0':['E']}}
                            '''





                            # 06. Agrega los nuevos estados a la lista de estados_afd si no estaba antes
                            #     lista1s = 'AB'                  lista0s = 'N'
                            #     estados_afd = ['A','AB','ABC']
                            #     estados_afd = ['A','AB','ABC','ABD']

                            if lista1s not in estados_afd:
                                   estados_afd.append(lista1s)
                                   
                            if lista0s not in estados_afd:
                                   estados_afd.append(lista0s)

                            # 07. Agrega el estado ya validado a una lista para no repetir:
                            #     validados = ['A']
                            validados.append(sta)
                     
                     else:
                            no_romper = False








#? TEST ________________________________________________________________________________________________

print('\n')

quitar_vacios()

encontrar_transiciones('A')
#encontrar_transiciones('AB')
#encontrar_transiciones('ABC')
#encontrar_transiciones('ABD')

print('\n')

#print(estados_afd)
print('\n')
