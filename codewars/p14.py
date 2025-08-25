#Retornar True si el paquete fue recibido el d�a anterior que fue enviado.
#Retornar False si el paquete No fue recibido el d�a anterior que fue enviado (entregado el mismo d�a o posterior).
#Timezone: -11 hasta +12 (incluyendo 0).
#Start, que ser�a la hora local cuando se envi� el paquete: 0 hasta 23.
#Duration, que ser�a la duraci�n en horas del env�o: 0 hasta 24.
#Convertir la hora local que se envi� el paquete a la zona horario d�nde va a llegar, as� sabr� la hora local donde va a llegar.
def was_package_received_yesterday(tz_from, tz_to, start, duration):
    if tz_from >= -11 and tz_from <= 12 and tz_to >= -11 and tz_to <= 12 and start >= 0 and start <= 23 and duration >= 0 and duration <= 24: #Validaci�n de datos, que valida el tipo de dato a entero y el rango espec�fico para cada argumento.
        total_horas_transcurridas = start + duration + (tz_to - tz_from) #F�rmula que da el total de horas transcurridas y su resultado puede ser positivo o negativo. Si es +, el paquete lleg� el mismo d�a o posterior de cuando fue enviado y, sino, el paquete lleg� el d�a anterior al que fue enviado.
        if total_horas_transcurridas < 0 and tz_from != tz_to: #Expresi�n l�gica de comparaci�n, que si el total de horas transcurridas es menor o igual que 0 y las dos zonas horarios (origen y llegada) SON DIFERENTES, pues el paquete lleg� el d�a anterior, sino pues lleg� el mismo d�a o posterior.
            return True #Retorna True porque las horas totale transcurridas es un n�mero negativo y al hacerlo, demuestra que el paquete lleg� el d�a anterior de cuando fue enviado.
        else:
            return False #Retorna False porque las horas totales transcurridas es un n�mero positivo y al hacerlo, demuestra que el paquete lleg� el mismo d�a o posterior de cuando fue enviado. Adem�s, incluye el caso de la zona horaria origen y llegada que sean IGUALES, ya que no lo pueden ser.
    else:
        return print("Respeta el tipo de dato y rango de cada argumento")

print(was_package_received_yesterday(12, -11, 5, 6)) #Print y funci�n con valor a cada argumento debugging para verificar retornos adecuados.