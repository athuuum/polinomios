from Objects.polynomial import *

qtd_polynomial = int(input("Quantos polinomios? "))

if qtd_polynomial > 1:

    #Definir polinômios
    polynomials = []
    for i in range(qtd_polynomial):
        degree = int(input(f"Qual o grau do polinomio nº{i+1}? "))
        coefficients = []
        for j in range(degree+1):
            coefficient = int(input(f"Coeficiente nº{j}: "))
            coefficients.append(coefficient)
        p = Polymonial(coefficients)
        polynomials.append(p)
    print(polynomials)



    for i in range(qtd_polynomial-1):
        polynomials[i].get_polynomial()
