import tkinter as tk
import csv
import os

# Función que se ejecuta cuando se presiona el botón 'Iniciar sesión'
def abrir_menu():
    # Obtener usuario y contraseña ingresados
    username = entry_username.get()
    password = entry_password.get()

    # Verificar si el archivo CSV existe y crearlo si no existe
    if not os.path.exists('usuarios.csv'):
        error_label.config(text="No hay usuarios registrados.")
        return
    
    # Verificar si el usuario existe en el archivo CSV
    with open('usuarios.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                if row[1] == password:
                    if row[2] == "Gestor":
                        root.destroy()  # Cerrar ventana principal
                        os.system('python menugestor.py')
                        return
                    elif row[2] == "Personal de almacén":
                        root.destroy()  # Cerrar ventana principal
                        os.system('python menualmacen.py')
                        return
                    elif row[2] == "Personal de tienda":
                        root.destroy()  # Cerrar ventana principal
                        os.system('python menutienda.py')
                        return
                    else:
                        error_label.config(text="Rol desconocido.")
                        return
    
    error_label.config(text="Usuario o contraseña incorrectos.")
    

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

# Crear etiqueta de nombre de usuario
label_username = tk.Label(root, text="Nombre de usuario:")
label_username.grid(row=1, column=0)

# Crear cuadro de entrada de nombre de usuario
entry_username = tk.Entry(root)
entry_username.grid(row=1, column=1)

# Crear etiqueta de contraseña
label_password = tk.Label(root, text="Contraseña:")
label_password.grid(row=2, column=0)

# Crear cuadro de entrada de contraseña
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1)

# Crear botón 'Iniciar sesión'
button_iniciar_sesion = tk.Button(root, text="Entrar", command=abrir_menu)
button_iniciar_sesion.grid(row=3, column=1)

# Crear botón 'Registrarse'
button_registrarse = tk.Button(root, text="Registrarse", command=registrarse)
button_registrarse.grid(row=3, column=0)

# Crear etiqueta de error
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=4, column=0, columnspan=2)

# Mostrar ventana
root.mainloop()
