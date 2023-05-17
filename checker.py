import tkinter as tk

PRODUCTOS = ["Platanos", "Naranjas", "Pepino", "Leche"]

class CheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Verificación de productos")

        # Crear la etiqueta "¿Ha llegado bien su pedido?"
        self.label = tk.Label(master, text="¿Ha llegado bien su pedido?", font=("Arial", 16))
        self.label.pack(pady=20)

        # Crear el botón "Sí"
        self.button_yes = tk.Button(master, text="Sí", font=("Arial", 14), command=self.confirm)
        self.button_yes.pack(side=tk.LEFT, padx=20)

        # Crear el botón "No"
        self.button_no = tk.Button(master, text="No", font=("Arial", 14), command=self.show_options)
        self.button_no.pack(side=tk.RIGHT, padx=20)

    def confirm(self):
        # Mostrar un mensaje de confirmación
        tk.messagebox.showinfo("Verificación de productos", "Gracias por confirmar que ha recibido su pedido correctamente.")

        # Cerrar la ventana
        self.master.destroy()

    def show_options(self):
        # Ocultar los botones "Sí" y "No"
        self.button_yes.pack_forget()
        self.button_no.pack_forget()

        # Crear la etiqueta "Seleccione el producto que ha llegado mal"
        self.label = tk.Label(self.master, text="Seleccione el producto que ha llegado mal:", font=("Arial", 16))
        self.label.pack(pady=20)

        # Crear el cuadro de selección de productos
        self.producto_var = tk.StringVar()
        self.producto_var.set(PRODUCTOS[0])
        self.producto_menu = tk.OptionMenu(self.master, self.producto_var, *PRODUCTOS)
        self.producto_menu.pack(pady=10)

        # Crear la entrada de cantidad
        self.cantidad_var = tk.StringVar()
        self.cantidad_entry = tk.Entry(self.master, textvariable=self.cantidad_var, font=("Arial", 14))
        self.cantidad_entry.pack(pady=10)

        # Crear el botón "Aceptar"
        self.button_accept = tk.Button(self.master, text="Aceptar", font=("Arial", 14), command=self.submit)
        self.button_accept.pack(pady=20)

    def submit(self):
        # Obtener los valores seleccionados
        producto = self.producto_var.get()
        cantidad = self.cantidad_var.get()

        # Mostrar un mensaje de confirmación
        tk.messagebox.showinfo("Verificación de productos", f"Se ha registrado que {cantidad} unidades del producto {producto} han llegado mal.")

        # Cerrar la ventana
        self.master.destroy()

# Crear la ventana principal
root = tk.Tk()

# Crear la aplicación
app = CheckerApp(root)

# Mostrar la ventana
root.mainloop()
