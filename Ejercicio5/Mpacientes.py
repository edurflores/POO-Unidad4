from Paciente import Paciente

class ManejaPaciente(object):
    __Pacientes=list
    def __init__(self):
        self.__Pacientes=[]
    def agregar(self, paciente):
        if isinstance(paciente, Paciente):
            self.__Pacientes.append(paciente)
    def getpacientes(self):
        return self.__Pacientes
    def updatePaciente(self, paciente, pacienteactualizado):
        indice = self.obtenerpaciente(paciente)
        self.__Pacientes[indice] = pacienteactualizado
    def obtenerpaciente(self, paciente):
        i=0
        while i < len(self.__Pacientes) and paciente != self.__Pacientes[i]:
            i+=1
        if i<len(self.__Pacientes):
            return i

    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            Elementos = [elemento.toJSON() for elemento in self.__Pacientes]
        )
    def borrar(self, index):
        try:
            self.__Pacientes.pop(index)
        except IndexError:
            raise IndexError("No se seleccionó paciente")

        