from formula import *

def and_all_formulas(formulas):
    and_forms=[]
    for formula in formulas:
        if formula == formulas[0]:
            and_forms = formulas[0]
        else:
            and_forms = And(and_forms, formula)
    return and_forms

def aux_atributo(atributo, regra, tipo):
    atributo_aux = Atom("%s,%s,%s" % (atributo, regra+1, tipo))
    return atributo_aux

def restricao1(m, lista_atributos):
    formula1 = []
    formula2 = []
    formula3 = []

    return;

def restricao2(m, lista_atributos):
    return;

def restricao3(m, lista_atributos):
    return;

def restricao4(m, lista_atributos):
    return;

def restricao5(m, pacientes, valoracao):
    formula  = [] 
    formula2 = []
    j=0;
    regra=0
    while j < pacientes:
        if valoracao[j][-1] =='1':
            formula = aux_r5(regra,m,j)
            formula2.append(or_all_forms(formula))
        j+=1  
    return  and_all_formulas(formula2)

def aux_r5(regra, m, pacientes):
    formula = []
    regra=0
    while regra < m:
        formula.append(aux_regra(regra,pacientes))
        regra+=1
    return formula
