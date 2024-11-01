class Polymonial():
    def __init__(self, coefficients):
        self.coefficients = coefficients
        mdc = coefficients[0]  # Começar com o primeiro número
        for num in coefficients[1:]:
            mdc = abs(mdc)  # Garantir que a seja positivo
            num = abs(num)  # Garantir que b seja positivo
            while num != 0:
                mdc, num = num, mdc % num  # Troca a e b
        self.mdc = mdc

        def is_square(x):
            if x < 0:
                return False
            root = int(x**0.5)
            return root * root == x 
            
        self.is_perfect_square_trinomial = False
        if not is_square(self.coefficients[0]):
            self.is_perfect_square_trinomial = False
        elif not is_square(self.coefficients[-1]):
            self.is_perfect_square_trinomial = False
        elif self.get_degree() != 2:
            self.is_perfect_square_trinomial = False
        else:
            sqrt_a = int(self.coefficients[0]**0.5)
            sqrt_c = int(self.coefficients[-1]**0.5)
            expected_b = 2 * sqrt_a * sqrt_c
            self.is_perfect_square_trinomial = self.coefficients[1] == expected_b


    def get(self):
        return self.coefficients
    
    def get_degree(self):
        return len(self.coefficients)-1