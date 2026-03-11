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

tk.Label(ventana, text="Usuario").pack()
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()

tk.Label(ventana, text="Contraseña").pack()
entrada_password = tk.Entry(ventana, show="*")
entrada_password.pack()

boton = tk.Button(ventana, text="Ingresar", command=capturar_credenciales)
boton.pack()

mensaje = tk.Label(ventana, text="")
mensaje.pack()

ventana.mainloop()
