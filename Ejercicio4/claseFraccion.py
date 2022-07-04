import re

class Fraccion(object):
    __denominador= int
    __numerador=int

    def __init__(self, num):
        if re.search("^-?[(0-9)]+/[(0-9)]{1,6}$", num):
            self.__numerador, self.__denominador= num.split("/")
            self.__numerador, self.__denominador= int(self.__numerador), int(self.__denominador)
        else:
            self.__numerador = int(num)
            self.__denominador = 1
        

    def getnumerador(self):
        return self.__numerador

    def getdenominador(self):
        return self.__denominador

    def mcd(self, num1, num2):
        aux1= max(num1, num2)
        aux2 = min(num1, num2)
        mcd=int
        while aux2!=0:
            mcd = aux2
            aux2 = aux1%aux2
            aux1 = mcd
        return mcd
    def mcm(self, num1, num2):
        aux1= max(num1, num2)
        aux2 = min(num1, num2)
        mcm=int((aux1/self.mcd(aux1, aux2))*aux2)
        return mcm

    def simplificar(self):
        mcd = self.mcd(self.__numerador, self.__denominador)
        self.__numerador = int(self.__numerador/mcd)
        self.__denominador = int(self.__denominador/mcd)
        return self

    def __str__(self):
        return "{}/{}".format(self.__numerador, self.__denominador)

    def __radd__(self, otro):
        denominador = int
        numerador= int
        if otro != type(Fraccion):
            otro=Fraccion("{}/1".format(otro))
        if otro.getdenominador() == self.__denominador:
            denominador= self.__denominador
            numerador= self.__numerador+ otro.getnumerador()
        else:
            denominador=self.mcm(self.__denominador, otro.getdenominador())
            numerador = (denominador/self.__denominador)*self.__numerador + (denominador/otro.getdenominador())*otro.getnumerador()
        
        return Fraccion("{}/{}".format(int(numerador), int(denominador))).simplificar()
    def __add__(self, otro):
        denominador = None
        numerador= None
        if type(otro) != Fraccion:
            otro=Fraccion("{}/1".format(otro))
        if otro.getdenominador() == self.__denominador:
            denominador= int(self.__denominador)
            numerador= int(self.__numerador+ otro.getnumerador())
        else:
            denominador=int(self.mcm(self.__denominador, otro.getdenominador()))
            numerador = int((denominador/self.__denominador)*self.__numerador + (denominador/otro.getdenominador())*otro.getnumerador())
        
        return Fraccion("{}/{}".format(int(numerador), int(denominador))).simplificar()

    def __sub__(self, otro):
        denominador = None
        numerador= None
        if type(otro) != Fraccion:
            otro=Fraccion("{}/1".format(otro))
        if otro.getdenominador() == self.__denominador:
            denominador= int(self.__denominador)
            numerador= int(self.__numerador - otro.getnumerador())
        else:
            denominador= int(self.mcm(self.__denominador, otro.getdenominador()))
            numerador = int((denominador/self.__denominador)*self.__numerador - (denominador/otro.getdenominador())*otro.getnumerador())
        
        return Fraccion("{}/{}".format(int(numerador), int(denominador))).simplificar()
    def __mul__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion("{}/1".format(otro))
        denominador = self.__denominador*otro.getdenominador()
        numerador= self.__numerador*otro.getnumerador()
        return Fraccion("{}/{}".format(numerador, denominador)).simplificar()
    def __rmul__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion("{}/1".format(otro))
        denominador = self.__denominador*otro.getdenominador()
        numerador= self.__numerador*otro.getnumerador()
        return Fraccion("{}/{}".format(numerador, denominador)).simplificar()
    def __truediv__(self, otro):
        if type(otro) != Fraccion:
            otro = Fraccion("{}/1".format(otro))
        denominador= self.__denominador*otro.getnumerador()
        numerador=self.__numerador*otro.getdenominador()
        return Fraccion("{}/{}".format(numerador, denominador)).simplificar()
    