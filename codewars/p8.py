def hex_to_dec(s): #Convertir los n�meros hexadecimales a decimales. Asimismo, los n�meros hexadecimales est�n almacenados en cadenas (string).
    return float.fromhex(s) #m�todo float.fromhex para n�meros hexadecimales string a decimales.
#print(hex_to_dec('0x309.C6E978D4FDF3B645')) #argumento en n�mero hexadecimal string. Asimismo, se puede hacer int string y etc�tera.
#Print y funci�n con su argumento debugging para comprobar el valor retornado adecuado.