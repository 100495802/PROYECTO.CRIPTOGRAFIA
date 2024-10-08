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
        self.configure(background=constants.BACKGROUND1)
        self.user_manager = Register_Authenticate()
        self.init_widgets()

    def init_widgets(self):
        # Frame para centrar los botones
        button_frame = tk.Frame(self, bg=constants.BACKGROUND1)
        button_frame.pack(expand=True)
        # Botón de Inicio de Sesión
        login_button = tk.Button(button_frame, text="Iniciar Sesión", command=self.iniciar_sesion)
        login_button.pack(pady=10)
        # Botón de Registrarse
        register_button = tk.Button(button_frame, text="Registrarse", command=self.registrarse)
        register_button.pack(pady=10)
        # Botón de Salir
        exit_button = tk.Button(button_frame, text="Salir", command=self.salir)
        exit_button.pack(pady=10)

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
        self.configure(background=constants.BACKGROUND2)
        self.controller = controller
        self.user_manager = Register_Authenticate()
        self.init_widgets()

    def init_widgets(self):
        # Título de la pantalla
        title_label = tk.Label(self, text="Iniciar Sesión", font=("Arial", 24), bg=constants.BACKGROUND2)
        title_label.pack(pady=10)

        # Campo de entrada para el nombre de usuario
        self.username_label = tk.Label(self, text="Nombre de usuario:", bg=constants.BACKGROUND2)
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        # Campo de entrada para la contraseña
        self.password_label = tk.Label(self, text="Contraseña:", bg=constants.BACKGROUND2)
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        # Botón de inicio de sesión
        login_button = tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion)
        login_button.pack(pady=10)

        # Botón para volver al inicio
        back_button = tk.Button(self, text="Volver al Inicio", command=lambda: self.controller.show_frame(Home))
        back_button.pack(pady=5)

    def iniciar_sesion(self):
        """ Método para iniciar sesión """
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_manager.autenticar_usuario(username, password):
            messagebox.showinfo("Éxito", f"¡Bienvenido {username}!")
            # Aquí puedes redirigir a otra pantalla o realizar otras acciones
        else:
            messagebox.showerror("Error", "Acceso denegado. Nombre de usuario o contraseña incorrectos.")

class Registro(tk.Frame):
    def __init__(self, parent, controller):
        """ Método constructor de la clase """
        super().__init__(parent)
        self.configure(background=constants.BACKGROUND3)
        self.controller = controller
        self.user_manager = Register_Authenticate()
        self.init_widgets()

    def init_widgets(self):
        # Título de la pantalla
        title_label = tk.Label(self, text="Registro de Usuario", font=("Arial", 24), bg=constants.BACKGROUND3)
        title_label.pack(pady=10)
        # Campo de entrada para el nombre de usuario
        self.username_label = tk.Label(self, text="Nombre de usuario:", bg=constants.BACKGROUND3)
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)
        # Campo de entrada para la contraseña
        self.password_label = tk.Label(self, text="Contraseña:", bg=constants.BACKGROUND3)
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        # Botón para registrar
        register_button = tk.Button(self, text="Registrar", command=self.registrar_usuario)
        register_button.pack(pady=10)
        # Botón para volver al inicio
        back_button = tk.Button(self, text="Volver al Inicio", command=lambda: self.controller.show_frame(Home))
        back_button.pack(pady=5)

    def registrar_usuario(self):
        """ Método para registrar un nuevo usuario """
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username and password:
            if self.user_manager.registrar_usuario(username, password):
                messagebox.showinfo("Éxito", "Usuario registrado exitosamente.")
                # Aquí puedes redirigir a otra pantalla o realizar otras acciones
            else:
                messagebox.showerror("Error", "El nombre de usuario ya está en uso.")
                self.controller.show_frame(Home)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un nombre de usuario y una contraseña.")
