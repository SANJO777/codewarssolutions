#Comprensión: borrar el primer carácter y último carácter de un string alphanumerico. Asimismo, la expresión lógica de condicón es: string > 3 para borrar.
def remove_char(s):
    return s[1:-1] #método slicing que crea una porción de una secuencia de datos con un rango específico. Asimismo, permite retornar una porción vacía si se deja a fuera todos los datos de una secuencia en el rango.

print(remove_char("S989@"))