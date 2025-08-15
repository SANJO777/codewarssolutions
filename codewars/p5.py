def sp_eng(sentence):
    sentence = sentence.lower()
    if sentence.count("english") == 1: #Sí el count con el substring english dentro de un string es igual a 1, si funciona. No obstante, si hay más de 1 un english sólo funcionaría agregando la condición mayor o igual que 1.
       return True
       #print(sentence) debugging completado y todos los casos pone en minúsculas la palabra y sí sirve el .count en cualquier lado.
    else:
        return False
        #print(sentence) #Asimismo, los métodos se pueden usar en cualquier lado cuando se necesitan usar para hacer un código: limpio, simple y escalable para que de buen rendimiento en cualquier sistema.

#print(sp_eng("123123123213EnglishEnglish")) #Ocultar print y función con argumento de debugging para conocer valor adecuado para retornar.