import tkinter as tk
import csv

# Función para procesar la solicitud de reabastecimiento
def procesar_solicitud():
    # Obtener el producto y la cantidad
    producto = opcion.get()
    cantidad = int(entrada.get())

    # Leer los productos y cantidades del archivo CSV
    productos = leer_archivo_csv()

    # Actualizar la cantidad del producto seleccionado
    productos[producto] += cantidad

    # Escribir los productos y cantidades actualizados al archivo CSV
    escribir_archivo_csv(productos)

    # Mostrar mensaje de confirmación
    mensaje.config(text=f"Se han reabastecido {cantidad} unidades de {producto}")

# Función para leer los productos y cantidades del archivo CSV
def leer_archivo_csv():
    with open('productos.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')
        productos = {}
        for fila in lector_csv:
            productos[fila['Producto']] = int(fila['Cantidad'])
        return productos

# Función para escribir los productos y cantidades al archivo CSV
def escribir_archivo_csv(productos):
    with open('productos.csv', 'w', newline='') as archivo_csv:
        encabezados = ['Producto', 'Cantidad']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados, delimiter=';')
        escritor_csv.writeheader()
        for producto, cantidad in productos.items():
            escritor_csv.writerow({'Producto': producto, 'Cantidad': cantidad})

# Crear la ventana
ventana = tk.Tk()
ventana.title("Reabastecer stock")

# Crear la etiqueta y el menú desplegable
etiqueta = tk.Label(ventana, text="Qué producto deseas reabastecer?")
etiqueta.pack()
opcion = tk.StringVar(ventana)
opcion.set("Plátanos") # opción por defecto
productos = leer_archivo_csv()
menu = tk.OptionMenu(ventana, opcion, *productos.keys())
menu.pack()

# Crear el campo para escribir el número de unidades
etiqueta2 = tk.Label(ventana, text="Número de unidades:")
etiqueta2.pack()
entrada = tk.Entry(ventana)
entrada.pack()

# Crear el botón de enviar
boton = tk.Button(ventana, text="Enviar", command=procesar_solicitud)
boton.pack()

# Crear la etiqueta para mostrar mensajes de confirmación
mensaje = tk.Label(ventana, text="")
mensaje.pack()

# Mostrar la ventana
ventana.mainloop()
