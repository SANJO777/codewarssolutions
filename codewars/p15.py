#Ejercicio de POO. Sin embargo, s�lo funciona desde Codewars porque tienen su clase ah�.
#Comprensi�n:Construir el objeto con su m�todo constructor: "__init__(self)" para que los atributos y m�todos, est�n dentro del objeto creado, tengan argumentos para sus valores personalizados o no tengan argumentos para sus valores fijos en los atributos y/o m�todos de la clase. 
class Hero(object):
    def __init__(self, name='Hero'):
        self.name = name
        self.position = '00'
        self.health = 100
        self.damage = 5
        self.experience = 0