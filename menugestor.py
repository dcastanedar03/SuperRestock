import tkinter as tk
import csv
import os

def añadir_stock():
    os.system('python reabastecer.py')

def modificar_stock():
    os.system('python modificar.py')

def resumen():
    os.system('python resumen.py')

def stock():
    os.system('python stock.py')

def avisos():
    os.system('python avisos.py')

def inicio():
    root.destroy() 
    os.system('python inicio.py')

def reiniciar_ventas():
    with open('ventas.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=';')
        escritor_csv.writerow(['producto', 'cantidad_vendida'])
    with open('productos_defectuosos.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=',')
    reiniciar_avisos() # Llama a la función que reinicia los avisos

def reiniciar_avisos():
    # Código para reiniciar los avisos
    pass # Reemplaza esta línea con el código correspondiente

# Crear la ventana principal
root = tk.Tk()
root.title("Menu principal")

# Crear la etiqueta "Que deseas hacer?"
label = tk.Label(root, text="Que deseas hacer?", font=("Arial", 16))
label.pack(pady=20)

# Crear los botones
button_add_stock = tk.Button(root, text="Añadir stock", font=("Arial", 14), command=añadir_stock)
button_modify_stock = tk.Button(root, text="Modificar Stock", font=("Arial", 14), command=modificar_stock)
button_daily_sales = tk.Button(root, text="Resumen de ventas diario", font=("Arial", 14), command=resumen)
button_reset_sales = tk.Button(root, text="Reiniciar ventas diarias", font=("Arial", 14), command=reiniciar_ventas)
button_alerts = tk.Button(root, text="Avisos", font=("Arial", 14), command=avisos) # Agrega el parámetro command aquí
button_stock = tk.Button(root, text="Ver stock", font=("Arial", 14), command=stock)
button_close = tk.Button(root, text="Cerrar", font=("Arial", 14), command=inicio)

# Colocar los botones en la ventana
button_add_stock.pack()
button_modify_stock.pack()
button_daily_sales.pack()
button_reset_sales.pack()
button_alerts.pack()
button_stock.pack()
button_close.pack(pady=20)

# Mostrar la ventana
root.mainloop()

