import random
import string
import tkinter as tk

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def mostrar_contraseña():
    try:
        longitud = int(entry_longitud.get())
        if longitud <= 0:
            raise ValueError
        contraseña = generar_contraseña(longitud)
        label_contraseña.config(text=f"Tu contraseña es: {contraseña}")
    except ValueError:
        label_contraseña.config(text="Por favor, introduce un número válido.")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("300x200")  # Tamaño fijo
ventana.resizable(False, False)  # Deshabilitar redimensionamiento

# Etiqueta y campo de entrada centrados
label = tk.Label(ventana, text="Longitud de la contraseña:")
label.pack(pady=10)

entry_longitud = tk.Entry(ventana, justify='center')  # Centrar texto en el Entry
entry_longitud.pack(pady=5)

# Botón para generar contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=mostrar_contraseña)
boton_generar.pack(pady=20)

# Etiqueta para mostrar la contraseña generada
label_contraseña = tk.Label(ventana, text="", wraplength=250)
label_contraseña.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()