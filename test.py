# Função para multiplicar dois polinômios
def multiply_polynomials(poly1, poly2):
    # O grau do polinômio resultante é a soma dos graus dos dois polinômios
    result_degree = len(poly1) + len(poly2) - 2
    result = [0] * (result_degree + 1)

    # Multiplicação de polinômios
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]

    return result

# Entrada do usuário
qtd_polynomial = int(input("Quantos polinômios? "))

if qtd_polynomial > 1:
    # Definir polinômios
    polynomials = []
    for i in range(qtd_polynomial):
        degree = int(input(f"Qual o grau do polinômio nº {i+1}? "))
        coefficients = []
        for j in range(degree + 1):
            coefficient = int(input(f"Coeficiente nº {j}: "))
            coefficients.append(coefficient)
        polynomials.append(coefficients)

    print("Polinômios inseridos:", polynomials)

    # Multiplicação de todos os polinômios
    result = polynomials[0]  # Começamos com o primeiro polinômio
    for i in range(1, len(polynomials)):
        result = multiply_polynomials(result, polynomials[i])  # Multiplica o resultado atual pelo próximo polinômio

    print("Resultado da multiplicação dos polinômios:", result)