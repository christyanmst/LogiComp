"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """

from formula import *
from functions import atoms

def aux_truth_value(formula):
    dicionario ={}
    for x in atoms(formula):
        print("Atômica: ",x)
        interpretation = int(input('Digite uma valoração para essa atômica, 0 ou 1:\n'))
        dicionario[x]= bool(interpretation)
    return dicionario
    
def truth_value(formula):
    dicionario = aux_truth_value(formula)
    valores =[]
    valores.append(dicionario)
    for i in valores:
        for k, v in i.items():
            formula = str(formula).replace(str(k),str(v)).replace('∧', 'and').replace('∨','or').replace('¬','not ')
            #print(k +": "+str(v))
    return(eval(formula))

def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    """Returns True if formula is a logically valid (tautology). Otherwise, it returns False"""
    pass
    # ======== YOUR CODE HERE ========


def satisfiability_brute_force(formula):
    """Checks whether formula is satisfiable.
    In other words, if the input formula is satisfiable, it returns an interpretation that assigns true to the formula.
    Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


