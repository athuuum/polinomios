from Objects.polynomial import *

degree = int(input(f"Qual o grau do polinômio: "))
polynomial = None
coefficients = []
for j in range(degree+1):
    coefficient = float(input(f"x^{j}: "))
    coefficients.append(coefficient)

polynomial = Polymonial(coefficients)

print(polynomial.get())
print("""
      (1) Fator comum em evidência
      (2) Agrupamento
      (3) Trinômio quadrado perfeito
      (4) Diferença de dois quadrados
      (5) Soma de dois cubos
      (6) Diferença de dois cubos\n
""")

choice = int(input("Escolha: "))

if choice == 1:
    if polynomial.mdc == 1:
        print("O MDC é 1")
    else:
        # Criar uma nova lista de coeficientes divididos pelo MDC
        new_coeffs = [coeff / polynomial.mdc for coeff in polynomial.get()]
        print(new_coeffs)
        # Construir a expressão fatorada
        factorized = f"{polynomial.mdc} * ("
        for i, coeff in enumerate(new_coeffs[:-1]):
            factorized += f"{coeff}x^{degree-i} + "
        factorized += f"{new_coeffs[-1]})"
        print(factorized)
elif choice == 3:
    if polynomial.is_perfect_square_trinomial:
        coeffs = polynomial.get()
        print(f"({coeffs[-1]**0.5}x + {coeffs[0]**0.5})²")
    else:
        print("Não é um trinômio quadrado perfeito")

elif choice == 4:
    coeffs = polynomial.get()
    if degree == 2 and coeffs[0] > 0 and coeffs[2] > 0 and coeffs[1] == 0:
        a = coeffs[0] ** 0.5
        b = coeffs[2] ** 0.5
        print(f"({a}x - {b})({a}x + {b})")
    else:
        print("O polinômio não é uma diferença de dois quadrados")

        



