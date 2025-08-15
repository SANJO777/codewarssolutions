FIRST_NAME = {'S': 'Alpha', 'P': 'Beta', 'R': 'Cache', 'V': 'Messi'} #No añadir en Codewars.
SURNAME = {'R': 'Analogue', 'W': 'Bomb', 'M': 'Catalyst'} #No añadir en Codewars.
def alias_gen(f_name: str, l_name: str) -> str:#De aquí para abajo añadir a Codewars.
    fn_t = f_name[0].isalpha()
    ln_t = l_name[0].isalpha()
    if fn_t == True and ln_t == True:
        f_name = f_name.capitalize()
        l_name = l_name.capitalize()
        return FIRST_NAME.get(f_name[0]) + " " + SURNAME.get(l_name[0])
        #print(f_name + " " + l_name + " -> " + FIRST_NAME.get(f_name[0]) + " " + SURNAME.get(l_name[0])) #Ocultar los prints porque ya depuramos, ahora añadir returns para Codewars.
    else:
        return "Your name must start with a letter from A - Z."
        #print("Your name must start with a letter from A - Z.") #Ocultar los prints porque ya depuramos, ahora añadir los returns para codewars.
alias_gen("santiago", "rodriguez") #No añadir de aquí para abajo a Codewars porque Codewars ya hace sus propios ejecuciones.
alias_gen("Pacheco", "Whashington") #Esto es para nuestro entorno local saber si funciona; es hacer debbugging, ejecutando la función y print.
alias_gen("ronaldo", "Messi")
alias_gen("Vinicius", "mbappe")
alias_gen("1234", "rodriguez")