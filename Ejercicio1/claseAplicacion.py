from tkinter import *
from tkinter import ttk, messagebox, font

class Aplicacion:
    __ventana = None
    __altura = None
    __peso = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('750x400')
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.columnconfigure(0, weight=1)
        self.__ventana.configure(background='white')
        self.__altura = StringVar()
        self.__peso = StringVar()

        fuentetitulo = font.Font(family="Helvetica", size=16, weight="bold")
        self.titulolbl = ttk.Label(self.__ventana,text='Calculadora de IMC',font=fuentetitulo)
        self.titulolbl.configure(background="gray91")
        self.titulolbl.grid(sticky="n", row=0, column=1)

        self.alturalbl = ttk.Label(self.__ventana,text='Altura:',font=(14),background="white")
        self.alturalbl.grid(sticky='e', row=1, column=0, pady=30)
        self.alturaEntry = ttk.Entry(self.__ventana,textvariable=self.__altura)
        self.alturaEntry.grid(sticky='w', row=1, column=1, pady=20, ipadx=70)
        self.cmlabel = ttk.Label(self.__ventana, text='cm', font=(14), background="gray93")
        self.cmlabel.grid(row=1, column=2, sticky='w')

        self.pesolbl = ttk.Label(self.__ventana,text='Peso:',font=(14),background="white")
        self.pesolbl.grid(sticky='e', row=2, column=0, pady=20)
        self.pesoEntry = ttk.Entry(self.__ventana,textvariable=self.__peso)
        self.pesoEntry.grid(sticky='w', row=2, column=1, ipadx=70, pady=20)
        self.kglabel = ttk.Label(self.__ventana,text='kg',font=(14),background="gray93")
        self.kglabel.grid(sticky="w",row=2,column=2)

        self.botonCalcular = ttk.Button(self.__ventana,text='Calcular',command=lambda: self.calcularIMC())
        self.botonCalcular.grid(row=3, column=1, ipadx=30, padx=10,sticky='w')

        self.botonLimpiar = ttk.Button(self.__ventana,text='Limpiar',command=lambda: self.limpiar())
        self.botonLimpiar.grid(row=3, column=2, ipadx=30, padx=10,sticky='w')
        self.alturaEntry.focus()
        self.__ventana.mainloop()

    def calcularIMC(self):
        try:
            self.__altura = int(self.alturaEntry.get())
            self.__peso = float(self.pesoEntry.get())
            imc = self.__peso / (self.__altura / 100) ** 2
            self.muestraIMC(imc)
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar valores enteros')
            self.limpiar()

    def muestraIMC(self,imc):
        global labelIMC
        global labelinfo

        labelIMC = ttk.Label(self.__ventana,text='Tu indice de Masa Corporal (IMC) es %.2f kg/m2' % (imc),font=("Helvetica",12),background="lightblue")
        labelIMC.grid(row=4,column=1,columnspan=2,padx=20,pady=30,sticky='s')

        if imc < 18.5:
            labelinfo = ttk.Label(self.__ventana,text='Peso inferior al normal',font=("Helvetica",12),
                                  background="red")
            labelinfo.grid(row=5,column=1,columnspan=2)
        elif imc >= 18.5 and imc <= 24.9:
            labelinfo = ttk.Label(self.__ventana, text='Peso normal', font=("Helvetica", 12),
                                  background="limegreen")
            labelinfo.grid(row=5, column=1, columnspan=2)
        elif imc >= 25.0 and imc <= 29.9:
            labelinfo = ttk.Label(self.__ventana, text='Peso superior al normal', font=("Helvetica", 12),
                                  background="red")
            labelinfo.grid(row=5, column=1, columnspan=2)
        elif imc >= 30.0:
            labelinfo = ttk.Label(self.__ventana, text='Obesidad', font=("Helvetica", 12),
                                  background="darkred")
            labelinfo.grid(row=5, column=1, columnspan=2)

 ### Hacer funcion que muestre el IMC

    def limpiar(self):
        self.pesoEntry.delete(0,END)
        self.alturaEntry.delete(0,END)
        labelIMC.grid_forget()
        labelinfo.grid_forget()
        self.alturaEntry.focus()