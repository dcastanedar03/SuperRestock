import csv
import tkinter as tk

# Leer los productos y la cantidad de productos desde el archivo CSV
with open('productos.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv, delimiter=';')
    productos = list(lector_csv)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Stock")

# Crear la tabla con los productos y la cantidad de productos
tabla = tk.Frame(ventana)
tabla.pack()

# Encabezados de la tabla
tk.Label(tabla, text="Producto").grid(row=0, column=0, padx=10, pady=10)
tk.Label(tabla, text="Cantidad").grid(row=0, column=1, padx=10, pady=10)

# Mostrar los productos y la cantidad de productos en la tabla
for i, producto in enumerate(productos):
    tk.Label(tabla, text=producto["Producto"]).grid(row=i+1, column=0, padx=10, pady=5)
    tk.Label(tabla, text=producto["Cantidad"]).grid(row=i+1, column=1, padx=10, pady=5)

# Mostrar la ventana
ventana.mainloop()