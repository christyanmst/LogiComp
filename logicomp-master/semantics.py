"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """
import ttg
from ctypes import Union
from formula import *
from functions import atoms

def aux_truth_value(formula):
    dicionario ={}
    for x in atoms(formula):
        print("\nATÔMICA: ",x)
        interpretation = eval(input('Digite uma valoração para essa atômica, True ou False:\n'))
        dicionario[x]= interpretation
    print(dicionario)
    return dicionario
    
def truth_value(formula):
    dicionario = aux_truth_value(formula)
    print(formula)
    for atom, value in dicionario.items():
        formula = str(formula).replace(str(atom), str(value))
    formula = str(formula).replace('∧', ' and ').replace('∨',' or ').replace('¬',' not ')
    print(formula)
    print(eval(formula))

def satisfiability_brute_force(formula):
    table=truth_table(formula)
    print(table)
    if table.valuation() == 'Contingency':
        print("A Fórmula é satisfatível")
    if table.valuation() == 'Tautology':
        print("A Fórmula é Válida")
    if table.valuation() == 'Contradiction':
        print("A Fórmula é insatisfatível")


def is_logical_consequence(premises, conclusion):  # function TT-Entails? in the book AIMA.
    """Returns True if the conclusion is a logical consequence of the set of premises. Otherwise, it returns False."""
    pass
    # ======== YOUR CODE HERE ========


def is_logical_equivalence(formula1, formula2):
    """Checks whether formula1 and formula2 are logically equivalent."""
    pass
    # ======== YOUR CODE HERE ========


def is_valid(formula):
    table=truth_table(formula)
    if table.valuation() == 'Tautology':
        return True 
    else:
        return False
    # ======== YOUR CODE HERE ========

def truth_table(formula):
    strFormula = str(formula).replace('∧', ' and ').replace('∨',' or ').replace('¬',' not ')
    table = ttg.Truths(list(atoms(formula)),[strFormula])
    return table

