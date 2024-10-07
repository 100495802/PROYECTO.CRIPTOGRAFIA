
import tkinter as tk
from screens import Home, InicioSesion, Registro
from register_authenticate import Register_Authenticate

class Manager(tk.Tk):
    """ Clase generadora de la interfaz """
    def __init__(self, *args, **kwargs):
        """ Método constructor de la clase. Hereda de la clase tk.Tk """
        super().__init__(*args, **kwargs)
        self.title("Manuel putero")
        self.user_manager = Register_Authenticate()
        # Contenedor principal
        container = tk.Frame(self)
        container.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (Home, InicioSesion, Registro):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.show_frame(Home)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()