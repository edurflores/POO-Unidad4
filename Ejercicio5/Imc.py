import tkinter as tk
from tkinter import ttk

class Imc(tk.Toplevel):
    def __init__(self, padre, peso, alt):
        super().__init__(padre)
        self.__imc=tk.DoubleVar()
        self.__txt=tk.StringVar()
        self.calcula(alt, peso)

        self.lbimc=ttk.Label(self, text="IMC")
        self.imcentry=ttk.Entry(self, textvariable=self.__imc, state="disable")
        self.lbtxt=ttk.Label(self, text="Composición Corporal")
        self.txtentry=ttk.Entry(self, textvariable=self.__txt, state="disable")
        self.lbimc.place(anchor=tk.N, relx=0.3, relwidth=0.2)
        self.imcentry.place(anchor=tk.N, relx=0.7, relwidth=0.4)
        self.txtentry.place(anchor=tk.N, relx=0.7, relwidth=0.6, rely=0.4)
        self.lbtxt.place(anchor=tk.N, relx=0.2, relwidth=0.4, rely=0.4)

    def calcula(self, alt, peso):
        try:
            imc=(peso/((alt/100)**2))
            imc=round(imc, 2)
        except ZeroDivisionError:
            tk.messagebox.showerror("Error", "Division entre cero")
        else:
            self.__imc.set(imc)
            if imc<18.5:
                self.__txt.set("Peso Inferior al Normal")
            elif imc<24.9:
                self.__txt.set("Peso Normal")
            elif imc<29.9:
                self.__txt.set("Peso Superior al Normal")
            else:
                self.__txt.set("Obesidad")