from VistaPacientes import PacientesView
from Mpacientes import ManejaPaciente
from NuevoPaciente import nuevopaciente
from Imc import Imc
from tkinter import messagebox
class Controlador(object):
    __vista= PacientesView
    __seleccion=int
    __paciente=ManejaPaciente

    def __init__(self, vista, paciente):
        self.__vista = vista
        self.__paciente = paciente
        self.__seleccion=-1
    def NuevoPaciente(self):
        nuevo=nuevopaciente(self.__vista).show()
        if nuevo:
            self.__paciente.agregar(nuevo)
            self.__vista.agregar(nuevo)
    def seleccionar(self, index):
        self.__seleccion = index
        paciente = self.__paciente.getpacientes()[index]
        self.__vista.verpaciente(paciente)

    def start(self):
        for p in self.__paciente.getpacientes():
            self.__vista.agregar(p)
        self.__vista.mainloop()
    def Guardar(self):
        if self.__seleccion == -1:
            return 
        paciente=self.__vista.obtenerdetalles()
        self.__paciente.updatePaciente(self.__paciente.getpacientes()[self.__seleccion], paciente)
        self.__vista.replacepaciente(self.__seleccion, paciente)
    def imc(self):
        if self.__seleccion == -1:
            return
        paciente=self.__vista.obtenerdetalles()
        Imc(self.__vista, paciente.getpeso(), paciente.getaltura())
    def borrar(self):
        if self.__seleccion == -1:
            return
        self.__vista.borrar(self.__seleccion)
        self.__paciente.borrar(self.__seleccion)
    def salir(self):
        return self.__paciente.toJSON()

