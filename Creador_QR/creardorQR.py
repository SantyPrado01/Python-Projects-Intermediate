import qrcode
import tkinter as tk
from tkinter import filedialog

def generar_codigo():
    link = entry_link.get()
    codigo = qrcode.make(link)
    guardar_ruta = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos PNG", "*.png")])
    if guardar_ruta:
        codigo.save(guardar_ruta)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Código QR")
ventana.geometry('300x200')

# Etiqueta y campo de entrada para el link
label_link = tk.Label(ventana, text="Ingrese el link del código a generar:")
label_link.pack()

entry_link = tk.Entry(ventana)
entry_link.pack()

# Botón para generar el código QR
btn_generar = tk.Button(ventana, text="Generar Código QR", command=generar_codigo)
btn_generar.pack()

ventana.mainloop()

