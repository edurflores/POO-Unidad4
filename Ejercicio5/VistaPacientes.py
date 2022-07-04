import tkinter as tk
from tkinter import ttk


from ListaPaciente import ListaPaciente
from UpdatePaciente import UpdatePaciente
#from Controlador import Controlador


class PacientesView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista Pacientes")
        self.geometry("500x350")
        self.config(padx=15, pady=20)
        self.list= ListaPaciente(self)
        self.paciente=UpdatePaciente(self)
        self.agregarbtn= ttk.Button(self, text="Agregar Paciente")
        
        self.list.place(anchor=tk.SW, rely=1, relwidth=0.3, relheight=1)
        self.paciente.place(anchor=tk.NE, rely=0, relx=0.95, relwidth=0.6, relheight=0.8)
        self.agregarbtn.place(anchor= tk.CENTER, rely= 0.9, relx = 0.65, relwidth= 0.3, relheight=0.1)

    def setControlador(self, ctrl):
        self.paciente.setcontrolador(ctrl)
        self.agregarbtn.config(command=ctrl.NuevoPaciente)
        self.list.doble_click(ctrl.seleccionar)

    def agregar(self, paciente):
        self.list.insertar(paciente)
    
    def verpaciente(self, paciente):
        self.paciente.MostrarPaciente(paciente)
    def obtenerdetalles(self):
        return self.paciente.CrearPaciente()
    def replacepaciente(self, index, paciente):
        self.list.modificar(paciente, index)
        tk.messagebox.showinfo("Paciente Modificado", "Paciente Modificado exitosamente")
    def borrar(self, index):
        self.list.borrar(index)
        self.paciente.limpiar()