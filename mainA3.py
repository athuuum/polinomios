from Objects.operations import *
from Objects.polynomial import *


qtd_polynomial = int(input("Quantos polinômios? "))

if qtd_polynomial > 1:

    #Definir polinômios
    polynomials = []
    for i in range(qtd_polynomial):
        degree = int(input(f"Qual o grau do polinomio nº{i+1}? "))
        coefficients = []
        for j in range(degree+1):
            coefficient = int(input(f"Coeficiente nº{j}: "))
            coefficients.append(coefficient)
        poly = Polynomial(coefficients)
        polynomials.append(poly)

    #Subtrair
    result = polynomials[0]
    for poly in polynomials[1:]:
        result = multiplication(result, poly)

    print("Multiplicação: ", result.get())

