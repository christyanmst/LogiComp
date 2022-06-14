"""The goal in this module is to define functions associated with the semantics of formulas in propositional logic. """
import ttg
from formula import *
from functions import atoms


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

def truth_table(formula):
    strFormula = str(formula).replace('∧', ' and ').replace('∨',' or ').replace('¬',' not ')
    return ttg.Truths(list(atoms(formula)),[strFormula])


def truth_value(formula, interpretation):
    dicionario = interpretation
    for atom, value in dicionario.items():
        formula = str(formula).replace(str(atom), str(value))
    formula = str(formula).replace('∧', ' and ').replace('∨',' or ').replace('¬',' not ')
    return eval(formula)

def satisfiability_brute_force(formula):
    interpretation = {}
    atomicas = atoms(formula)
    for atomica in atoms(formula):
        interpretation[atomica] = 0
    result = sat(formula, atomicas, interpretation)
    return(result)

def sat(formula, atomicas, valoracao):
    if len(atomicas) == 0:
        if truth_value(formula, valoracao):
            return valoracao
        else:
            return False

    atomica = atomicas.pop()
    interpretacao1 = valoracao.copy()
    interpretacao2 = valoracao.copy()
    interpretacao1[atomica] = True
    interpretacao2[atomica] = False

    interpretacao1_result = sat(formula, atomicas, interpretacao1)
    if interpretacao1_result != False:
        return interpretacao1_result
    else:
        return sat(formula, atomicas, interpretacao2)