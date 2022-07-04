import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Paciente import Paciente
class PacienteForm(ttk.Labelframe):
    __fields=("Apellido", "Nombre", "Teléfono", "Altura", "Peso")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Paciente", **kwargs)
        self.entries= list(map(self.CrearCampo, enumerate(self.__fields)))

    def CrearCampo(self, field):
        position, text = field
        label= ttk.Label(self, text=text)
        label.config()
        entry = ttk.Entry(self)
        if position > 0:
            position = position/6

        label.place(anchor=tk.NW, rely= position, relx = 0.017, relheight= 0.1, relwidth = 0.3)
        entry.place(anchor=tk.NW, rely= position, relx = 0.3, relheight= 0.1, relwidth= 0.6)
        return entry
    def MostrarPaciente(self, paciente):

        values=(paciente.getapellido(), paciente.getnom(), paciente.gettel(), paciente.getaltura(), paciente.getpeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    def CrearPaciente(self):
        paciente=Paciente
        values=[e.get() for e in self.entries]
        try:
            paciente=Paciente(*values)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=self)
        else:
            return paciente
    def clean(self):
        for entry in self.entries:
            entry.delete(0, tk.END)
