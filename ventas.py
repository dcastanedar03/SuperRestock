import tkinter as tk
import csv

# Cargar el archivo de ventas existente o crear uno nuevo si no existe
try:
    with open('ventas.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')
        ventas = {fila['producto']: int(fila['cantidad_vendida']) for fila in lector_csv}
except FileNotFoundError:
    ventas = {}

# Crear la ventana
ventana = tk.Tk()
ventana.title("Vender stock")

# Crear la etiqueta y el menú desplegable
etiqueta = tk.Label(ventana, text="Qué producto se ha vendido?")
etiqueta.pack()
opcion = tk.StringVar(ventana)
opcion.set("Plátanos") # opción por defecto
productos = []
with open('productos.csv', 'r', newline='') as archivo_csv:
    lector_csv = csv.DictReader(archivo_csv, delimiter=';')
    for fila in lector_csv:
        productos.append(fila['Producto'])
menu = tk.OptionMenu(ventana, opcion, *productos)
menu.pack()

# Crear el campo para escribir el número de unidades
etiqueta2 = tk.Label(ventana, text="Número de unidades:")
etiqueta2.pack()
entrada = tk.Entry(ventana)
entrada.pack()

# Crear el botón de enviar
def procesar_solicitud():
    producto = opcion.get()
    cantidad = int(entrada.get())
    
    # Actualizar el contador de ventas
    if producto in ventas:
        ventas[producto] += cantidad
    else:
        ventas[producto] = cantidad
    
    with open('ventas.csv', 'a', newline='') as archivo_csv:
        encabezados = ['producto', 'cantidad_vendida']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados, delimiter=';')
        if archivo_csv.tell() == 0:
            escritor_csv.writeheader()
        escritor_csv.writerow({'producto': producto, 'cantidad_vendida': cantidad})
    
    with open('productos.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')
        filas = list(lector_csv)

    with open('productos.csv', 'w', newline='') as archivo_csv:
        encabezados = ['Producto', 'Cantidad']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados, delimiter=';')
        escritor_csv.writeheader()

        for fila in filas:
            if fila['Producto'] == producto:
                fila['Cantidad'] = int(fila['Cantidad']) - cantidad
            escritor_csv.writerow(fila)

    mensaje.config(text=f"Se han vendido {cantidad} unidades de {producto}")

boton = tk.Button(ventana, text="Enviar", command=procesar_solicitud)
boton.pack()

mensaje = tk.Label(ventana, text="")
mensaje.pack()

# Mostrar la ventana
ventana.mainloop()
