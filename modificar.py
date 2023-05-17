import csv
import tkinter as tk

def leer_archivo_csv():
    productos = {}
    with open('productos.csv', 'r', newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv, delimiter=';')
        for fila in lector_csv:
            productos[fila['Producto']] = int(fila['Cantidad'])
    return productos

def escribir_archivo_csv(productos):
    with open('productos.csv', 'w', newline='') as archivo_csv:
        encabezados = ['Producto', 'Cantidad']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados, delimiter=';')
        escritor_csv.writeheader()
        for producto, cantidad in productos.items():
            escritor_csv.writerow({'Producto': producto, 'Cantidad': cantidad})

def modificar_cantidad():
    producto = opcion.get()
    cantidad = cantidad_modificar.get()

    productos = leer_archivo_csv()
    productos[producto] = int(cantidad)
    escribir_archivo_csv(productos)

    mensaje.config(text=f"La cantidad de {producto} ha sido actualizada a {cantidad}")

# Crear archivo CSV con productos y cantidad 0 si no existe
try:
    with open('productos.csv', 'r'):
        pass
except FileNotFoundError:
    with open('productos.csv', 'w', newline='') as archivo_csv:
        encabezados = ['Producto', 'Cantidad']
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=encabezados, delimiter=';')
        escritor_csv.writeheader()
        productos = ['Plátanos', 'Naranjas', 'Pepino', 'Leche']
        for producto in productos:
            escritor_csv.writerow({'Producto': producto, 'Cantidad': 0})

# Crear interfaz gráfica
ventana = tk.Tk()
ventana.title("Modificar stock")
etiqueta = tk.Label(ventana, text="Qué producto deseas modificar?")
etiqueta.pack()
opcion = tk.StringVar()
opcion.set('Plátanos')
productos = leer_archivo_csv().keys()
menu = tk.OptionMenu(ventana, opcion, *productos)
menu.pack()
etiqueta2 = tk.Label(ventana, text="Número de unidades:")
etiqueta2.pack()
cantidad_modificar = tk.Entry(ventana)
cantidad_modificar.pack()

boton = tk.Button(ventana, text="Modificar cantidad", command=modificar_cantidad)
boton.pack()

mensaje = tk.Label(ventana, text="")
mensaje.pack()

ventana.mainloop()
