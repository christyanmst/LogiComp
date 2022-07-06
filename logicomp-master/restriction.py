from formula import *

def and_all_formulas(formulas):
    and_forms=[]
    for formula in formulas:
        if formula == formulas[0]:
            and_forms = formulas[0]
        else:
            and_forms = And(and_forms, formula)
    return and_forms

def or_all_forms(formulas):
    or_forms=[]
    for formula in formulas:
        if formula == formulas[0]:
            or_forms = formulas[0]
        else:
            or_forms = Or(or_forms, formula)
    return or_forms


def aux_atributo(atributo, regra, tipo):
    atributo_aux = Atom("%s,%s,%s" % (atributo, regra+1, tipo))
    return atributo_aux

def aux_regra(regra, n_pacientes):
    regra_aux = Atom("%s%s,%s" % ('C',regra+1,n_pacientes+1))
    return regra_aux

def restricao1(m, lista_atributos):
    formulas = []
    for regra in range(m):
        possibilidades = []

        for atributo in lista_atributos:
            if atributo != atributo[-1]:
                possibilidades.append(
                    Or(
                        Or(
                            And(
                                And(aux_atributo(atributo,regra,'p'), 
                                Not(aux_atributo(atributo,regra,'n'))),
                                Not(aux_atributo(atributo,regra,'s'))
                            ),
                            And(
                                And(aux_atributo(atributo,regra,'p'), 
                                aux_atributo(atributo,regra,'n')),
                                Not(aux_atributo(atributo,regra,'s'))
                            )
                        ),
                        And(
                                And(Not(aux_atributo(atributo,regra,'p')), 
                                Not(aux_atributo(atributo,regra,'n'))),
                                aux_atributo(atributo,regra,'s')
                        )
                    )
                )
        formulas.append(and_all_formulas(possibilidades))
    
    return and_all_formulas(formulas)

def restricao2(m, lista_atributos):
    formula  = [] 
    formula2 = []
    regra=0;
    while regra < m:
        for atributo in lista_atributos:
            if atributo !='P':
                formula.append(Not(aux_atributo(atributo, regra, 's')))
        formula2.append(or_all_forms(formula))
        regra+=1;
        formula = []
    return and_all_formulas(formula2)


def restricao3(m, lista_atributos, pacientes, valoracao):
    j=0
    regra=0
    formula2 = []
    while True:
        if j == pacientes:
            break
        if valoracao[j][-1] == '0':
            while True: 
                formula =[]
                if regra == m:
                    break;
                for atributo in lista_atributos:
                    if atributo != atributo[-1]:
                        if valoracao[j][lista_atributos.index(str(atributo))] == '1': 
                            formula.append(aux_atributo(atributo, regra, 'n'))
                        elif valoracao[j][lista_atributos.index(str(atributo))] == '0':
                            formula.append(aux_atributo(atributo, regra, 'p'))
                formula2.append(or_all_forms(formula))
                regra+=1
        j+=1;
    return and_all_formulas(formula2)

def restricao4(m, lista_atributos, pacientes, valoracao):
    formula2 = []
    j=0
    index_pacientes = len(lista_atributos) - 1
    while True:
        if j == pacientes:
            break
        if valoracao[j][-1] == '1':
            for regra in range(0, m):
                formula =[]     
                for index in range(index_pacientes):
                        if lista_atributos[index] != 'P':
                            if valoracao[j][index] == '1': 
                                formula.append(Or(Not(aux_atributo(str(lista_atributos[index]), regra, 'n')), Not(aux_regra(regra,j))))
                            elif valoracao[j][index] == '0':
                                formula.append(Or(Not(aux_atributo(str(lista_atributos[index]), regra, 'p')), Not(aux_regra(regra,j))))
                formula2.append(and_all_formulas(formula))
        j+=1
    return and_all_formulas(formula2)

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