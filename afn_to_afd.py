
#? El usuario determina el NFA ______________________________________________________________________________________________________

#TODO Ejemplo 01: Sin transiciones vacias y sin epsilons
#Input:
#nfa = {'A'   :{'0':['A'],           '1':['A','B']},        
#       'B'   :{'0':['A','B','C'],   '1':['A','B']},
#       'C'   :{'0':['A','B','C'],   '1':['A','B','D']}, 
#       'D'   :{'0':['A','B','C'],   '1':['A','B']}}

#estado_inicial = 'A'
#estado_aceptacion = 'D' 
#dfa = {}

#Output:
#dfa = {'A'   :{'0':['A'],           '1':['AB']}, 
#       'AB'  :{'0':['ABC'],         '1':['AB']}, 
#       'ABC' :{'0':['ABC'],         '1':['ABD']}, 
#       'ABD' :{'0':['ABC'],         '1':['AB']}}


#TODO Ejemplo 02: Con transiciones vacias pero sin epsilons

#Input:
"""
nfa = {'A'    :{'0':['E'],           '1':['B','C']}, 
       'B'    :{'0':[''],            '1':['A']}, 
       'C'    :{'0':[''],            '1':['D']}, 
       'D'    :{'0':['A'],           '1':['']},
       'E'    :{'0':[''],            '1':['']}}

estado_inicial = 'A'
estado_aceptacion = 'E' 
"""

dfa = {}

#Output:
#dfa = {'A'   : {'0':['E'],          '1':['BC']},
#       'BC'  : {'0':['E'],          '1':['AD']}, 
#       'AD'  : {'0':['AE'],         '1':['BC']}, 
#       'E'   : {'0':['N'],          '1':['N']}, 
#       'AE'  : {'0':['E'],          '1':['BC']}}


#TODO Ejemplo 03: Con transiciones vacias y con epsilons
#Input:
#nfa = {'A'   :{'0':['E'],           '1':['B','C']}, 
#       'B'   :{'0':[''],            '1':['A']}, 
#       'C'   :{'0':[''],            '1':['D']}, 
#       'D'   :{'0':['A'],           '1':['']},
#       'E'   :{'0':[''],            '1':['']}}

#estado_inicial = 'A'
#estado_aceptacion = 'E' 
#dfa = {}

#Output:
#dfa = {'A'   :{'0':['E'],           '1':['BC']}, 
#       'BC'  :{'0':['E'],           '1':['AD']}, 
#       'AD'  :{'0':['AE'],          '1':['BC']}, 
#       'E'   :{'0':['N'],           '1':['N']}, 
#       'AE'  :{'0':['E'],           '1':['BC']}}



#? Algoritmos para limpiar el automata de vacios y epsilons _________________________________________________________________________
# Limpia el nfa de estados vacios:
import afn_vacios_afn as limpiar
import formatear_output as formatear

#? Algoritmo que encuentra las trandisiones de los estados __________________________________________________________________________
def encontrar_transiciones(nfa, estado_inicial, estado_final):

       limpiar.quitar_vacios(nfa)

       # estados_afd = ['A']
       estados_afd = [estado_inicial]

       validados = []

       no_terminado = True

       while no_terminado:
              for sta in estados_afd:

                     # 01. Va a revisar los estados que vayan entrando en esyados_afd y si no estan validados: e.g. 'A'
                     if (sta in estados_afd) and (sta not in validados):

                            # 02. Lo separa individualmente sin son multiples estados: eta = ['A','B','C']
                            sta = list(sta)

                            # 03. Itera individualmente cada key del dictionario (estados), en este caso e.g. A, B y C
                            #     creando un str de cada conjunto de estados por transicion1 y trandicion0:
                            
                            #     For 'A'  ->    transicion0 = 'A'         transicion1 = 'AB'          
                            #     For 'B'  ->    transicion0 = 'ABC'       transicion1 = 'AB'          
                            #     For 'C'  ->    transicion0 = 'ABC'       transicion1 = 'ABD'         

                            #     Juntando por cada iteracion en cadenas grandes por transicion1 y transicion0
                            #     For 'ABC': ->  transicion0 = 'AABCABC'   transicion1 = 'ABABABD'

                            transicion0 = ''
                            transicion1 = ''

                            for caracter in sta:
                                   transicion0 = transicion0 + ''.join(nfa[caracter]['0'])
                                   transicion1 = transicion1 + ''.join(nfa[caracter]['1'])
                            

                            # 04. Crea sets de transicion0 y transicion1 para eliminar elementos repetidos y 
                            #     al final los trasforma en strings y los ordena alfabeticamente:
                            
                            #     lista0s = set('AABCABC')        lista1s = set('ABABABD')         
                            #     lista0s = ['A','B','C']         lista1s = ['A','B','D']          
                            #     lista0s = 'ABC'                 lista1s = 'ABD'                  

                            lista0s = ''.join(sorted(set(list(transicion0))))
                            lista1s = ''.join(sorted(set(list(transicion1))))


                            # 05. Elimina N si tiene N al final y es mas de un caracter

                            if len(lista0s) > 1:
                                   lista0s = lista0s.replace('N','')
                            
                            if len(lista1s) > 1:
                                   lista1s = lista1s.replace('N','')


                            # 06. Vuelve a coombinar el estado incial en un str 
                            sta = ''.join(sta)


                            # 07. Imprime el estado que se ingresó y a los estados a los que llega con transicion 0 y 1:
                            # print(f'Transiciones de {sta}:  \t0:{lista0s}  \t1:{lista1s}')


                            # 07. Guarda los datos en un diccionario dfa{}:
                            
                            #dfa = {'A'   : {'0':['E'],    '1':['BC']},
                            #       'BC'  : {'0':['E'],    '1':['AD']}, 
                            #       'AD'  : {'0':['AE'],   '1':['BC']}, 
                            #       'E'   : {'0':['N'],    '1':['N']}, 
                            #       'AE'  : {'0':['E'],    '1':['BC']}}     

                            dfa[sta] = {'0':lista0s, '1':lista1s}


                            # 08. Agrega los nuevos estados a la lista de estados_afd si no estaba antes
                            #     lista1s = 'AB'                  lista0s = 'N'
                            #     estados_afd = ['A','AB','ABC']
                            #     estados_afd = ['A','AB','ABC','ABD']

                            if lista1s not in estados_afd:
                                   estados_afd.append(lista1s)
                                   
                            if lista0s not in estados_afd:
                                   estados_afd.append(lista0s)

                            # 09. Agrega el estado ya validado a una lista para no repetir:
                            #     validados = ['A']
                            validados.append(sta)
                     
                     else:
                            no_terminado = False

       print(dfa)

       #dfa_formateado = formatear.formatear_output(dfa)

       #print(dfa_formateado)

       return dfa







#? TEST _____________________________________________________________________________________________________________________________

#encontrar_transiciones('A')
