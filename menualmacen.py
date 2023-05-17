import tkinter as tk
import csv
import os

def checker_stock():
    os.system('python comprobacion.py')

def stock():
    os.system('python stock.py')

def inicio():
    root.destroy() 
    os.system('python inicio.py')

# Crear la ventana principal
root = tk.Tk()
root.title("Menu principal")

# Crear la etiqueta "Que deseas hacer?"
label = tk.Label(root, text="Que deseas hacer?", font=("Arial", 16))
label.pack(pady=20)

# Crear los botones
button_stock_checker = tk.Button(root, text="Checker stock", font=("Arial", 14), command=checker_stock)
button_stock = tk.Button(root, text="Ver stock", font=("Arial", 14), command=stock)
button_close = tk.Button(root, text="Cerrar", font=("Arial", 14), command=inicio)

# Colocar los botones en la ventana
button_stock_checker.pack()
button_stock.pack()
button_close.pack(pady=20)

# Mostrar la ventana
root.mainloop()

