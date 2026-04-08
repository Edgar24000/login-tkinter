import tkinter as tk
import os
from dotenv import load_dotenv

load_dotenv()

APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def capturar_credenciales():
    usuario = entrada_usuario.get()
    password = entrada_password.get()
    validar_credenciales(usuario, password)

def validar_credenciales(usuario, password):
    if usuario == APP_USER and password == APP_PASSWORD:
        mostrar_mensaje(True)
    else:
        mostrar_mensaje(False)

def mostrar_mensaje(correcto):
    if correcto:
        mensaje.config(text="Acceso correcto", fg="green")
    else:
        mensaje.config(text="Usuario o contraseña incorrectos", fg="red")

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("350x180")

# Labels
label_usuario = tk.Label(ventana, text="Usuario")
label_password = tk.Label(ventana, text="Contraseña")

# Entradas
entrada_usuario = tk.Entry(ventana)
entrada_password = tk.Entry(ventana, show="*")

# Botón
boton = tk.Button(ventana, text="Ingresar", command=capturar_credenciales)

# Mensaje
mensaje = tk.Label(ventana, text="")

# Organizar con grid()
label_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entrada_usuario.grid(row=0, column=1, padx=10, pady=10)

label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entrada_password.grid(row=1, column=1, padx=10, pady=10)

boton.grid(row=2, column=0, columnspan=2, pady=10)

mensaje.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()