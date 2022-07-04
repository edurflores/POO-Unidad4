from re import search

class Paciente(object):
    __nombre = str
    __apellido = str
    __tel = str
    __altura= int
    __peso = float

    def __init__(self,apellido, nom, tel, alt, peso):
        self.__nombre = nom if nom != "" else self.error("Ingrese Nombre")
        self.__apellido = apellido if apellido != "" else self.error("Ingrese Apellido")
        self.__peso = float(peso) if peso != "" else self.error ("Ingrese Peso")
        self.__altura = int(alt) if alt != "" else self.error("Ingrese altura")
        self.__tel = tel if search("([0-9]{3})[0-9]{7}", tel) else self.error("Teléfono Incorrecto")
    def getpeso(self):
        return self.__peso
    def getaltura(self):
        return self.__altura
    def gettel(self):
        return self.__tel
    def getnom(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    def setapellido(self, apellido):
        self.__apellido = apellido
    def setnombre(self, nombre):
        self.__nombre = nombre
    def setpeso(self, peso):
        if isinstance(peso, float):
            self.__peso = peso
    def setaltura(self, altura):
        if isinstance(altura, int):
            self.__altura = altura
    def settelefono(self, telefono):
        self.__tel=telefono
    def error(self, message):
        raise ValueError(message)
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,  
            __atributos__=dict(
                peso = self.__peso,
                nom = self.__nombre,
                apellido = self.__apellido,
                alt = self.__altura,
                tel = self.__tel
            )
        )
        return d