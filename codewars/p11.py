#Debugging para que retorne siempra la clave como: key, y el valor sea el asignado en el argumento de la función.
def wrap(value):
    return locals()
print(wrap(True))