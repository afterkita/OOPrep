import sympy as sym
from sympy import *


class Data:
    def __init__(self, function, delta, point):
        self.function = function
        self.delta = delta
        self.point = point

    def __str__(self):
        return f"f(x) = {self.function} "

class Calc(Data):
    def __init__(self, function, delta, point):
        super().__init__(function, delta, point)
        self.f = lambdify(x, self.function)

    def Right(self):
        return round(sym.limit((self.f(x+self.delta) - self.f(x)) / self.delta, x, self.point, dir='+'), 5)

    def Left(self):
        return round(sym.limit((self.f(x+self.delta) - self.f(x)) / self.delta, x, self.point, dir='-'), 5)

    def Centre(self):
        return round(sym.limit((self.f(x+self.delta) - self.f(x)) / self.delta, x, self.point, dir='+-'), 5)

    def diff(self):
        return sym.diff(self.function, x)



if __name__ == '__main__':
    x = symbols('x')

    delta = 0.000000001
    function = (6*x)**4 + 45
    point = 2

    a = Calc(function, delta, point)
    #--------
    print(f"f'(x) = {a.diff()}")
    print(f"Проивзодная справа {a.Right()}")
    print(f"Проивзодная слева {a.Left()}")
    print(f"Проивзодная центральная {a.Centre()}")
