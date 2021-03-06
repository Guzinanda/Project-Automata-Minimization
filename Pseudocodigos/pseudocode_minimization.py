
'''
0.  ENTRADA: 
    Usuario mete su automata de esta manera
    Ejemplo en Archivo04

    transitions     ={
                        '1':{'0':'2','1':'1'}, 
                        '2':{'0':'1','1':'3'},
                        '3':{'0':'4','1':'2'},
                        '4':{'0':'4','1':'1'},
                        '5':{'0':'4','1':'6'},
                        '6':{'0':'7','1':'5'},
                        '7':{'0':'6','1':'7'},
                        '8':{'0':'7','1':'4'}}

    estado_inicial = 
    estado_aceptacion = 4


01. ALGORÍTMO DE MINIMIZACIÓN:

    1. Crear todas las parejas posibles sin repetir combinaciones:
        [1,2], [1,3], [1,4], [1,5], [1,6], [1,7], [1,8]
        [2,3], [2,4], [2,5], [2,6], [2,7], [2,8]
        [3,4], [3,5], [3,6], [3,7], [3,8]
        [4,5], [4,6], [4,7], [4,8]
        [5,6], [5,7], [5,8]
        [6,7], [6,8]
        [7,8]

    2. PRIMER PASADA: Todas las parejas que contengan un estado de aceptacion 
       y uno que no, es decir [6,1] no puede ser ni [6,6] o [1,3]:
       [1,2], [1,3], [1,4], [1,5], [ x ], [1,7]
       [2,3], [2,4], [2,5], [ x ], [2,7]
       [3,4], [3,5], [ x ], [3,7]
       [4,5], [ x ], [4,7]
       [ x ], [5,7]
       [ x ]

    3. Determinar transiciones para cada pareja de estado:
       [1,2]: {'0':{2,1},'1':{1,3},
       [1,3]: {'0':{2,4},'1':{1,2},
       [1,4]: {'0':{ , },'1':{ , },
       [1,5]: {'0':{2,4},'1':{1,6},
       [1,6]: {'0':{2,7},'1':{1,5},
       [1,7]: {'0':{2,6},'1':{1,7},
       [1,8]: {'0':{2,7},'1':{1,4},
       [2,3]: {'0':{1,4},'1':{3,2},
       [2,4]: {'0':{ , },'1':{ , },
       [2,5]: {'0':{1,4},'1':{3,6},
       [2,6]: {'0':{1,7},'1':{3,5},
       [2,7]: {'0':{1,6},'1':{3,7},
       [2,8]: {'0':{1,7},'1':{3,4},
       [3,4]: {'0':{ , },'1':{ , },
       [3,5]: {'0':{4,4},'1':{2,6},
       [3,6]: {'0':{4,7},'1':{2,5},
       [3,7]: {'0':{4,6},'1':{2,7},
       [3,8]: {'0':{4,7},'1':{2,4},
       [4,5]: {'0':{ , },'1':{ , },
       [4,6]: {'0':{ , },'1':{ , },
       [4,7]: {'0':{ , },'1':{ , },
       [4,8]: {'0':{ , },'1':{ , },
       [5,6]: {'0':{4,7},'1':{6,5},
       [5,7]: {'0':{4,6},'1':{6,7},
       [5,8]: {'0':{4,7},'1':{6,4},
       [6,7]: {'0':{7,6},'1':{5,7},
       [6,8]: {'0':{7,7},'1':{5,4},
       [7,8]: {'0':{6,7},'1':{7,4},

     
    4. SEGUNDA PASADA: De nuevo saca todos los pares que no tengan uno si y uno no, 
       aunque ambos tengan un 6 (no puede ser en el mismo par ordenado):
       [1,2]: {'0':{2,1},'1':{1,3}, 
       [1,3]: {'0':{2,4},'1':{1,2}, X
       [1,4]: {'0':{ , },'1':{ , },
       [1,5]: {'0':{2,4},'1':{1,6}, X
       [1,6]: {'0':{2,7},'1':{1,5},
       [1,7]: {'0':{2,6},'1':{1,7},
       [1,8]: {'0':{2,7},'1':{1,4}, X
       [2,3]: {'0':{1,4},'1':{3,2}, X
       [2,4]: {'0':{ , },'1':{ , },
       [2,5]: {'0':{1,4},'1':{3,6}, X
       [2,6]: {'0':{1,7},'1':{3,5},
       [2,7]: {'0':{1,6},'1':{3,7},
       [2,8]: {'0':{1,7},'1':{3,4}, X
       [3,4]: {'0':{ , },'1':{ , },
       [3,5]: {'0':{4,4},'1':{2,6},
       [3,6]: {'0':{4,7},'1':{2,5}, X
       [3,7]: {'0':{4,6},'1':{2,7}, X
       [3,8]: {'0':{4,7},'1':{2,4}, X
       [4,5]: {'0':{ , },'1':{ , },
       [4,6]: {'0':{ , },'1':{ , },
       [4,7]: {'0':{ , },'1':{ , },
       [4,8]: {'0':{ , },'1':{ , },
       [5,6]: {'0':{4,7},'1':{6,5}, X
       [5,7]: {'0':{4,6},'1':{6,7}, X
       [5,8]: {'0':{4,7},'1':{6,4}, X
       [6,7]: {'0':{7,6},'1':{5,7}, 
       [6,8]: {'0':{7,7},'1':{5,4}, X
       [7,8]: {'0':{6,7},'1':{7,4}, X


    5. TERCERA PASADA: Sub keys van a comparace con el key master se eliminan (no cuenta el 
       mismo estado) con que uno sea. (Los que ya marque no lso tengo que volver a marcar):
       Solo los marcados anteriores.
       [1,2]: {'0':{2,1},'1':{1,3},  X
       [1,3]: {'0':{2,4},'1':{1,2}, X
       [1,4]: {'0':{ , },'1':{ , },   
       [1,5]: {'0':{2,4},'1':{1,6}, X
       [1,6]: {'0':{2,7},'1':{1,5},   X
       [1,7]: {'0':{2,6},'1':{1,7},   
       [1,8]: {'0':{2,7},'1':{1,4}, X 
       [2,3]: {'0':{1,4},'1':{3,2}, X
       [2,4]: {'0':{ , },'1':{ , },   
       [2,5]: {'0':{1,4},'1':{3,6}, X
       [2,6]: {'0':{1,7},'1':{3,5},   
       [2,7]: {'0':{1,6},'1':{3,7},   X
       [2,8]: {'0':{1,7},'1':{3,4}, X 
       [3,4]: {'0':{ , },'1':{ , },    
       [3,5]: {'0':{4,4},'1':{2,6},   
       [3,6]: {'0':{4,7},'1':{2,5}, X
       [3,7]: {'0':{4,6},'1':{2,7}, X
       [3,8]: {'0':{4,7},'1':{2,4}, X
       [4,5]: {'0':{ , },'1':{ , },   
       [4,6]: {'0':{ , },'1':{ , },   
       [4,7]: {'0':{ , },'1':{ , },   
       [4,8]: {'0':{ , },'1':{ , },   
       [5,6]: {'0':{4,7},'1':{6,5}, X
       [5,7]: {'0':{4,6},'1':{6,7}, X
       [5,8]: {'0':{4,7},'1':{6,4}, X
       [6,7]: {'0':{7,6},'1':{5,7},   X
       [6,8]: {'0':{7,7},'1':{5,4}, X
       [7,8]: {'0':{6,7},'1':{7,4}, X

⟶
    6. De las parejas que quedaron sin marcar combinar las que tienen un estado en comun:

        1,7
        2,6
        3,5

        4
        8

       Combinaciones: 	(17)  (26) (35) (4) (8)
                        A     B    C     D   E
                         

    7. Hacer tabla de transiciones minimas:
       combinaciones_f ={
                        'A':{'0':'B', '1':'A'}} 

                        'B':{'0':'A','1':'C'},

                        'C':{'0':'D','1':'D'},

                        'D':{'0':'D','1':'A'},

                        'E':{'0':'A','1':'A'},


TO DO:
- Esto es para AFD

TO DO:
- Algoritmo para convertir de No determinista (NAFD) a Determinista (AFD)


Sin empsilon: Fernanada 
- Convertir


Con epsilon: Juan
- Primero quitar 
- Convertir


'''