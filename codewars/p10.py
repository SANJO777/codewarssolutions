#La sumatoria es sumar una cantidad de números para calcular el total de algo. 
#Asimismo, la sumatoria del problema tiene una condición, que es: empezar la sumatoria desde el número uno entero positivo hasta un número dado (también incluído en la sumatoria).
#Retornar el resultado de la sumatoria y la sumatoria explícita: 3 -> 6 (1+2+3) <- Esto debería retornar al ingresar el número tres.
#Usaré el enfoque matemática: sumatoria de Gauss, para resolver el problema desde una sola línea en vez de iterar código.
def summation(num):
    return num * (num + 1) / 2 #Sumatoria de Gauss, desde 1 hasta n número.
print(summation(100)) #print y función de debugging para confirmar el valor adecuado retornado.