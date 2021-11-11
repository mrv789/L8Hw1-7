class ComplexNumber:
    def __init__(self, a, b,):
        self.a = a
        self.b = b

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


z_1 = ComplexNumber(4, 9)
z_2 = ComplexNumber(6, -4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)