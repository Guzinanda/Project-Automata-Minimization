
#? Algoritmo para remover las transiciones vacias del autómata ________________________________________
#Esto valida las transiciones vacías (inexistentes, no confundir con transiciones Epsilon)

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


def quitar_vacios(nfa):
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
