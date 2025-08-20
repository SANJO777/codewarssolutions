#Comprensi�n del Problema: #no usar la funci�n input() porque es para codewars. Por ende, usamos el argumento como valor de entrada.

#Entrada:

#input de la velocidad constante y positiva en cent�metros por segundos (o sobre segundos).

#Salida:

#Retornar el tiempo en segundos que tarda ese p�talo en llegar al suelo desde la misma rama. Tipo de dato: positivo, y en segundos.

#Asimismo, retornar el dato booleano: 0 (false), que significa que el dato ingresado en el input NO es positivo. 
#Por ende, usar la estructura de control: IF/ELSE, para los dos casos: input adecuado y retornar la velocidad en segundos del p�talo. 
#Segundo caso, input no positivo y retornar 0 (false), que significa que el dato NO es positivo 
#(tengo 2 expresiones l�gicas de condici�n en mi estructura de control y modelo matem�tico, que haya la velocidad en segundos de la ca�da en cent�metros por segundos de un p�talo que cae desde una rama hasta tocar el suelo.

def sakura_fall(v):
    if v <= 0:#Uso if para comprobar que la velocidad NO puede ser un n�mero no positivo. Es decir, menor o igual que cero hacia los negativos. Ya que, si lo cumple retornar� 0 para decir eso y por ende, no continuar porque si continua va a dividir por 0 y trodo n�mero divido por cero es indeterminable.
        return 0 
    else: #Else despu�s de que la condici�n anterior no fuera verdadera, ya que la velocidad no puede ser no positiva, s�lo puede ser no negativa. Es decir, desde 0 hasta los n�meros positivos.
        return 400 / v  #Asimismo, modelo matem�tico que haya la velocidad, con la distancia constante que siempre va a ser 400 para este ejercicio y v que es la velocidad dada como argumento.
    #La distancia constante la c�lcul� con la velocidad y tiempo del problema, ya que la distancia es la misma para todos los p�talos del ejercicio.
print(sakura_fall(10000)) #print y funci�n debugging para comprobrar el retorno adecuado de los valores.