
"""
automata = {
                'A':{'0':'A','1':'B','E':''},
                'B':{'0':'C','1':'B','E':'A'},
                'C':{'0':'','1':'D','E':'B'},
                'D':{'0':'C','1':'','E':'B'}
            }
estado_inicial = 'A'
estado_aceptacion = 'D'
"""

#Declaración e inicialización de variables
cerraduras_epsilon = {}             #Diccionario para guardar las cerraduras epsilon de cada uno de los estados del autómata
matriz_transicion_aumentada = {}    #Diccionario para guardar la matriz de transición aumentada del autómata
automata_sin_epsilon = {}           #Diccionario para guardar el autómata sin transiciones Epsilon equivalente

#Definicioón de funciones
#Esta función toma como parámetro un estado del autómata y retorna el estado/s resultado de una transición Epsilon
def transicion_E(estado, automata):
    return automata[estado]['Eps']  

#TODO:  [IMPORTANTE: FIXME]Es necesario agregar la validación para el caso en el que el autómata tenga transiciones epsilon en todos sus estados. 
#       El código actual producirá un error en la recursividad (se cicla, se enclocha) si se da el caso.
#Esta función toma como parámetro un estado del autómata y retorna los estados que conforman su cerradura Epsilon
def cerradura_epsilon(estado, automata):        
    transicion_con_E = transicion_E(estado, automata)    
    if(transicion_con_E == ['N']): c_epsilon = estado + ''
    else: 
        c_epsilon = estado
        for item in transicion_con_E:
            c_epsilon = c_epsilon + cerradura_epsilon(item, automata)    
    return c_epsilon

#Esta función toma como parámetro un estado del autómata junto con una de sus transiciones y retorna una lista de su función de transición aumentada
def transicion_aumentada(estado, trans, automata):
    c_epsilon = list(cerradura_epsilon(estado, automata))
    print("Cerradura epsilon: ", c_epsilon)
    t_aumentada = ''
    for epsilon in c_epsilon:
        transicion = automata[epsilon][trans]
        if transicion == ['N']: lista_epsilon = ''
        else:     
            lista_epsilon = []        
            for item in transicion:
                lista_epsilon = lista_epsilon + list(cerradura_epsilon(item, automata))
        t_aumentada = t_aumentada + ''.join(lista_epsilon)
        lista_epsilon = list(t_aumentada)
        lista_epsilon = list(dict.fromkeys(lista_epsilon))
        print("Transicion aumentada: ", lista_epsilon)
    return lista_epsilon

#Lógica para remover las transiciones Epsilon del autómata
def remover_epsilon(automata):
    #Esto valida las transiciones vacías (inexistentes, no confundir con transiciones Epsilon)
    for estados in automata.keys():
        for transiciones in automata[estados].keys():
            if automata[estados][transiciones] == '': automata[estados][transiciones] = 'N'
    print("[DBG]AUTOMATA PARA REMOVER EPSILON:\n", automata)
    #Calcular las cerraduras Epsilon de todos los estados y llena el diccionario respectivo
    for estados in automata.keys():
        cerraduras_epsilon[estados] = cerradura_epsilon(estados, automata)
    print("[DBG]CERRADURAS EPSILON:\n", cerraduras_epsilon)
    #Calcular la matriz de transición aumentada y llena el diccionario respectivo
    for estados in automata.keys():
        matriz_transicion_aumentada[estados] = {}
        for transiciones in automata[estados].keys():
            matriz_transicion_aumentada[estados][transiciones] = transicion_aumentada(estados, transiciones, automata)
        del matriz_transicion_aumentada[estados]['Eps']   #Elimina la columna Epsilon del diccionario porque no es necesaria en la matriz de transición aumentada
    print("[DBG]MATRIZ DE TRANSICION AUMENTADA:\n", matriz_transicion_aumentada)

    #Ordena los estados para evitar el TOC
    for estados in matriz_transicion_aumentada.keys():
        for transiciones in matriz_transicion_aumentada[estados].keys():
            matriz_transicion_aumentada[estados][transiciones] = sorted(matriz_transicion_aumentada[estados][transiciones])
    automata_sin_epsilon = matriz_transicion_aumentada
    return automata_sin_epsilon

    #print(automata_sin_epsilon)