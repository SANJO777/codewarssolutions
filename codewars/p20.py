#Fusionar dos arrays ascendentes y/o descendentes de tipo entero en un sólo array final, cumpliendo estas condiciones: 
#Ordenar el array final SIEMPRE en orden ascendente.
#Eliminar valores repetidos y que sólo aparezcan una vez en el array final.
#Retornar un array vacío si ambos arrays están vacíos.
#Lógica: concatenar, eliminar repetidos y dejar un repetido de los eliminados en el array final y reorganizar de forma ascendente.
def merge_arrays(arr1, arr2): #Función que fusiona dos arrays, eliminando elementos repetidos y dejando una copia de ellos en el array final. Asimismo, organiza en orden ascendente el array final y lo retorna. Además, si los arrays están vacíos, los concatena y retorna. También, hace todo lo anterior si sólo hay un array con elementos y el otro está vacío.
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