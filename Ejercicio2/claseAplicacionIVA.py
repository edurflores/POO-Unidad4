from tkinter import *
from tkinter import ttk, messagebox

class AplicacionIVA:
    __mainframe = None
    __precioBase = 0
    __iva = 0 ### Iva seleccionado con radiobutton
    __impuesto = 0 ### Iva calculado que se suma al precio base
    __total = 0 ### Precio con iva

    def __init__(self):
        self.__mainframe = Tk()
        self.__mainframe.title('Calculo de IVA')
        self.__mainframe.geometry('341x341')
        self.__mainframe.configure(background="white")
        self.__mainframe.rowconfigure(0,weight=1)
        self.__mainframe.rowconfigure(1,weight=1)
        self.__mainframe.rowconfigure(2,weight=1)
        self.__mainframe.rowconfigure(3, weight=1)
        self.__mainframe.columnconfigure(0,weight=1)
        self.__precioBase = StringVar()
        self.__iva = StringVar()
        self.__impuesto = StringVar()
        self.__total = StringVar()
        estiloframetitu = ttk.Style()
        estiloframetitu.configure("BW.TLabel",background="limegreen")
        self.tituframe = ttk.Frame(self.__mainframe,height=50,style="BW.TLabel")
        self.tituframe.configure(border=1,borderwidth=1)
        self.tituframe.grid(row=0,column=0,sticky='nwe')
        self.tituframe.rowconfigure(0,weight=1)
        self.tituframe.columnconfigure(0,weight=1)
        self.tituLabel = ttk.Label(self.tituframe,text='Cálculo de IVA',font=("Helvetica",15),background="limegreen")
        self.tituLabel.grid(row=0,column=0,sticky='nw',padx=100,ipadx=20,pady=20)

        self.LabelPreciosinIva = ttk.Label(self.__mainframe,text='Precio sin IVA',background="white")
        self.LabelPreciosinIva.grid(row=1,column=0,sticky='w',padx=15)
        self.__EntryPreciosinIva = ttk.Entry(self.__mainframe,textvariable=self.__precioBase,width=20)
        self.__EntryPreciosinIva.grid(row=1,column=0,sticky='w',padx=100,ipady=3)

        estiloradiobutton = ttk.Style()
        estiloradiobutton.configure('Wild.TRadiobutton',background="white")

        self.radioIva21 = ttk.Radiobutton(self.__mainframe,text='IVA 21 %',value=21,variable=self.__iva,style="Wild.TRadiobutton")
        self.radioIva21.grid(row=2,column=0,sticky='nw',pady=10,padx=20)

        self.radioIva10 = ttk.Radiobutton(self.__mainframe,text='IVA 10.5 %',value=10,variable=self.__iva,style="Wild.TRadiobutton")
        self.radioIva10.grid(row=2,column=0,sticky='nw',pady=40,padx=20)

        self.LabelIVA = ttk.Label(self.__mainframe,text='IVA',background="white")
        self.LabelIVA.grid(row=2,column=0,sticky='w',pady=70,padx=30)
        self.__EntryIVA = ttk.Entry(self.__mainframe,textvariable=self.__impuesto,state='disabled')
        self.__EntryIVA.grid(row=2,column=0,sticky='w',padx=120)

        self.labelPrecioconIva = ttk.Label(self.__mainframe,text='Precio con IVA',background="white")
        self.labelPrecioconIva.grid(row=2,column=0,sticky='sw',pady=45,padx=30)
        self.__EntryPrecioCONIva = ttk.Entry(self.__mainframe,textvariable=self.__total,state='disabled')
        self.__EntryPrecioCONIva.grid(row=2,column=0,sticky='sw',pady=45,padx=120)


        self.botonCalcular = Button(self.__mainframe,text='Calcular',height=2,width=10,background="lightgreen",command=lambda: self.calcular())
        self.botonCalcular.grid(row=3,column=0,sticky='w',padx=30)

        self.botonSalir = Button(self.__mainframe,text='Salir',height=2,width=10,background="pink",command=lambda: quit())
        self.botonSalir.grid(row=3,column=0,sticky='e',padx=80)

        self.__EntryPreciosinIva.focus()
        self.__mainframe.mainloop()

    def calcular(self):
        try:
            pbase = float(self.__EntryPreciosinIva.get())
            if int(self.__iva.get()) == 10:
                imp = (pbase * 10.5) / 100
                tot = pbase + imp
            elif int(self.__iva.get()) == 21:
                imp = (pbase * 21) / 100
                tot = pbase + imp
            else:
                tot = 0
                imp = 0
            self.__impuesto.set(str(imp))
            self.__total.set(str(tot))
        except ValueError:
            messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numerico')