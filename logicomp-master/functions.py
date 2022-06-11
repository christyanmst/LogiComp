"""The goal in this module is to define functions that take a formula as input and
do some computation on its syntactic structure. """


from re import T
from formula import *


def length(formula):
    """Determines the length of a formula in propositional logic."""
    if isinstance(formula, Atom):
        return 1
    if isinstance(formula, Not):
        return length(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return length(formula.left) + length(formula.right) + 1


def subformulas(formula):
    """Returns the set of all subformulas of a formula.

    For example, observe the piece of code below.

    my_formula = Implies(Atom('p'), Or(Atom('p'), Atom('s')))
    for subformula in subformulas(my_formula):
        print(subformula)

    This piece of code prints p, s, (p v s), (p → (p v s))
    (Note that there is no repetition of p)
    """

    if isinstance(formula, Atom):
        return {formula}
    if isinstance(formula, Not):
        return {formula}.union(subformulas(formula.inner))
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        sub1 = subformulas(formula.left)
        sub2 = subformulas(formula.right)
        return {formula}.union(sub1).union(sub2)

#  we have shown in class that, for all formula A, len(subformulas(A)) <= length(A).


def atoms(formula):
    formula = str(formula).replace(u"\u2192", '').replace(u"\u00ac", '').replace(u"\u2227", '').replace(u"\u2228",'').replace('(', '').replace(')', '').replace('  ', ',')
    conjAtoms = set()

    for i in formula.split(','):
        conjAtoms.add(i)

    return conjAtoms

def number_of_atoms(formula):
    formula = str(formula).replace(u"\u2192", '').replace(u"\u00ac", '').replace(u"\u2227", '').replace(u"\u2228",'').replace('(', '').replace(')', '').replace('  ', ',')
    conjAtoms = set()

    for i in formula.split(','):
        conjAtoms.add(i)

    return len(conjAtoms)

def number_of_connectives(formula):
    if isinstance(formula, Atom):
        return 0
    if isinstance(formula, Not):
        return number_of_connectives(formula.inner) + 1
    if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
        return number_of_connectives(formula.left) + number_of_connectives(formula.right) + 1

def is_literal(formula):
    if (length(formula) <=2):
        if isinstance(formula, Atom):
            return True
        if isinstance(formula, Not):
            return  True
    else:
        return False

def substitution(formula, old_subformula, new_subformula):
    if (old_subformula!=new_subformula):
        formula = str(formula).replace(str(old_subformula),str(new_subformula))
        return formula
    else:
        return formula

def is_clause(formula):
    if isinstance(formula, Atom):
        return False
    if isinstance(formula, Not):
        return False
    if isinstance(formula, Or):
        return True
    if isinstance(formula, Implies) or isinstance(formula, And):
        return False

def is_negation_normal_form(formula):
    """Returns True if formula is in negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_cnf(formula):
    """Returns True if formula is in conjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_term(formula):
    """Returns True if formula is a term. It returns False, otherwise"""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_dnf(formula):
    """Returns True if formula is in disjunctive normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========


def is_decomposable_negation_normal_form(formula):
    """Returns True if formula is in decomposable negation normal form.
    Returns False, otherwise."""
    pass  # ======== REMOVE THIS LINE AND INSERT YOUR CODE HERE ========

def arquivo_csv(arquivo):
    import csv
    with open(arquivo,'r') as dados:
        leitor=csv.reader(dados)
        for linha in leitor:
            print (linha)