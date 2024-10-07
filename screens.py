
import constants
import tkinter as tk
from tkinter import font as tkfont
from register_authenticate import Register_Authenticate


class Home(tk.Frame):
    def __init__(self, parent, controller):
        """ Método constructor de la clase """
        super().__init__(parent)
        self.controller = controller
        self.configure(background=constants.BACKGROUND1)
        self.user_manager = Register_Authenticate()
        self.init_buttons()

    def init_buttons(self):
        # Definir estilos
        button_font = tkfont.Font(family="Helvetica", size=15, weight="normal")
        button_style = {
            "bg": "#0d6f91",  # Color de fondo
            "fg": "white",  # Color de texto
            "font": button_font,
            "borderwidth": 2,
            "relief": tk.GROOVE,
            "activebackground": "white",  # Color de fondo al hacer clic
            "activeforeground": "#0d6f91"  # Color de texto al hacer clic
        }
        # Frame para centrar los botones
        button_frame = tk.Frame(self, bg=constants.BACKGROUND1)
        button_frame.pack(expand=True)
        # Botón de Inicio de Sesión
        login_button = tk.Button(button_frame, text="Iniciar Sesión", command=self.iniciar_sesion, **button_style)
        login_button.pack(pady=10)

        # Botón de Registrarse
        register_button = tk.Button(button_frame, text="Registrarse", command=self.registrarse, **button_style)
        register_button.pack(pady=10)

        # Botón de Salir
        exit_button = tk.Button(button_frame, text="Salir", command=self.salir, **button_style)
        exit_button.pack(pady=10)

    def iniciar_sesion(self):
        """ Lógica para el botón de iniciar sesión """
        self.controller.show_frame(InicioSesion)

    def registrarse(self):
        self.controller.show_frame(Registro)

    def salir(self):
        """ Lógica para salir de la aplicación """
        self.controller.quit()

    def pedir_input(self, title, prompt):
        """ Muestra una ventana emergente para pedir un input al usuario """
        input_window = tk.Toplevel(self)
        input_window.title(title)

        # Variable controlada por Tkinter para almacenar el valor
        input_value = tk.StringVar()

        tk.Label(input_window, text=prompt).pack(pady=5)
        entry = tk.Entry(input_window, textvariable=input_value)
        entry.pack(pady=5)

        def obtener_valor():
            input_window.destroy()  # Cerramos la ventana cuando el usuario termina

        submit_button = tk.Button(input_window, text="OK", command=obtener_valor)
        submit_button.pack(pady=5)

        self.wait_window(input_window)  # Esperamos que la ventana emergente se cierre

        # Retornamos el valor almacenado en input_value
        return input_value.get()


class InicioSesion(tk.Frame):
    def __init__(self, parent, controller):
        """ Método constructor de la clase """
        super().__init__(parent)
        self.configure(background=constants.BACKGROUND2)
        self.controller = controller

class Registro(tk.Frame):
    def __init__(self, parent, controller):
        """ Método constructor de la clase """
        super().__init__(parent)
        self.configure(background=constants.BACKGROUND3)
        self.controller = controller

        """Lógica para el botón de registrarse
        username = self.pedir_input("Registrarse", "Ingresa un nombre de usuario:")
        password = self.pedir_input("Registrarse", "Ingresa una contraseña:")

        if username and password:
            self.user_manager.registrar_usuario(username, password)"""

