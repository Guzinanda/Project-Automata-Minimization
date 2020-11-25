#TODO:  Por ahora el alfabeto siempre es {0, 1}, en caso de dejar esto a discreción del usuario debemos 
#       implementar lógica agnóstica al alfabeto

import re

#Este es el automata de la presentación 04, diapositiva 114
"""
automata = {
    's1': {'0':'s2', '1':'s2'},
    's2': {'0':'s4', '1':'s5'},
    's3': {'0':'s6', '1':'s7'},
    's4': {'0':'s4', '1':'s5'},
    's5': {'0':'s6', '1':'s7'},
    's6': {'0':'s4', '1':'s5'},
    's7': {'0':'s6', '1':'s7'}
}
estado_inicial = 's1'
estados_aceptacion = ['s6']
"""
#Este es el automata del segundo examen parcial
#automata = {
#    's1':{'0':'s2','1':'s1'}, 
#    's2':{'0':'s1','1':'s3'},
#    's3':{'0':'s4','1':'s2'},
#    's4':{'0':'s4','1':'s1'},
#    's5':{'0':'s4','1':'s6'},
#    's6':{'0':'s7','1':'s5'},
#    's7':{'0':'s6','1':'s7'},
#    's8':{'0':'s7','1':'s4'}
#}
#estado_inicial = 1
#estados_aceptacion = ['s4']

#Definición de variables
pares_transiciones = {}                 #Esto crea un diccionario vacío para guardar las transiciones de las parejas de estados
automata_minimizado = {}                #Esto crea un diccionario vacío para guardar el automata minimizado final
pares_marcados = []                     #Esto crea una lista vacía para guardar las parejas de estados a marcar
pares_no_marcados = []                  #Esto crea una lista vacía para guardar las parejas de estados que no han sido marcadas después de todas las pasadas
bandera_pasadas = 0                     #Bandera que nos indica si es necesaria otra pasada. 0=No es necesaria, 1=Si es necesaria

#NOTA:  Si en algún momento tenemos problemas con el tiempo de ejecución del programa (i.e. performance), 
#       estas funciones se pueden refactorizar para sustituir los if anidados en for por un chequeo más óptimo de la forma:
#       if <item> in <list>
#       -God bless python \o/ (and people on stackoverflow for teaching us how to use it properly)-

#Definición de funciones
#Esta función recibe como parámetro dos estados del autómata y retorna 1 si son estados compatibles o 0 si no lo son
def es_compatible(estado_1, estado_2, estados_aceptacion):
    estado_1_aceptacion = 0
    estado_2_aceptacion = 0
    for estado_aceptacion in estados_aceptacion:
        if estado_1 == estado_aceptacion: estado_1_aceptacion = 1
        if estado_2 == estado_aceptacion: estado_2_aceptacion = 1
    if (estado_1_aceptacion == 0 and estado_2_aceptacion == 1) or (estado_1_aceptacion == 1 and estado_2_aceptacion == 0):
        return 1
    else:
        return 0

#Esta función recibe como parámetro una pareja de estados (junto con sus transiciones) y retorna 1 si esa pareja debe ser marcada o 0 si no debe serlo
def es_marcada(pareja_estados):
    bandera_es_marcado = 0
    for par_marcado in pares_marcados:
        if (pareja_estados['0'] == par_marcado) or (pareja_estados['1'] == par_marcado):
            bandera_es_marcado = 1
            break
    return bandera_es_marcado

def voltear_par(par):    
    lista = par.split(',')
    print(lista)
    cadena_volteada = lista[1] + ',' + lista[0]
    return(cadena_volteada)

#print("Automata\n", automata)
#print("\n")
def minimizer(automata, estados_aceptacion):
    lista_combinaciones = []                #Esto crea una lista vacía para guardar la lista de combinaciones finales
    automata_keys = list(automata.keys())   #Esto pone en una lista todos los estados del autómata
    if '' in automata_keys:         
        del automata['']
        automata_keys.remove('')
    print(automata_keys)
    #Este for anidado crea la tabla de transiciones por par de estados y marca las parejas de estados compatibles (primera pasada)
    for key in automata.keys():
        for idx in range (automata_keys.index(key) + 1, len(automata_keys)):
            pares_transiciones[key + ',' + automata_keys[idx]] = {}
            pares_transiciones[key + ',' + automata_keys[idx]]['0'] = automata[key]['0'] + ',' + automata[automata_keys[idx]]['0'] 
            pares_transiciones[key + ',' + automata_keys[idx]]['1'] = automata[key]['1'] + ',' + automata[automata_keys[idx]]['1']                
            if (es_compatible(key, automata_keys[idx], estados_aceptacion)):    #Marcamos la pareja si son estados compatibles (Primera pasada)
                pares_marcados.insert(len(pares_marcados), key + ',' + automata_keys[idx])

            """       
            if automata[key]['0'] == automata[automata_keys[idx]]['0']: #Si las transiciones son al mismo estado no se necesita normalización
                pares_transiciones[key + automata_keys[idx]]['0'] = automata[key]['0'] + automata[automata_keys[idx]]['0']            
            else:   #Si las transiciones son a estados diferentes normalizamos antes de formar la tabla de transiciones
                par_ordenado = sorted({automata[key]['0'], automata[automata_keys[idx]]['0']})
                pares_transiciones[key + automata_keys[idx]]['0'] = par_ordenado[0] + par_ordenado[1]
            if automata[key]['1'] == automata[automata_keys[idx]]['1']:
                pares_transiciones[key + automata_keys[idx]]['1'] = automata[key]['1'] + automata[automata_keys[idx]]['1']
            else:
                par_ordenado = sorted({automata[key]['1'], automata[automata_keys[idx]]['1']})            
                pares_transiciones[key + automata_keys[idx]]['1'] = par_ordenado[0] + par_ordenado[1]     
            if (es_compatible(key, automata_keys[idx], estados_aceptacion)):    #Marcamos la pareja si son estados compatibles
                pares_marcados.insert(len(pares_marcados), key + automata_keys[idx])
            """

    print("Pares con sus transiciones\n", pares_transiciones)
    print("\n")

    #Este ciclo realiza las pasadas necesarias para completar la minimización
    while True:
        bandera_pasadas = 0
        for par_estados in pares_transiciones.keys():
            bandera_ya_marcado = 0
            for par_marcado in pares_marcados:                
                if (pares_transiciones[par_estados]['0'] == par_marcado) or (pares_transiciones[par_estados]['0'] == voltear_par(par_marcado)) or (pares_transiciones[par_estados]['1'] == par_marcado) or (pares_transiciones[par_estados]['1'] == voltear_par(par_marcado)):  #Switch pairs
                    for ya_marcado in pares_marcados:
                        if par_estados == ya_marcado:
                            bandera_ya_marcado = 1
                            break
                    if bandera_ya_marcado == 0:
                        pares_marcados.insert(len(pares_marcados), par_estados)
                        bandera_pasadas = 1
                        break
        if bandera_pasadas == 0: break

    print("Pares marcados\n", pares_marcados)
    print("\n")

    #Este ciclo obtiene la lista de pares no marcados utilizando la lista final de pares marcados
    for par_estados in pares_transiciones.keys():
        bandera_ya_marcado = 0
        for par_marcado in pares_marcados:
            if par_estados == par_marcado: 
                bandera_ya_marcado = 1
                break
        if bandera_ya_marcado == 0: pares_no_marcados.insert(len(pares_no_marcados), par_estados)

    print("Pares no marcados\n", pares_no_marcados)
    print("\n")

    #Este ciclo le dará formato de listas a las parejas de estados no marcados para poder encontrar las combinaciones
    for par_estados in pares_no_marcados:    
        lista_combinaciones.insert(len(lista_combinaciones), par_estados.split(','))
        """
        regex_res = re.split("(s[0-9]+)", par_estados)  #Esto separa la pareja de estados en una lista que contiene estados individuales    
        regex_res = [i for i in regex_res if i]         #Esto remueve elementos vacíos de la lista que por alguna razón aparecen después de la regexp    
        lista_combinaciones.insert(len(lista_combinaciones), regex_res) #Esto crea una lista que contiene las listas generadas anteriormente (lista de listas :K)
        """

    print("Lista separada\n", lista_combinaciones)
    print("\n")

    #Este bloque de código tremendamente ineficiente encuentra las combinaciones y modifica las listas de acuerdo a ellas
    for lista_estados in lista_combinaciones:
        for elementos in lista_estados:
            for idx in range(lista_combinaciones.index(lista_estados) + 1, len(lista_combinaciones)):            
                if elementos in lista_combinaciones[idx]:                
                    lista_combinaciones[lista_combinaciones.index(lista_estados)].extend(lista_combinaciones[idx])  #Combina parejas de estados con estados en común
                    lista_combinaciones[idx] = ''   #Vacía las parejas anexadas en el paso anterior. Esto es para evitar que idx se salga del rango
                    print(lista_combinaciones)
    lista_combinaciones = [i for i in lista_combinaciones if i] #Remueve las sub-listas que quedaron vacías
    for idx in range(len(lista_combinaciones)):     
        lista_combinaciones[idx] = list(dict.fromkeys(lista_combinaciones[idx]))  #Remueve los estados repetidos de las listas combinadas

    print("Lista de combinaciones sin estados solitos\n", lista_combinaciones)
    print("\n")

    #Añadir los estados que no fueron combinados
    for estados in automata.keys():
        bandera_existe = 0
        for combinaciones in lista_combinaciones:
            if estados in combinaciones: bandera_existe = 1
        if bandera_existe == 0:        
            lista_combinaciones.append(list([estados]))        

    #print("Lista completa de combinaciones\n", lista_combinaciones)
    #print("\n")

    #TODO:  [Nice to have]Si queda tiempo, validar que las transiciones de las combinaciones son consistentes con las transiciones de los estados que las componen
    #       Por ahora asumimos que ningún error catastrófico ha ocurrido
    #Calcular transiciones para las combinaciones
    for combinaciones in lista_combinaciones:
        formato_combinacion = ''.join(combinaciones)
        #print("Combinacion: ", combinaciones)
        #print("\n")
        automata_minimizado[''.join(combinaciones)] = {}    
        estado_de_transicion = automata[combinaciones[0]]['0']
        #print("Estado de transicion0: ", estado_de_transicion)
        #print("\n")
        for estados in lista_combinaciones:
            if estado_de_transicion in estados: 
                automata_minimizado[formato_combinacion]['0'] = ''.join(estados)
                #print("Automata: ", automata_minimizado)
                break
        estado_de_transicion = automata[combinaciones[0]]['1']
        #print("Estado de transicion1: ", estado_de_transicion)
        #print("\n")
        for estados in lista_combinaciones:
            if estado_de_transicion in estados: 
                automata_minimizado[formato_combinacion]['1'] = ''.join(estados)
                #print("Automata: ", automata_minimizado)        
                break

    #Calcular estados de aceptacion
    nuevos_estados_aceptacion = []
    for estados in automata.keys():
        new_list = list(estados)
        print(new_list)
        for item in estados_aceptacion:
            if item in new_list: nuevos_estados_aceptacion.append(estados)
    
    #keys_finales = automata_minimizado.keys()
    print(len(automata_minimizado.keys()))
    if len(automata_minimizado.keys()) == 1: 
        return automata, nuevos_estados_aceptacion
    else: 
        return automata_minimizado, nuevos_estados_aceptacion

    #print("Automata minimizado\n", automata_minimizado)
    #print("\n")