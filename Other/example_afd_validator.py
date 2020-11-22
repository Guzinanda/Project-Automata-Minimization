
from automata.fa.dfa import DFA

dfa = DFA(  
    states          ={'q0','q1','q2'},
    
    input_symbols   ={'0','1'},
    
    transitions     ={
                      'q0':{'0':'q0','1':'q1'}, 
                      'q1':{'0':'q0','1':'q2'},
                      'q2':{'0':'q2','1':'q1'}},

    initial_state   = 'q0',

    final_states    ={'q1'}
)


# if accepted it will return the state or error:
print(dfa.read_input('01'))  # answer is "q1" 
#dfa.read_input('011') # answer is "error"

# states:
#print(dfa.read_input_stepwise('011'))

# returns true if it is correct or else false:
print(dfa.validate())


'''
# TEST __________________________________________________________________________

@ DFA which matches all binary strings ending in an odd number of 1's
  
  L = {1,01,001,111,1101...}

    
  Inputs           q0   q1   q2
          ________________________
            q0  |   0    1    -
  States    q1  |   0    -    1
            q2  |   -    1    0

'''