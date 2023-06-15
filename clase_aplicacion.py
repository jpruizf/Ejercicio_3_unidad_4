from tkinter import*
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana= None
    __dolares= None
    __pesos= None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title("Conversor de moneda")
        mainframe = ttk.Frame(self.__ventana,padding='3 3 12 12')
        mainframe.grid(row=0, column=0, sticky=(N, W, E, S))
        mainframe.rowconfigure(0, weight= 1)
        mainframe.columnconfigure(0, weight= 1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__dolares= StringVar()
        self.__pesos = StringVar()
        self.__dolares.trace("w", self.calcular)
        self.__dolares_entry = ttk.Entry(mainframe, width=7, textvariable= self.__dolares)
        self.__dolares_entry.grid(row=1, column= 2, sticky=(W, E))
        ttk.Label(mainframe, textvariable= self.__pesos).grid(row=2, column=2, sticky=(W, E))
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(row=3, column=3, sticky=W)
        ttk.Label(mainframe,text='dolares').grid(row=1, column=3, sticky=W)
        ttk.Label(mainframe,text='es equivalente a').grid(row=2, column=1, sticky=E)
        ttk.Label(mainframe,text='pesos').grid(row=2, column=3,sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5,pady=5)
        self.__dolares_entry.focus()
        self.__ventana.mainloop()
    def calcular(self, *args):
        if self.__dolares_entry.get()!="":
            try:
                valor=float(self.__dolares_entry.get())
                self.__pesos.set(valor*500)
            except ValueError:
                messagebox.showerror(title='Error de tipo', message='Ingrese un valor valido')
                self.__dolares.set("")
                self.__dolares_entry.focus()
        else:
            self.__pesos.set("")