#Encontrar el primer número no consecutivo dentro de un array. 
#Asimismo, un array debe contener números consecutivos, 
#ya sean: positivos o negativos y un número no consecutivo entre ellos.
#Retornar null (nada) cuando no se encuentre un número consecutivo.
#Un número no consecutivo es un número que no es mayor a uno que el anterior.
#El array mínimo debe de tener mínimo 2 elementos.

def first_non_consecutive(arr):
    for i in range(1, len(arr)): #empezamos desde el segundo elemento de la estructura de datos porque mi expresión lógica necesita el elemento anterior y actual para compararlos. Asimismo, uso len() en el argumento arr para especificar el tamaño de la estructura para que el bucle recorra todos sus elementos y se detenga adecuadamente sin errores.
        if arr[i] != arr[i-1]+1: #Si elemento actual no es igual que el anterior más 1, ya que esta expresión determina si el número no es consecutivo. Si me pidieran el número consecutivo, entonces la expresión tendría que ser el elemento actual debe de ser igual al elemento anterior, que sería i-1 +1.
            return arr[i] #Retorne el elemento actual (que sería el no consecutivo).
    return None #return none explícito al no cumplirse la condición de la búsqueda del número no consecutivo del bucle for. Por ende, el return none, significa: "la estructura sólo contiene números consecutivos".
#print(first_non_consecutive([-4, -3, -2, -1, 0, 1, 2, 3, 5])) #oculto print y función de debugging para verificar el valor retornado.