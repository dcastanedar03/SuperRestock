import tkinter as tk
import csv

# Cargar los datos de ventas y productos
ventas = {}
with open('ventas.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv, delimiter=';')
    ventas = {fila['producto']: int(fila['cantidad_vendida']) for fila in lector_csv}

productos = {}
with open('productos.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv, delimiter=';')

    productos = {fila['Producto']: int(fila['Cantidad']) for fila in lector_csv}

comprobacion = {}
with open('productos_defectuosos.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter=',')
    productos_defectuosos = {fila[0]: int(fila[1]) for fila in lector_csv if fila}
  

# Crear la ventana
ventana = tk.Tk()
ventana.title("Avisos")

# Crear la etiqueta para mostrar los productos vendidos
etiqueta_vendidos = tk.Label(ventana, text="Productos vendidos:")
etiqueta_vendidos.pack()

lista_vendidos = tk.Listbox(ventana)
for producto, cantidad in ventas.items():
    lista_vendidos.insert(tk.END, f"{producto}: {cantidad}")
lista_vendidos.pack()

# Crear la etiqueta para mostrar los productos en mal estado
etiqueta_mal_estado = tk.Label(ventana, text="Productos en mal estado:")
etiqueta_mal_estado.pack()

lista_mal_estado = tk.Listbox(ventana)
for producto, cantidad in productos_defectuosos.items():
    lista_mal_estado.insert(tk.END, f"{producto}: {cantidad}")
lista_mal_estado.pack()

# Crear la etiqueta para mostrar los productos con baja cantidad
etiqueta_baja_cantidad = tk.Label(ventana, text="Productos con baja cantidad:")
etiqueta_baja_cantidad.pack()

lista_baja_cantidad = tk.Listbox(ventana)
for producto, cantidad in productos.items():
    if cantidad < 10:
        lista_baja_cantidad.insert(tk.END, f"{producto}: {cantidad}")
lista_baja_cantidad.pack()

# Mostrar la ventana
ventana.mainloop()
