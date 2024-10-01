# объявление функции
def solve(a, b, c):
    D = b**2 - 4*a*c
    x1 = (-b+D**0.5)/(2*a)
    x2 = (-b-D**0.5)/(2*a)
    return float(x1), float(x2)

# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)