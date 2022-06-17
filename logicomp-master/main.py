"""You can test your functions in this module as in the following code: """
from formula import *
from functions import *
from semantics import *
from restriction import *


formula1 = Atom('p')  # p
formula2 = Or(Atom('q'), Atom('p'))  # q ^ p
formula3 = And(formula1, formula2)  # (p /\ q)
formula4 = Or(Not(Atom('p')), Atom('s'))  # (¬p /\ s)
formula5 = Not(And(Atom('p'), Atom('s')))  # (¬(p /\ s))
formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))  # ((¬(p /\ s)) v q)

formula7 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Atom('r')))  # ((¬(p /\ s)) -> (q /\ r))
formula7v2 = Or(Not(Not(And(Atom('p'), Atom('s')))), And(Atom('q'), Atom('r'))) 

formula8 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Not(And(Atom('p'), Atom('s'))))) # ((¬(p /\ s)) -> (q /\ (¬(p /\ s))))
formula8v2 = Or(Not(Not(And(Atom('p'), Atom('s')))), And(Atom('q'), Not(And(Atom('p'), Atom('s')))))

formula9 = Implies(Atom('l'),Atom('m'))
formula9v2 = Or(Not(Atom('l')),Atom('m'))

formula10 = And(Implies(Atom('l'),Atom('m')),Implies(Atom('x'),Atom('z')))
formula10v2 = And(Or(Not(Atom('l')),Atom('m')),Or(Not(Atom('x')),Atom('z')))

formula11 = And(Atom('p'), Not(Atom('p')))
formula12 = Or(Atom('p'), Not(Atom('p')))

#PROJETO
import csv
from pathlib import Path
valoracao=[]
linhas=0
atributos=[]
with open (Path(__file__).parent /'arquivos_pacientes/column_bin_5a_3p.csv') as teste:
    ler = csv.reader(teste)

    for dado in ler:
        if linhas == 0:
            atributos=dado
            linhas+=1; 
        
        else: 
            valoracao.append(dado)
            linhas+=1

    qtdPacientes=len(valoracao)
#Conferindo dados do arquivo csv lido.
print('Linhas:',linhas, '\nAtributos:',atributos, '\nValoracao:',valoracao,'\nPacientes:',qtdPacientes,'\nQuantidade de atributos:', len(atributos)-1)

m=4
#CHAMANDO AS RESTRIÇÕES
rest1 = restricao1(m, atributos)
rest2 = restricao2(m, atributos)
rest3 = restricao3(m, atributos)
rest4 = restricao4(m, atributos)
rest5 = restricao5(m, qtdPacientes, valoracao)


print('\nRESTRIÇÃO 2:\n',rest2)
print('\nRESTRIÇÃO 5:\n',rest5)

