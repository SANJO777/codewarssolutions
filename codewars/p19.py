#Retornar la cadena ingresada invirtiendo su orden. Es decir, empiece desde el final y termine en el principio. Asimismo, verificar que s�lo tenga espacios entre palabras y NO al principio y final.
def reverse_words(s): #Funci�n que recorta car�cteres y almacena en una lista, invierte el orden de la lista para que empiece desde el final hasta el principio y concatene para retornar una nueva cadena de texto con el orden de final hasta el principio (al revez).
    s = s.split() #split crea una lista con los car�cteres separados.
    s.reverse() #invierte el orden de la lista para que empiece de final hasta el principio.
    s = " ".join(s) #concatena la lista para crear un nuevo car�cter.
    return s
print(reverse_words("Hola, Mundo"))
print(reverse_words(" Hola, Mundo"))
print(reverse_words("Hola, Mundo "))
print(reverse_words("Chavales,notengoespacio"))