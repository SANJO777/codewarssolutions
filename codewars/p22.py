#El m�todo all tiene dos argumentos:

#- La secuencia.

#- La funci�n de primera clase.

#Asimismo, retorna True si la funci�n de primera clase retorna true para cada elemento de la secuencia. 
#Si retorna false en un s�lo elemento, se detiene la verificaci�n y retorna false. 
#Adem�s, si la secuencia est� vac�a, debe retornar true porque no hay nada para hacer la verificaci�n y, 
#por ende, nada va a fallar.

def _all(seq, fun):
    for element in seq:
        if not (fun(element)):
            return False
    return True

#EN CONCLUSI�N, UN EJERCICIO MAL REDACTADO ME TOM� 4 HORAS PARA RESOLVERLO GRACIAS A GEMINI PARA ENTENDER QUE NO DEBO DE CREAR NADA.
#M�S BIEN, DEBO DE USAR UNA ESTRUCTURA DE CONTROL DE COMPARACI�N Y UN OPERADOR L�GICO PARA COMPARAR LO CREADO (EXPRESI�N)
#CON LOS ELEMENTOS DE MI BUCLE. A�N AS�, APREND� CONCEPTOS INTERESANTES, SOBRE: 
# FUNCIONES DE PRIMER NIVEL, RECURSIVIDAD Y CALLBACK (conoc�a los dos �ltimos, pero me quedaron ya me quedaron m�s claros que el agua).
# Asimismo, la iteraci�n por indexaci�n y la iteraci�n directa.