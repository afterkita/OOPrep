class Fract:
    def __init__(self, verh, niz):
        self.verh = verh
        self.niz = niz

    def __str__(self):
        return str(self.verh)+'/'+str(self.niz)

    def decimal_fract(self):
        return round(self.verh / self.niz, 6)

    def __add__(self, other):
        new_verh = self.verh * other.niz + other.verh * self.niz
        new_niz = self.niz * other.niz
        degree = reduction(new_verh, new_niz)
        return Fract(new_verh//degree, new_niz//degree)

    def __sub__(self, other):
        new_verh = self.verh * other.niz - other.verh * self.niz
        new_niz = self.niz * other.niz
        degree = reduction(new_verh, new_niz)
        return Fract(new_verh//degree, new_niz//degree)

    def __mul__(self, other):
        new_verh = self.verh * other.verh
        new_niz = self.niz * other.niz
        degree = reduction(new_verh, new_niz)
        return Fract(new_verh//degree, new_niz//degree)

    def __floordiv__(self, other):
        new_verh = self.verh * other.niz
        new_niz = self.niz * other.verh
        degree = reduction(new_verh, new_niz)
        return Fract(new_verh//degree, new_niz//degree)
# Проверки
    def __ne__(self, other):
        return (self.verh * other.niz) != (other.verh * self.niz)

    def __eq__(self, other):
        return (self.verh * other.niz) == (other.verh * self.niz)

    def __gt__(self, other):
        return str(self.verh * other.niz) > str(other.verh * self.niz)

    def __lt__(self, other):
        return self.verh * other.niz < other.verh * self.niz


def reduction(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


if __name__ == "__main__":
    f1 = Fract(int(input()), int(input()))
    f2 = Fract(int(input()), int(input()))
    print(f" f1 = {f1}   f2 = {f2} ")
    print(f" Сумма = {f1 + f2}")
    print(f" Десятичная дробь от суммы = {(f1 + f2).decimal_fract()}")
    print(f" Разность = {f1 - f2}")
    print(f" Произведение = {f1 * f2}")
    print(f" Деление = {f1 // f2}")
    print(f" Функция f1 не равна f2 = {f1 != f2}")
    print(f" Функция f1 равна f2 = {f1 == f2}")
    print(f" Функция f1 больше f2 = {f1 > f2}")
    print(f" Функция f1 меньше f2 = {f1 < f2}")