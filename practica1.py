# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 13:33:22 2020

@author: Antonio Ortiz
"""

"""
estados separados por coma
lenguaje aceptado (caracteres)
estado inicial
estado final
transiciones +
    estado inicio, letra, estado al que llega
    
Ejemplo: 
    0, 1, 2, 3
    a, b
    0
    2
    0, a, 0
    0, b, 0
    0, a, 1
    1, b, 2
    1, a, 3
    2, a, 3
    2, b, 3
    3, a, 3
    3, b, 3

"""
import numpy as np
#import scipy as sc

def get_file( file_name ):
    # file_name must be with extension
    file = open(file_name, encoding = 'utf-8')
    text = file.read()
    return text

def get_quintuple( file_content ):
    quintuple  = file_content.replace(" ", "").split('\n', 4)
    quintuple = np.array( quintuple )
    return quintuple

def get_states( quintuple ):
    states = np.array( quintuple[0].split(',') )
    return states

def get_symbols( quintuple ):
    symbols = np.array( quintuple[1].split(',') )
    return symbols

def get_initial_state( quintuple ):
    initial_state = np.array(quintuple[2].split())
    return initial_state

def get_final_state( quintuple ):
    final_state= np.array(quintuple[3].split())
    return final_state

def get_transition_function( quintuple ):
    transitions = quintuple[4].split('\n') 
    transition_function = np.array( [element.split(',') for element in transitions] )
    return transition_function

def get_dfa_roads(dfa):
    print(dfa['transition_function'])
    return dfa
    

if __name__ == '__main__':  
    # print(get_file('AF1.txt'))
    file_content = get_file('AF1.txt')
    quintuple = get_quintuple(file_content)
    #print (quintuple[4])
    states  =       get_states(quintuple)
    alphabet =      get_symbols(quintuple)
    initial_state = get_initial_state(quintuple)
    final_state =   get_final_state(quintuple)
    transition_function = get_transition_function(quintuple)
    #print(transition_function[0])
    # Deterministic Finite Automata
    dfa = {
        'states': states,
        'alphabet': alphabet,
        'initial_state': initial_state,
        'final_state': final_state,
        'transition_function': transition_function
    }
    roads = get_dfa_roads(dfa)