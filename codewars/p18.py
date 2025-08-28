#Comprensi�n: devolver la sumatoria de un array tipo entero, que contiene n�meros enteros (positivos y negativos) y n�meros con formato string (cadena).
def sum_mix(arr):
    return sum(map(int, arr)) #la sumatoria del objeto mutable, pero que se convierte en inmutable por la funci�n map.

#Debugging con print y valores a los argumentos de la funci�n para verificar buen retorno.
print(sum_mix(["1", "2", "3", 4, 5, 6]))
print(sum_mix([0, 1, 2, 3, 4]))
print(sum_mix(["1", "2", "3", "4", "100"]))
print(sum_mix([1, 2, 3]))
