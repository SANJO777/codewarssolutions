def hex_to_dec(s): #Convertir los números hexadecimales a decimales. Asimismo, los números hexadecimales están almacenados en cadenas (string).
    return float.fromhex(s) #método float.fromhex para números hexadecimales string a decimales.
#print(hex_to_dec('0x309.C6E978D4FDF3B645')) #argumento en número hexadecimal string. Asimismo, se puede hacer int string y etcétera.
#Print y función con su argumento debugging para comprobar el valor retornado adecuado.