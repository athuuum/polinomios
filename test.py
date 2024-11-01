# Função que implementa o algoritmo de Euclides para calcular o MDC de dois números
def mdc(a, b):
    a = abs(a)  # Garantir que a seja positivo
    b = abs(b)  # Garantir que b seja positivo
    while b != 0:
        a, b = b, a % b  # Troca a e b
    return a

# Função para calcular o MDC de uma lista de números
def mdc_lista(numeros):
    resultado = numeros[0]  # Começar com o primeiro número
    for num in numeros[1:]:
        resultado = mdc(resultado, num)  # Calcular o MDC com o próximo número
    return resultado

# Exemplo de uso
numeros = [4, 12]
resultado = mdc_lista(numeros)
print("O MDC é:", resultado)