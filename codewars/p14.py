#Retornar True si el paquete fue recibido el día anterior que fue enviado.
#Retornar False si el paquete No fue recibido el día anterior que fue enviado (entregado el mismo día o posterior).
#Timezone: -11 hasta +12 (incluyendo 0).
#Start, que sería la hora local cuando se envió el paquete: 0 hasta 23.
#Duration, que sería la duración en horas del envío: 0 hasta 24.
#Convertir la hora local que se envió el paquete a la zona horario dónde va a llegar, así sabré la hora local donde va a llegar.
def was_package_received_yesterday(tz_from, tz_to, start, duration):
    if tz_from >= -11 and tz_from <= 12 and tz_to >= -11 and tz_to <= 12 and start >= 0 and start <= 23 and duration >= 0 and duration <= 24: #Validación de datos, que valida el tipo de dato a entero y el rango específico para cada argumento.
        total_horas_transcurridas = start + duration + (tz_to - tz_from) #Fórmula que da el total de horas transcurridas y su resultado puede ser positivo o negativo. Si es +, el paquete llegó el mismo día o posterior de cuando fue enviado y, sino, el paquete llegó el día anterior al que fue enviado.
        if total_horas_transcurridas < 0 and tz_from != tz_to: #Expresión lógica de comparación, que si el total de horas transcurridas es menor o igual que 0 y las dos zonas horarios (origen y llegada) SON DIFERENTES, pues el paquete llegó el día anterior, sino pues llegó el mismo día o posterior.
            return True #Retorna True porque las horas totale transcurridas es un número negativo y al hacerlo, demuestra que el paquete llegó el día anterior de cuando fue enviado.
        else:
            return False #Retorna False porque las horas totales transcurridas es un número positivo y al hacerlo, demuestra que el paquete llegó el mismo día o posterior de cuando fue enviado. Además, incluye el caso de la zona horaria origen y llegada que sean IGUALES, ya que no lo pueden ser.
    else:
        return print("Respeta el tipo de dato y rango de cada argumento")

print(was_package_received_yesterday(12, -11, 5, 6)) #Print y función con valor a cada argumento debugging para verificar retornos adecuados.