
import constants
import tkinter as tk

from tkinter import font as tkfont
from tkinter import messagebox
from register_authenticate import Register_Authenticate

class Home(tk.Frame):
    def __init__(self, parent, controller):
        """ Método constructor de la clase """
        super().__init__(parent)
        self.controller = controller
        self.configure(background=constants.BACKGROUND)
        self.user_manager = Register_Authenticate()
        self.init_widgets()

    def init_widgets(self):
        """Inicializa los widgets en la pantalla"""
        # Frame principal para alinear elementos verticalmente
        main_frame = tk.Frame(self, bg=constants.BACKGROUND)
        main_frame.pack(expand=True)
        # Título de la pantalla
        title_label = tk.Label(
            main_frame,
            text="MyDiary.com",
            font=("Arial", 30),
            bg=constants.BACKGROUND,
            fg="black")
        title_label.pack(pady=15)
        # Frame para centrar los botones
        button_frame = tk.Frame(main_frame, bg=constants.BACKGROUND)
        button_frame.pack()
        # Botón de Inicio de Sesión
        login_button = tk.Button(
            button_frame,
            text="Iniciar Sesión",
            command=self.iniciar_sesion,
            font=("Arial", 10),
            width=10,
            padx=7,
            pady=7,
            bg=constants.BOTON,
            fg="black",
            relief="solid",
            bd=0
        )
        login_button.pack(pady=7)
        # Botón de Registrarse
        register_button = tk.Button(
            button_frame,
            text="Registrarse",
            command=self.registrarse,
            font=("Arial", 10),
            width=10,
            padx=7,
            pady=7,
            bg=constants.BOTON,
            fg="black",
            relief="solid",
            bd=0
        )
        register_button.pack(pady=7)
        # Botón de Salir
        exit_button = tk.Button(
            button_frame,
            text="Salir",
            command=self.salir,
            font=("Arial", 10),
            width=10,
            padx=7,
            pady=7,
            bg=constants.BOTON,
            fg="black",
            relief="solid",
            bd=0
        )
        exit_button.pack(pady=7)

    def iniciar_sesion(self):
        """ Lógica para el botón de iniciar sesión """
        self.controller.show_frame(InicioSesion)

    def registrarse(self):
        self.controller.show_frame(Registro)

    def salir(self):
        """ Lógica para salir de la aplicación """
        self.controller.quit()

class InicioSesion(tk.Frame):
    def __init__(self, parent, controller):
        """ Método constructor de la clase """
        super().__init__(parent)
        self.configure(background=constants.BACKGROUND)
        self.controller = controller
        self.user_manager = Register_Authenticate()
        self.init_widgets()

    def init_widgets(self):
        # Frame principal para alinear elementos verticalmente
        main_frame = tk.Frame(self, bg=constants.BACKGROUND)
        main_frame.pack(expand=True)
        # Título de la pantalla
        title_label = tk.Label(
            main_frame,
            text="Iniciar Sesión",
            font=("Arial", 30),
            bg=constants.BACKGROUND)
        title_label.pack(pady=5)
        # Frame para centrar los botones y campos de entrada
        button_frame = tk.Frame(main_frame, bg=constants.BACKGROUND)
        button_frame.pack(pady=7)
        # Campo de entrada para el nombre de usuario
        self.username_label = tk.Label(
            button_frame,
            text="Nombre de usuario:",
            font=("Arial", 10),
            bg=constants.BACKGROUND
        )
        self.username_label.pack(pady=2)
        # Etiqueta para escribir el nombre de usuario
        self.username_entry = tk.Entry(button_frame)
        self.username_entry.pack(pady=2)
        # Campo de entrada para la contraseña
        self.password_label = tk.Label(
            button_frame,
            text="Contraseña:",
            font=("Arial", 10),
            bg=constants.BACKGROUND
        )
        self.password_label.pack(pady=2)
        # Etiqueta para escribir la contraseña
        self.password_entry = tk.Entry(button_frame, show="*")
        self.password_entry.pack(pady=2)
        # Botón de inicio de sesión
        login_button = tk.Button(
            button_frame,
            text="Iniciar Sesión",
            command=self.iniciar_sesion,
            font = ("Arial", 10),
            width = 10,
            padx = 7,
            pady = 7,
            bg = constants.BOTON,
            fg = "black",
            relief = "solid",
            bd = 0
        )
        login_button.pack(pady=15, padx=10)
        # Botón para volver al inicio
        back_button = tk.Button(
            button_frame,
            text="Volver al Inicio",
            command=lambda: self.controller.show_frame(Home),
            font=("Arial", 10),
            width=10,
            padx=7,
            pady=7,
            bg=constants.BOTON,
            fg="black",
            relief="solid",
            bd=0
        )
        back_button.pack(pady=5, padx=10)

    def iniciar_sesion(self):
        """Método para iniciar sesión"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_manager.autenticar_usuario(username, password):
            messagebox.showinfo("Éxito", f"¡Bienvenido/a {username}!")
        else:
            messagebox.showerror("Error", "Acceso denegado. Nombre de usuario o contraseña incorrectos.")
import tkinter as tk
from tkinter import messagebox

class Registro(tk.Frame):
    def __init__(self, parent, controller):
        """ Método constructor de la clase """
        super().__init__(parent)
        self.configure(background=constants.BACKGROUND)
        self.controller = controller
        self.user_manager = Register_Authenticate()
        self.init_widgets()

    def init_widgets(self):
        # Frame principal para alinear elementos verticalmente
        main_frame = tk.Frame(self, bg=constants.BACKGROUND)
        main_frame.pack(expand=True)
        # Título de la pantalla
        title_label = tk.Label(
            main_frame,
            text="Registrarse",
            font=("Arial", 30),
            bg=constants.BACKGROUND
        )
        title_label.pack(pady=5)
        # Frame para centrar los botones y campos de entrada
        button_frame = tk.Frame(main_frame, bg=constants.BACKGROUND)
        button_frame.pack(pady=7)
        # Campo de entrada para el nombre de usuario
        self.username_label = tk.Label(
            button_frame,
            text="Nombre de usuario:",
            font=("Arial", 10),
            bg=constants.BACKGROUND
        )
        self.username_label.pack(pady=2)
        # Etiqueta para escribir el nombre de usuario
        self.username_entry = tk.Entry(button_frame)
        self.username_entry.pack(pady=2)
        # Campo de entrada para la contraseña
        self.password_label = tk.Label(
            button_frame,
            text="Contraseña:",
            font=("Arial", 10),
            bg=constants.BACKGROUND
        )
        self.password_label.pack(pady=2)
        # Etiqueta para escribir la contraseña
        self.password_entry = tk.Entry(button_frame, show="*")
        self.password_entry.pack(pady=2)
        # Botón para registrar
        register_button = tk.Button(
            button_frame,
            text="Registrar",
            command=self.registrar_usuario,
            font=("Arial", 10),
            width=10,
            padx=7,
            pady=7,
            bg=constants.BOTON,
            fg="black",
            relief="solid",
            bd=0
        )
        register_button.pack(pady=15, padx=10)
        # Botón para volver al inicio
        back_button = tk.Button(
            button_frame,
            text="Volver al Inicio",
            command=lambda: self.controller.show_frame(Home),
            font=("Arial", 10),
            width=10,
            padx=7,
            pady=7,
            bg=constants.BOTON,
            fg="black",
            relief="solid",
            bd=0
        )
        back_button.pack(pady=5, padx=10)

    def registrar_usuario(self):
        """ Método para registrar un nuevo usuario """
        # Obtenemos el username y la contraseña
        username = self.username_entry.get()
        password = self.password_entry.get()
        # Comprobamos que no sean strings vacíos
        if username and password:
            # Comprbamos el formato de la contraseña
            if not self.user_manager.comprobar_formato_contraseña(password):
                # Ventana de advertencia en caso de que la contraseña no presente un formato correcto
                messagebox.showinfo("Advertencia",
                                    "La contraseña no tiene un formato válido: mínimo 8 caracteres de los cuales incluyan al menos una mayúscula, un número y un carácter especial")
                self.controller.show_frame(Home)
            else:
                # Intentamos registrar el usuario
                if self.user_manager.registrar_usuario(username, password):
                    # Ventana de éxito en caso de que el usuario se haya registrado correctamente
                    messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")
                    self.controller.show_frame(Home)
                else:
                    # Ventana de error en caso de que el nombre de usuario se repita
                    messagebox.showerror("Error", "El nombre de usuario ya está en uso.")
        else:
            # Ventana de advertencia si los datos son strings vacíos
            messagebox.showwarning("Advertencia", "Por favor, ingresa un nombre de usuario y una contraseña.")
