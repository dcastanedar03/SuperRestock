import tkinter as tk
from tkinter import messagebox
import csv

# Crear la ventana
ventana = tk.Tk()
ventana.title("Checker de stock")

# Crear la etiqueta y los botones
etiqueta = tk.Label(ventana, text="¿Ha llegado bien el stock?")
etiqueta.pack()

def stock_bien():
    messagebox.showinfo("Información", "Se ha procesado su aviso de comprobación de stock")
    ventana.destroy()  

def stock_mal():
    etiqueta2 = tk.Label(ventana, text="¿Qué producto ha llegado defectuoso?")
    etiqueta2.pack()
    opcion = tk.StringVar(ventana)
    opcion.set("Plátanos") # opción por defecto
    menu = tk.OptionMenu(ventana, opcion, "Plátanos", "Naranjas", "Pepino", "Leche")
    menu.pack()

    etiqueta3 = tk.Label(ventana, text="Número de unidades defectuosas:")
    etiqueta3.pack()
    entrada = tk.Entry(ventana)
    entrada.pack()

    def procesar_solicitud():
        producto = opcion.get()
        cantidad = entrada.get()

        # Escribir en el archivo CSV
        with open('productos_defectuosos.csv', 'a', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow([producto, cantidad])

        messagebox.showinfo("Información", "Se ha procesado su aviso de comprobación de stock")

    boton = tk.Button(ventana, text="Enviar", command=procesar_solicitud)
    boton.pack()

# Crear los botones "sí" y "no"
boton_si = tk.Button(ventana, text="Sí", command=stock_bien)
boton_si.pack(side="left", padx=10)

boton_no = tk.Button(ventana, text="No", command=stock_mal)
boton_no.pack(side="right", padx=10)

# Mostrar la ventana
ventana.mainloop()
