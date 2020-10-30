import math


class Vector:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '( A:' + str(self.a) + ', B:' + str(self.b) + ' )'

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b:
            return True
        else:
            return False

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

    def lenght(self):
        return math.sqrt((self.a ** 2) + (self.b ** 2))

    def scalar(self, other):
        return (self.a * other.a) + (self.b * other.b)

    def eqZero(self, other):
        if self.scalar(other) == 0:
            return "Так"
        else:
            return "Ні"


# до обіду

x = Vector(0, 0)
y = Vector(1, 1)
print(x.__str__())
print('Довжина вектора:', x.lenght())
print(x.__add__(y))
print("Скалярний добуток:", x.scalar(y))
print("Перпендикулярні? :", x.eqZero(y))
