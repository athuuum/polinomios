
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
        polynomials.append(coefficients)
    print(polynomials)

    #Somar
    for i in range(len(polynomials)):
        if len(polynomials[i]) < 3:
            polynomials[i] += [0] * (3 - len(polynomials[i]))

    result = polynomials[0][:]
    for polynomial in polynomials:
        for i in range(3):
            result[i] -= polynomial[i]
        
    print("Resultado da soma dos polinômios:", result)







    

        
    
