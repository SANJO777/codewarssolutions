def sp_eng(sentence):
    sentence = sentence.lower()
    if sentence.count("english") == 1: #S� el count con el substring english dentro de un string es igual a 1, si funciona. No obstante, si hay m�s de 1 un english s�lo funcionar�a agregando la condici�n mayor o igual que 1.
       return True
       #print(sentence) debugging completado y todos los casos pone en min�sculas la palabra y s� sirve el .count en cualquier lado.
    else:
        return False
        #print(sentence) #Asimismo, los m�todos se pueden usar en cualquier lado cuando se necesitan usar para hacer un c�digo: limpio, simple y escalable para que de buen rendimiento en cualquier sistema.

#print(sp_eng("123123123213EnglishEnglish")) #Ocultar print y funci�n con argumento de debugging para conocer valor adecuado para retornar.