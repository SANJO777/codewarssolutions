#El método all tiene dos argumentos:

#- La secuencia.

#- La función de primera clase.

#Asimismo, retorna True si la función de primera clase retorna true para cada elemento de la secuencia. 
#Si retorna false en un sólo elemento, se detiene la verificación y retorna false. 
#Además, si la secuencia está vacía, debe retornar true porque no hay nada para hacer la verificación y, 
#por ende, nada va a fallar.

def _all(seq, fun):
    for element in seq:
        if not (fun(element)):
            return False
    return True

#EN CONCLUSIÓN, UN EJERCICIO MAL REDACTADO ME TOMÓ 4 HORAS PARA RESOLVERLO GRACIAS A GEMINI PARA ENTENDER QUE NO DEBO DE CREAR NADA.
#MÁS BIEN, DEBO DE USAR UNA ESTRUCTURA DE CONTROL DE COMPARACIÓN Y UN OPERADOR LÓGICO PARA COMPARAR LO CREADO (EXPRESIÓN)
#CON LOS ELEMENTOS DE MI BUCLE. AÚN ASÍ, APRENDÍ CONCEPTOS INTERESANTES, SOBRE: 
# FUNCIONES DE PRIMER NIVEL, RECURSIVIDAD Y CALLBACK (conocía los dos últimos, pero me quedaron ya me quedaron más claros que el agua).
# Asimismo, la iteración por indexación y la iteración directa.