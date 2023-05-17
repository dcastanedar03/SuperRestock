import tkinter as tk
import csv
import os

# Función que se ejecuta cuando se presiona el botón 'Crear usuario'
def crear_usuario():
    username = entry_username.get()
    password = entry_password.get()
    repeat_password = entry_repeat_password.get()
    rol = variable_rol.get()
    # Verificar si el archivo CSV existe y crearlo si no existe
    if not os.path.exists('usuarios.csv'):
        with open('usuarios.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password', 'rol'])
    
    # Verificar si las contraseñas coinciden
    if password != repeat_password:
        error_label.config(text="Las contraseñas no coinciden.")
        return
    
    # Verificar si el usuario ya existe en el archivo CSV
    with open('usuarios.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                error_label.config(text="El usuario ya existe.")
                return
    
    # Abrir archivo CSV y escribir datos
    with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, rol])
        
    # Cerrar ventana actual y abrir ventana de confirmación
    root.destroy()
    os.system('python iniciosesion.py')

# Crear ventana principal
root = tk.Tk()
root.title("Crear usuario")

# Crear etiqueta de nombre de usuario
label_username = tk.Label(root, text="Nombre de usuario:")
label_username.grid(row=0, column=0)

# Crear cuadro de entrada de nombre de usuario
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)

# Crear etiqueta de contraseña
label_password = tk.Label(root, text="Contraseña:")
label_password.grid(row=1, column=0)

# Crear cuadro de entrada de contraseña
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)

# Crear etiqueta de repetir contraseña
label_repeat_password = tk.Label(root, text="Repetir contraseña:")
label_repeat_password.grid(row=2, column=0)

# Crear cuadro de entrada de repetir contraseña
entry_repeat_password = tk.Entry(root, show="*")
entry_repeat_password.grid(row=2, column=1)

# Crear etiqueta de rol
label_rol = tk.Label(root, text="Rol:")
label_rol.grid(row=3, column=0)

# Crear menú desplegable de rol
roles = ["Gestor", "Personal de almacén", "Personal de tienda"]
variable_rol = tk.StringVar(root)
variable_rol.set(roles[0]) # Establecer valor predeterminado
menu_rol = tk.OptionMenu(root, variable_rol, *roles)
menu_rol.grid(row=3, column=1)

# Crear botón 'Crear usuario'
button_crear = tk.Button(root, text="Crear usuario", command=crear_usuario)
button_crear.grid(row=4, column=1)

# Crear etiqueta de error
error_label = tk.Label(root, text="", fg="red")
error_label.grid(row=5, column=0, columnspan=2)

# Mostrar ventana
root.mainloop()
