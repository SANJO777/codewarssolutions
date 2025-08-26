#Ejercicio de POO. Sin embargo, sólo funciona desde Codewars porque tienen su clase ahí.
#Comprensión:Construir el objeto con su método constructor: "__init__(self)" para que los atributos y métodos, estén dentro del objeto creado, tengan argumentos para sus valores personalizados o no tengan argumentos para sus valores fijos en los atributos y/o métodos de la clase. 
class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0