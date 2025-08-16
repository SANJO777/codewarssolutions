def simple_multiplication(number) : #Multiplicar un número par por 8 y si es impar por 9.
    par = number%2 #Deben de darme el resultado (o residuo) 0 todos los números pares divididos en 2. Sino, es impar porque da 1.
    if par ==0:
        return number * 8
    else:
        return number * 9
#print(simple_multiplication(777)) #print y función de debugging para comprobar resultado del retorno adecuado.