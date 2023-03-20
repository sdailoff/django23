def crear_diccionario(str_input):
  '''Recibe una cadena de caracteres y regresa un diccionario con las palabras y frecuencia'''
  lista= str_input.split()
  dicc={}
  for i in lista:
    if i in dicc:
      dicc[i] +=1
    else:
      dicc[i] = 1
  return dicc
 
print(crear_diccionario(input('Cadena de caracteres: ')))