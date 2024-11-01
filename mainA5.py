def is_square(x):
    if x < 0:
        return False
    root = int(x**0.5)
    return root * root == x 

def is_perfect_square_trinomial(a, b, c):

    if not is_square(a):
        return False
    if not is_square(c):
        return False

    sqrt_a = int(a**0.5)
    sqrt_c = int(c**0.5)

    expected_b = 2 * sqrt_a * sqrt_c
    return b == expected_b



degree = int(input(f"Qual o grau do polinomio: "))
polynomial = []
for j in range(degree+1):
    coefficient = float(input(f"Coeficiente nº{j}: "))
    polynomial.append(coefficient)

#polynomial = polynomial[::-1]

mdc = polynomial[0]  # Começar com o primeiro número
for num in polynomial[1:]:
    mdc = abs(mdc)  # Garantir que a seja positivo
    num = abs(num)  # Garantir que b seja positivo
    while num != 0:
        mdc, num = num, mdc % num  # Troca a e b


#Primeira
result = f"{mdc}*("
for i in range(len(polynomial)):
    if polynomial[i]/mdc > 0 and i != 0:
        result += f"+"
    result += f"{polynomial[i]/mdc}"
    if i != len(polynomial): 
        result += f"x**{i} "
    elif i != 0:
        result += f" " 

print(result + ")")

#Trinômio quadrado perfeito

print(f"({polynomial[-1]**0.5}x + {polynomial[0]})²")




