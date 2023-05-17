import tkinter as tk
import csv

# Crear la ventana
ventana = tk.Tk()
ventana.title("Resumen de ventas")

# Leer el archivo CSV
ventas = {}
with open('ventas.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv, delimiter=';')
    for fila in lector_csv:
        producto = fila['producto']
        cantidad = int(fila['cantidad_vendida'])
        if producto in ventas:
            ventas[producto] += cantidad
        else:
            ventas[producto] = cantidad

# Mostrar la tabla en una etiqueta
tabla = "Producto,Cantidad vendida\n"
for producto, cantidad in ventas.items():
    tabla += f"{producto}\t{cantidad}\n"

etiqueta = tk.Label(ventana, text=tabla)
etiqueta.pack()

# Mostrar la ventana
ventana.mainloop()
