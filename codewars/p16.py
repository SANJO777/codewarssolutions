#Comprensi�n: borrar el primer car�cter y �ltimo car�cter de un string alphanumerico. Asimismo, la expresi�n l�gica de condic�n es: string > 3 para borrar.
def remove_char(s):
    return s[1:-1] #m�todo slicing que crea una porci�n de una secuencia de datos con un rango espec�fico. Asimismo, permite retornar una porci�n vac�a si se deja a fuera todos los datos de una secuencia en el rango.

print(remove_char("S989@"))