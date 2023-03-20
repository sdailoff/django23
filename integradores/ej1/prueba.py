def maximo_comun_divisor(x, y):
    temp = 0
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x

print(maximo_comun_divisor(5, 15))