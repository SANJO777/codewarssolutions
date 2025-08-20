#Comprensión del Problema: #no usar la función input() porque es para codewars. Por ende, usamos el argumento como valor de entrada.

#Entrada:

#input de la velocidad constante y positiva en centímetros por segundos (o sobre segundos).

#Salida:

#Retornar el tiempo en segundos que tarda ese pétalo en llegar al suelo desde la misma rama. Tipo de dato: positivo, y en segundos.

#Asimismo, retornar el dato booleano: 0 (false), que significa que el dato ingresado en el input NO es positivo. 
#Por ende, usar la estructura de control: IF/ELSE, para los dos casos: input adecuado y retornar la velocidad en segundos del pétalo. 
#Segundo caso, input no positivo y retornar 0 (false), que significa que el dato NO es positivo 
#(tengo 2 expresiones lógicas de condición en mi estructura de control y modelo matemático, que haya la velocidad en segundos de la caída en centímetros por segundos de un pétalo que cae desde una rama hasta tocar el suelo.

def sakura_fall(v):
    if v <= 0:#Uso if para comprobar que la velocidad NO puede ser un número no positivo. Es decir, menor o igual que cero hacia los negativos. Ya que, si lo cumple retornará 0 para decir eso y por ende, no continuar porque si continua va a dividir por 0 y trodo número divido por cero es indeterminable.
        return 0 
    else: #Else después de que la condición anterior no fuera verdadera, ya que la velocidad no puede ser no positiva, sólo puede ser no negativa. Es decir, desde 0 hasta los números positivos.
        return 400 / v  #Asimismo, modelo matemático que haya la velocidad, con la distancia constante que siempre va a ser 400 para este ejercicio y v que es la velocidad dada como argumento.
    #La distancia constante la cálculé con la velocidad y tiempo del problema, ya que la distancia es la misma para todos los pétalos del ejercicio.
print(sakura_fall(10000)) #print y función debugging para comprobrar el retorno adecuado de los valores.