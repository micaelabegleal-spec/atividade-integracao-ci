class Calculadora:

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b


calc = Calculadora()

print("2 + 3 =", calc.somar(2, 3))
print("5 - 2 =", calc.subtrair(5, 2))
