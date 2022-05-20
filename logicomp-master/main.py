"""You can test your functions in this module as in the following code: """
from formula import *
from functions import *
from semantics import *

formula1 = Atom('p')  # p
formula2 = And(Atom('q'), Atom('p'))  # q ^ p
formula3 = And(formula1, formula2)  # (p /\ q)
formula4 = Or(Not(Atom('p')), Atom('s'))  # (¬p /\ s)
formula5 = Not(And(Atom('p'), Atom('s')))  # (¬(p /\ s))
formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))  # ((¬(p /\ s)) v q)
formula7 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Atom('r')))  # ((¬(p /\ s)) -> (q /\ r))
formula8 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Not(And(Atom('p'), Atom('s'))))) # ((¬(p /\ s)) -> (q /\ (¬(p /\ s))))
formula9 = Implies(Atom('l'),Atom('m'))
# print(number_of_connectives(formula5))
# print(formula1 == formula3)
# print(formula1 == formula2)
# print(formula3 == And(Atom('p'), Atom('q')))

# print('formula1:', formula1)
# print('formula2:', formula2)
# print('formula3:', formula3)
# print('formula4:', formula4)
# print('formula5:', formula5)
# print('formula6:', formula6)
# print('formula7:', formula7)
# print('formula8:', formula8)

# print('length of formula1:', length(formula1))
# print('length of formula3:', length(formula3))

# print('length of formula7:', length(formula7))

# print('subformulas of formula7:')
# print(subformulas(formula7))
# for subformula in subformulas(formula6):
#     print(subformula)
# ((¬(p /\ s)) v q)

# print('length of formula8:', length(formula8))
# print('subformulas of formula8:')
# for subformula in subformulas(formula8):
#     print(subformula)

# testando o Atoms
# print("Fórmulas atômicas: ", atoms(formula1))

# # testando number of atoms
# print("Quantidade de fórmulas atômicas: ",number_of_atoms(formula1))

# testando is_literal
# print(is_literal(formula5))

# #  we have shown in class that for all formula A, len(subformulas(A)) <= length(A):
# # for example, for formula8:
# print('number of subformulas of formula8:', len(subformulas(formula8)))
# print('len(subformulas(formula8)) <= length(formula8):', len(subformulas(formula8)) <= length(formula8))

# print(formula9)
# formula9 = str(formula9).replace("→",'**')
# print(formula9[::-1].replace(")"," ").replace("(", " ").replace(""))

# print( False & True ** True)
# print(truth_value(formula3))

# print(is_clause(formula4))
# print(formula4)

# formula24 = Implies(Atom('True'), Atom('False'))  # (¬p /\ s)
# print(formula24)
# print(replace_truth_value(formula24))

print('\ntestando substitution escrevendo a fórmula:')
# formula 2 = q ^ p
print(substitution(formula2, Atom('q'), Atom('zz')))

print('\nou pode passar uma variável, como por exemplo:')
# formula 2 = q ^ p
old_sub= Atom('q')
new_sub= Atom('zz')
print(substitution(formula2,old_sub, new_sub ))