def maximo_comun_divisor(x, y):
    temp = 0
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x


def minimo_comun_multiplo(x, y):
    
    return (x * y) // maximo_comun_divisor(x, y)

print(minimo_comun_multiplo(5, 2))
    