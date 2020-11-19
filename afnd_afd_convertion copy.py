
# Convertir NFA a DFA

import pandas as pd

# ////////////////////////////////////////////////////////////////////////////////////////////////

# Taking NFA from User:
nfa = {'A': {'0':['A'],           '1':['A','B']}, 
       'B': {'0':['A','B','C'],   '1':['A','B']}, 
       'C': {'0':['A','B','C'],   '1':['A','B','D']}, 
       'D': {'0':['A','B','C'],   '1':['A','B']}}

# Total no. of states: A -> B -> C -> D
n = 4
# Total no. of transitions/paths: 0,1                           
t = 2

# Initial state of NFA:
nfa_initial_state = ['A']
# Final state of NFA:
nfa_final_state = ['D']  



# ////////////////////////////////////////////////////////////////////////////////////////////////

# Calculates DFA from NFA:
dfa = {}

new_states_list = []                                                    # holds all the new states created in dfa

keys_list = list(list(nfa.keys())[0])                                   # conatins all the states in nfa plus the states created in dfa are also appended further
path_list = list(nfa[keys_list[0]].keys())                              # list of all the paths eg: [a,b] or [0,1]


# Computing first row of DFA transition table:
dfa[keys_list[0]] = {}                                                  # creating a nested dictionary in dfa 
for y in range(t):
    var = "".join(nfa[keys_list[0]][path_list[y]])                      # creating a single string from all the elements of the list which is a new state
    dfa[keys_list[0]][path_list[y]] = var                               # assigning the state in DFA table
    if var not in keys_list:                                            # if the state is newly created 
        new_states_list.append(var)                                     # then append it to the new_states_list
        keys_list.append(var)                                           # as well as to the keys_list which contains all the states

# Computing the other rows of DFA transition table:
while len(new_states_list) != 0:                                        # consition is true only if the new_states_list is not empty
    dfa[new_states_list[0]] = {}                                        # taking the first element of the new_states_list and examining it
    
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []                                                   # creating a temporay list
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]        # taking the union of the states
            s = ""
            s = s.join(temp)                                            # creating a single string(new state) from all the elements of the list
            if s not in keys_list:                                      # if the state is newly created
                new_states_list.append(s)                               # then append it to the new_states_list
                keys_list.append(s)                                     # as well as to the keys_list which contains all the states
            dfa[new_states_list[0]][path_list[i]] = s                   # assigning the new state in the DFA table
        
    new_states_list.remove(new_states_list[0])                          # Removing the first element in the new_states_list


# ////////////////////////////////////////////////////////////////////////////////////////////////

# Printing the DFA created
print("\nPrinting DFA :- ")
print(dfa)                                                     

# Printing the DFA table created
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())

#Printing final states of DFA
dfa_states_list = list(dfa.keys())
dfa_final_states = []
for x in dfa_states_list:
    for i in x:
        if i in nfa_final_state:
            dfa_final_states.append(x)
            break  
print("\nFinal states of the DFA are : ",dfa_final_states)

