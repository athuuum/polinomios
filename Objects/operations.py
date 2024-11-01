from Objects.polynomial import *

def match(p1, p2):
    max_degree = max(len(p1), len(p2))
    p1 = p1 + [0] * (max_degree - len(p1))
    p2 = p2 + [0] * (max_degree - len(p2))

    return p1, p2

def sum(p1: Polynomial, p2: Polynomial):
    c1 = p1.get()
    c2 = p2.get()
    c1, c2 = match(c1, c2)
    result = [0] * len(c1)
    for i in range(len(c1)):
        result[i] = c1[i] + c2[i]

    return Polynomial(result)

def subtraction(p1: Polynomial, p2: Polynomial):
    c1 = p1.get()
    c2 = p2.get()
    c1, c2 = match(c1, c2)
    result = [0] * len(c1)
    for i in range(len(c1)):
        result[i] = c1[i] - c2[i]

    return Polynomial(result)

def multiplication(p1: Polynomial, p2: Polynomial):
    c1 = p1.get()  
    c2 = p2.get() 
    
    result_degree = p1.get_degree() + p2.get_degree() 
    result = [0] * (result_degree + 1)  
    
    for i in range(len(c1)):
        for j in range(len(c2)):
            result[i + j] += c1[i] * c2[j]
    
    return Polynomial(result)




def division(p1: Polynomial, p2: Polynomial):
    c1 = p1.get()
    c2 = p2.get() 

    if len(c1) < len(c2):
        return Polynomial([0]), p1
    
    result_degree = len(c1) - len(c2)
    quotient = [0] * (result_degree + 1)
    remainder = Polynomial(c1)  

    for i in range(result_degree + 1):
        quotient[-(i+1)] = remainder.get()[-1] / c2[-1]
        q = Polynomial([0] * (result_degree - i) + [quotient[-(i+1)]])
        remainder = subtraction(remainder, multiplication(q, p2))

        if remainder.get()[-1] == 0:
            remainder = Polynomial(remainder.get()[:-1])

    return Polynomial(quotient), remainder

def division_recursive(p1: Polynomial, p2: Polynomial):
    c1 = p1.get() 
    c2 = p2.get() 

    if len(c1) < len(c2):
        return Polynomial([0]), p1

    leading_coeff = c1[-1] / c2[-1]
    result_degree = len(c1) - len(c2)
    quof = Polynomial([0] * result_degree + [leading_coeff])
    remainder = subtraction(p1, multiplication(quof, p2))
    
    if remainder.get()[-1] == 0:
        remainder = Polynomial(remainder.get()[:-1])
    partial_quotient, remainder = division_recursive(remainder, p2)
    
    final_quotient = sum(quof, partial_quotient)
    print('TERMO', quof.get(), '\nPARTIAL', partial_quotient.get(),'\nFINAL',final_quotient.get(),'\n------')
    
    return quof, remainder

        
'''



    # Inicializa o quociente e o resto
    result_degree = len(c1) - len(c2)
    quotient = [0] * (result_degree + 1)
    remainder = c1.copy()  # Resto começa como o dividendo

    # Algoritmo de divisão
    for i in range(result_degree + 1):
        # Coeficiente do quociente na posição i
        quotient[i] = remainder[i] / c2[-1]  # Divide pelo coeficiente líder do divisor
        
        # Subtrai o múltiplo do divisor do resto
        for j in range(len(c2)):
            remainder[i + j] -= quotient[i] * c2[j]

    # Remove os zeros à esquerda do resto
    while len(remainder) > 0 and remainder[-1] == 0:
        remainder.pop()

    return Polynomial(quotient), Polynomial(remainder)'''


    


