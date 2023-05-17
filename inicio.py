import tkinter as tk
import os

# Función que se ejecuta cuando se presiona el botón 'Iniciar sesión'
def iniciar_sesion():
    root.destroy()  # Cerrar ventana principal
    os.system('python iniciosesion.py')

# Función que se ejecuta cuando se presiona el botón 'Registrarse'
def registrarse():
    root.destroy()  # Cerrar ventana principal
    os.system('python registro.py')

# Crear ventana principal
root = tk.Tk()
root.title("Bienvenido")

# Crear etiqueta de bienvenida
label_bienvenida = tk.Label(root, text="¡Bienvenido!")
label_bienvenida.grid(row=0, column=0, columnspan=2)

# Crear botón 'Iniciar sesión'
button_iniciar_sesion = tk.Button(root, text="Iniciar sesión", command=iniciar_sesion)
button_iniciar_sesion.grid(row=1, column=0)

# Crear botón 'Registrarse'
button_registrarse = tk.Button(root, text="Registrarse", command=registrarse)
button_registrarse.grid(row=1, column=1)

# Mostrar ventana
root.mainloop()
