#Encontrar el primer n�mero no consecutivo dentro de un array. 
#Asimismo, un array debe contener n�meros consecutivos, 
#ya sean: positivos o negativos y un n�mero no consecutivo entre ellos.
#Retornar null (nada) cuando no se encuentre un n�mero consecutivo.
#Un n�mero no consecutivo es un n�mero que no es mayor a uno que el anterior.
#El array m�nimo debe de tener m�nimo 2 elementos.

def first_non_consecutive(arr):
    for i in range(1, len(arr)): #empezamos desde el segundo elemento de la estructura de datos porque mi expresi�n l�gica necesita el elemento anterior y actual para compararlos. Asimismo, uso len() en el argumento arr para especificar el tama�o de la estructura para que el bucle recorra todos sus elementos y se detenga adecuadamente sin errores.
        if arr[i] != arr[i-1]+1: #Si elemento actual no es igual que el anterior m�s 1, ya que esta expresi�n determina si el n�mero no es consecutivo. Si me pidieran el n�mero consecutivo, entonces la expresi�n tendr�a que ser el elemento actual debe de ser igual al elemento anterior, que ser�a i-1 +1.
            return arr[i] #Retorne el elemento actual (que ser�a el no consecutivo).
    return None #return none expl�cito al no cumplirse la condici�n de la b�squeda del n�mero no consecutivo del bucle for. Por ende, el return none, significa: "la estructura s�lo contiene n�meros consecutivos".
#print(first_non_consecutive([-4, -3, -2, -1, 0, 1, 2, 3, 5])) #oculto print y funci�n de debugging para verificar el valor retornado.