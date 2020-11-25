from tkinter import *
from tkinter import ttk

import tkinter.scrolledtext as tkst

import afn_to_afd
import afn_epsilon_afn
import afd_minimization
import formatear_output
import afn_vacios_afn as limpiar

"""
class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Minimizacion de automatas")
        self.etiqueta_encabezado = Label(master, text="Programa que minimiza automatas finitos deterministas y no deterministas")
        self.etiqueta_encabezado.pack()
        self.etiqueta_indicaciones = Label(master, text="Favor de indicar el automata a minimizar, solamente se aceptan automatas que reconocen el alfabeto {0, 1}")
        self.etiqueta_indicaciones.pack()
"""

#? Definición de variables ______________________________________________________________________________________________________________________________________________

eje_x = 330 #Valor inicial en x (Donde se imprime el 0 del encabezado)
eje_y = 75  #Valor inicial en y (Donde se imprime el 0 del encabezado)

eje_y_inicial = eje_y   #Copia el valor inicial en y para en el caso de necesitar transiciones epsilon
separacion_x = 75   #Número de pixeles de separación entre elementos sobre el eje x
separacion_y = 30   #Número de pixeles de separación entre elementos sobre el eje y
estados, transiciones = (1, 2)
entradas = []
text_var = []
automata = {}   #Automata de entrada
estados_nombres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ya_epsilon = 0
automata_minimizado = {}
finales = []
estado_inicial = ""

def nuevo_estado():
    global estados
    global eje_y    
    nuevo_estado = estados_nombres[estados]       
    etiqueta_nuevo_estado = Label(text=nuevo_estado)
    etiqueta_nuevo_estado.place(x=eje_x-separacion_x+30, y=eje_y)    
    entradas.append([])
    text_var.append([])
    text_var[estados].append(StringVar())    
    entradas[estados].append(Entry(window, textvariable=text_var[estados][0], width=7))
    entradas[estados][0].place(x=eje_x, y=eje_y)
    text_var[estados].append(StringVar())
    entradas[estados].append(Entry(window, textvariable=text_var[estados][1], width=7))
    entradas[estados][1].place(x=eje_x+separacion_x, y=eje_y)
    if ya_epsilon == 1:
        text_var[estados].append(StringVar())
        entradas[estados].append(Entry(window, textvariable=text_var[estados][2], width=7))
        entradas[estados][2].place(x=eje_x+(separacion_x*2), y=eje_y)
    eje_y = eje_y + separacion_y        
    estados += 1  

def agregar_epsilon():
    global ya_epsilon
    global transiciones
    if ya_epsilon == 0:
        ya_epsilon = 1
        transiciones = 3
        #Añadir encabezado
        etiqueta_epsilon = Label(text="Eps")
        global eje_y_inicial
        etiqueta_epsilon.place(x=eje_x + (separacion_x*2), y=eje_y_inicial)
        for idx in range(estados):
            #entradas[idx].append([])
            text_var[idx].append(StringVar())
            entradas[idx].append(Entry(window, textvariable=text_var[idx][2], width=7))
            entradas[idx][2].place(x=eje_x + (separacion_x*2), y=eje_y_inicial+separacion_y)
            eje_y_inicial = eje_y_inicial+separacion_y

def minimizar():    
    global automata   
    global automata_minimizado
    global finales
    global estado_inicial

    estado_inicial = entrada_inicial.get()
    estado_final = entrada_final.get() 

    for estado in range(estados):
        automata[estados_nombres[estado]] = {}
        automata[estados_nombres[estado]]['0'] = list(text_var[estado][0].get())
        if automata[estados_nombres[estado]]['0'] == []: automata[estados_nombres[estado]]['0'] = list('N')
        automata[estados_nombres[estado]]['1'] = list(text_var[estado][1].get())
        if automata[estados_nombres[estado]]['1'] == []: automata[estados_nombres[estado]]['1'] = list('N')
        if ya_epsilon: 
            automata[estados_nombres[estado]]['Eps'] = list(text_var[estado][2].get())
            if automata[estados_nombres[estado]]['Eps'] == []: automata[estados_nombres[estado]]['Eps'] = list('N')    
    
    print('\n')
    print("AUTOMATA INICIAL: \n", automata)
    if ya_epsilon == 1: 
        
        print('\n')
        print("Automata con transiciones epsilon: \n")
        automata_sin_epsilon = afn_epsilon_afn.remover_epsilon(automata)
        print(automata_sin_epsilon)
        automata_formateado = afn_to_afd.encontrar_transiciones(automata_sin_epsilon, estado_inicial, estado_final)
        automata_minimizado, finales = afd_minimization.minimizer(automata_formateado, list(estado_final))
    else: 
        print('\n')
        print("Automata sin transiciones epsilon: \n")
        automata_formateado = afn_to_afd.encontrar_transiciones(automata, estado_inicial, estado_final)
        automata_minimizado, finales = afd_minimization.minimizer(automata_formateado, list(estado_final))

    
    print('\n')
    print("AUTOMATA MINIMIZADO: \n", automata_minimizado)
    print("FINALES:\n", finales)
    #print(automata)   

    print('\n') 

def result():
    global automata_minimizado
    global finales
    global estado_inicial

    newwindow = Tk()
    newwindow.title("Minimización")
    newwindow.geometry("600x200")  #Anchura x altura
    newwindow.resizable(False, False)

    h = Scrollbar(newwindow, orient='vertical')
    h.pack(side = BOTTOM, fill = X) 
    v = Scrollbar(newwindow)
    v.pack(side = RIGHT, fill = Y)

    # Procesa la infromacion para crear automata minimizado:
    minimizar()

    t = Text(newwindow, width = 15, height = 15, wrap = NONE, xscrollcommand = h.set, yscrollcommand = v.set) 

    t.insert(END,"ESTADO INICIAL: ")
    t.insert(END, estado_inicial)
    t.insert(END, "\n")
    t.insert(END, "ESTADOS FINALES: ")
    t.insert(END, finales)
    t.insert(END, "\n")
    t.insert(END,"AUTOMATA MINIMIZADO: \n")

    # Creamos str para agregar a la caja de texto:
    for estados in automata_minimizado.keys():
        cadena = estados + ':{ '
        for transiciones in automata_minimizado[estados].keys():
            cadena = cadena + transiciones + ':' + automata_minimizado[estados][transiciones] + ' '
        cadena = cadena + "} \n"
        t.insert(END, cadena)
    
    

    t.pack(side=TOP, fill=X) 
    h.config(command=t.xview) 
    v.config(command=t.yview) 
    newwindow.mainloop() 


#def cerrar_ventana():
#    newwindow.destroy()



#? Formato de la ventana ________________________________________________________________________________________________________________________________

#El siguiente pedazo de código es feo como pegarle a un bebé y por las premuras del tiempo no podremos hacerlo más estético, pero funciona (espero)
window = Tk()
window.title("Minimización de Automatas")
window.geometry("600x400")  #Anchura x altura
window.resizable(False, False)

etiqueta_encabezado = Label(font='Helvetica 13 bold', text=
'''Minimizador de Automatas
finitos deterministas (AFD)
y no detemrinistas (AFND)''')
etiqueta_encabezado.place(x=40, y=50)
#etiqueta_encabezado.pack()

etiqueta_indicaciones = Label(font='Helvetica 10', text=
'''Sólamente se aceptan autómatas
que reconocen el alfabeto {0,1}''')
etiqueta_indicaciones.place(x=40, y=110)
#etiqueta_indicaciones.pack()


etiqueta_inicial = Label(text="E. Inicial")
etiqueta_inicial.place(x=40, y=170)
entrada_inicial = Entry(window, textvariable=StringVar(), width=7)
entrada_inicial.place(x=40, y=200)

etiqueta_final = Label(text="E. Final")
etiqueta_final.place(x=130, y=170)
entrada_final = Entry(window, textvariable=StringVar(), width=7)
entrada_final.place(x=130, y=200)



#? Inputs _________________________________________________________________________________________________________________________________________________

etiqueta_0 = Label(text="0")
etiqueta_0.place(x=eje_x, y=eje_y)

etiqueta_1 = Label(text="1")
etiqueta_1.place(x=eje_x+separacion_x, y=eje_y)

etiqueta_A = Label(text="A")
etiqueta_A.place(x=eje_x-separacion_x+30, y=eje_y+separacion_y)

entradas.append([]) #Entradas A
text_var.append([]) #Valores A
text_var[0].append(StringVar())
entradas[0].append(Entry(window, textvariable=text_var[0][0], width=7))
entradas[0][0].place(x=eje_x, y=eje_y+separacion_y)
text_var[0].append(StringVar())
entradas[0].append(Entry(window, textvariable=text_var[0][1], width=7))
entradas[0][1].place(x=eje_x+separacion_x, y=eje_y+separacion_y)
eje_y = eje_y + (separacion_y*2)



#? Botones ______________________________________________________________________________________________________________________________________________

boton_crear_estado = Button(window, text="Añadir Estado", width=15, command=nuevo_estado)
boton_crear_estado.place(x=40, y=255)

boton_epsilon = Button(window, text="Añadir Epsilon", width=15, command=agregar_epsilon)
boton_epsilon.place(x=40, y=285)

boton_minimizar = Button(window, text="Minimizar", width=15, command=result)
boton_minimizar.place(x=40, y=330)


#? Fin _________________________________________________________________________________________________________________________________________________

window.mainloop()