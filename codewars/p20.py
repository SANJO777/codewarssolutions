#Fusionar dos arrays ascendentes y/o descendentes de tipo entero en un s�lo array final, cumpliendo estas condiciones: 
#Ordenar el array final SIEMPRE en orden ascendente.
#Eliminar valores repetidos y que s�lo aparezcan una vez en el array final.
#Retornar un array vac�o si ambos arrays est�n vac�os.
#L�gica: concatenar, eliminar repetidos y dejar un repetido de los eliminados en el array final y reorganizar de forma ascendente.
def merge_arrays(arr1, arr2): #Funci�n que fusiona dos arrays, eliminando elementos repetidos y dejando una copia de ellos en el array final. Asimismo, organiza en orden ascendente el array final y lo retorna. Adem�s, si los arrays est�n vac�os, los concatena y retorna. Tambi�n, hace todo lo anterior si s�lo hay un array con elementos y el otro est� vac�o.
    if len(arr1) >= 1 and len(arr2) >= 1:
        return sorted(set(arr1+arr2))
    else:
        return sorted(set(arr1+arr2))
print(merge_arrays([0, 1, 2, 3], [4, 5, 6, 7, 8]))
print(merge_arrays([2, 3, 5], [1, 4, 6]))
print(merge_arrays([], []))
print(merge_arrays([-1, -10, -777, 1, 9, 10], [-2, -9, -776, 2, 8, 11]))
print(merge_arrays([1, 2, 3], [1, 2, 3]))
print(merge_arrays([1, 2, 3], []))
print(merge_arrays([], [2, 10, 1]))
print(merge_arrays([2], [1]))