from tkinter import *
from tkinter import ttk, messagebox
import json
from urllib.request import urlopen ### Uso de API


class AplicacionDolar:
    __dolares = None ### Cantidad de dolares ingresada
    __pesos = None ### Cantidad de pesos resultantes de la conversion

    def __init__(self):
        self.__dolarventa = self.consulta()
        self.__ventana = Tk()
        self.__ventana.title('Conversor de moneda')
        self.__ventana.geometry('400x300')
        self.__dolares = StringVar()
        self.__pesos = StringVar()

        self.__mainframe = ttk.Frame(self.__ventana,padding=(3,3,12,12))
        self.__mainframe.configure(borderwidth=2,relief='sunken')
        self.__mainframe.grid(row=0,column=0,sticky='nswe')
        self.__mainframe.rowconfigure(0,weight=1)
        self.__mainframe.columnconfigure(0,weight=1)

        self.__entryDolar = ttk.Entry(self.__mainframe,width=8,textvariable=self.__dolares)
        self.__entryDolar.grid(row=1,column=2,sticky='we')

        labelDolar = ttk.Label(self.__mainframe,text='dólares')
        labelDolar.grid(row=1,column=3,sticky='we')

        labelEquivalente = ttk.Label(self.__mainframe,text='es equivalente a ')
        labelEquivalente.grid(row=3,column=1)

        labelPesosConvertido = Label(self.__mainframe,textvariable=self.__pesos)
        labelPesosConvertido.grid(row=3,column=2)

        labelPesostexto = ttk.Label(self.__mainframe,text='pesos')
        labelPesostexto.grid(row=3,column=3)

        botonSalir = Button(self.__mainframe,text='Salir',command=lambda: quit())
        botonSalir.grid(row=4,column=3)

        self.__dolares.trace('w',self.conversion)
        self.__entryDolar.focus()
        self.__mainframe.mainloop()

    def consulta(self): ### Obtiene el valor del dolar para la venta, API
        url_template = 'https://www.dolarsi.com/api/api.php?type=dolar'
        response = urlopen(url_template)
        self.__resultadoAPI = json.loads(response.read().decode())

        return self.__resultadoAPI[0]['casa']['venta']

    def conversion(self,*args): ### Convierte dolares a pesos
        if self.__dolares.get() != '':
            try:
                dolares = float(self.__dolares.get())
                self.__dolarventa = self.__dolarventa.replace(',','.') ### Reemplaza coma por un punto
                total = dolares * float(self.__dolarventa) ### Convertido de dolares a pesos
                self.__pesos.set('%.2f' % (total))
            except ValueError:
                messagebox.showerror(title='Error de tipo',message='Debe ingresar valores numericos')
        else:
            self.__pesos.set('')