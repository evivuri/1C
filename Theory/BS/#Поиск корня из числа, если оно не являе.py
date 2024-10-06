#Поиск корня из числа, если оно не является квадратом

x = float(input())
l = 0
r = x
for _ in range(100):
    m = (l + r) / 2
    if m**2 <= x:
        l = m
    else:
        r = m