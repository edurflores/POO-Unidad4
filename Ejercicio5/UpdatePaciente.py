import tkinter as tk
from tkinter import ttk

from PacienteForm import PacienteForm
class UpdatePaciente(PacienteForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btnguardar=ttk.Button(self, text="Guardar")
        self.btnborrar=ttk.Button(self, text="Borrar")
        self.btnimc=ttk.Button(self, text="IMC")

        self.btnimc.place(anchor=tk.S, relwidth= 0.2, relheight=0.1, relx=0.3, rely= 0.96)
        self.btnborrar.place(anchor=tk.S, relwidth=0.2, relheight=0.1, relx=0.5, rely=0.96)
        self.btnguardar.place(anchor=tk.S, relwidth=0.2, relheight=0.1, relx=0.7, rely=0.96)

    def setcontrolador(self, ctrl):
        self.btnguardar.config(command=ctrl.Guardar)
        self.btnimc.config(command=ctrl.imc)
        self.btnborrar.config(command=ctrl.borrar)
    def limpiar(self):
        self.clean()