def crear_diccionario(str_input):
    '''Recibe una cadena de caracteres y regresa un diccionario con las palabras y frecuencia'''
    lista = str_input.split()
    dicc = {}
    for i in lista:
        if i in dicc:
            dicc[i] += 1
        else:
            dicc[i] = 1
    return dicc


def counter_diccionario(dic):
    '''Recibe un diccionario y regresa una tupla'''
    str_frecuente = ''
    str_count = 0
    for keys, values in dic.items():
        if values > str_count: 
            str_count = values
            str_frecuente = keys
    return str_frecuente, str_count


cadena_entrada = input('Cadena de caracteres: ')
print(counter_diccionario(crear_diccionario(cadena_entrada)))
