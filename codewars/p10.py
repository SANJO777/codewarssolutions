#La sumatoria es sumar una cantidad de n�meros para calcular el total de algo. 
#Asimismo, la sumatoria del problema tiene una condici�n, que es: empezar la sumatoria desde el n�mero uno entero positivo hasta un n�mero dado (tambi�n inclu�do en la sumatoria).
#Retornar el resultado de la sumatoria y la sumatoria expl�cita: 3 -> 6 (1+2+3) <- Esto deber�a retornar al ingresar el n�mero tres.
#Usar� el enfoque matem�tica: sumatoria de Gauss, para resolver el problema desde una sola l�nea en vez de iterar c�digo.
def summation(num):
    return num * (num + 1) / 2 #Sumatoria de Gauss, desde 1 hasta n n�mero.
print(summation(100)) #print y funci�n de debugging para confirmar el valor adecuado retornado.