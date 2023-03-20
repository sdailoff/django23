import ej1 as e

def minimo_comun_multiplo(x, y):    
    return (x * y) // e.maximo_comun_divisor(x, y)

print(minimo_comun_multiplo(5, 2))
    