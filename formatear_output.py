
#? Algoritmo que formatea output a programa de Lalo _________________________________________________________________________________

def formatear_output(dfa):
    
    dfa_formateado = {}

    cambio = {'A':'s0','B':'s1','C':'s2','D':'s3','E':'s4','N':'s5'}


    #dfa = {'AB': {'0':'E','1':'BC'}
    for mkay in dfa:
    
        #TODO: Para transicion master
        # 'AB'  ->  'A', 'B'
        estados = list(mkay)

        # 'A', 'B'  ->  's0s1'
        kay_nuevo = ''
        for i in estados:
            kay_nuevo = kay_nuevo + cambio[str(i)]

    

        #TODO: Para transiciones pequeñas
        # mkay = 'A'
        # 'A' -> 'A'  &  'AB' -> 'A', 'B'
        estados0 = list(dfa[mkay]['0'])
        estados1 = list(dfa[mkay]['1'])

        transiciones0_nuevas = ''
        transiciones1_nuevas = ''

         # 'E' -> s4
        for i in estados0:
            transiciones0_nuevas = transiciones0_nuevas + cambio[str(i)]
        
        # 'B', 'C' -> 's1s2'
        for i in estados1:
            transiciones1_nuevas = transiciones1_nuevas + cambio[str(i)]


        # dfa_formateado = {'s0s1': {'0':'E','1':'BC'}
        dfa_formateado[kay_nuevo] = {'0':transiciones0_nuevas, '1':transiciones1_nuevas}


    return dfa_formateado
        



# TEST ________________________________________________________

#Input:
#dfa = {'A'   : {'0':'E'  ,   '1':'BC'},
#       'BC'  : {'0':'E'  ,   '1':'AD'}, 
#       'AD'  : {'0':'AE' ,   '1':'BC'}, 
#       'E'   : {'0':'N'  ,   '1':'N'}, 
#       'AE'  : {'0':'E'  ,   '1':'BC'}}

#Output:
#dfa_formateado = 
#      {'s0'    : {'0':'s4'  ,   '1':'s1s2'},
#       's1s2'  : {'0':'s4'  ,   '1':'s0s3'}, 
#       's0s3'  : {'0':'s0s4' ,  '1':'s1s2'}, 
#       's4'    : {'0':'s5'  ,   '1':'s5'}, 
#       's0s4'  : {'0':'s4'  ,   '1':'s1s2'}}
