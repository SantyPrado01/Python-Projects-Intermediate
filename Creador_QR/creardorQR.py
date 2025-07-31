import qrcode
from reportlab.graphics import renderPS
from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib import colors  # <- Importar colores correctamente
from tkinter import Tk, Entry, Label, Button, filedialog

def generar_codigo_vectorial():
    link = entry_link.get()

    # Crear QR como matriz
    qr = qrcode.QRCode(box_size=10, border=0)
    qr.add_data(link)
    qr.make(fit=True)
    matrix = qr.get_matrix()

    size = len(matrix)
    box_size = 10
    drawing = Drawing(width=size * box_size, height=size * box_size)

    # Dibujar cuadrados negros como vectores
    for y in range(size):
        for x in range(size):
            if matrix[y][x]:
                rect = Rect(
                    x * box_size,
                    (size - y - 1) * box_size,  # Invertir eje Y
                    box_size,
                    box_size,
                    fillColor=colors.black,  # <- Color correcto
                    strokeWidth=0
                )
                drawing.add(rect)

    # Guardar archivo EPS
    guardar_ruta = filedialog.asksaveasfilename(
        defaultextension=".eps",
        filetypes=[("Archivo EPS", "*.eps")]
    )

    if guardar_ruta:
        renderPS.drawToFile(drawing, guardar_ruta, '')

# Interfaz
ventana = Tk()
ventana.title("Generador de QR Vectorial")
ventana.geometry('300x200')

Label(ventana, text="Ingrese el link del código a generar:").pack(pady=10)
entry_link = Entry(ventana)
entry_link.pack()

Button(ventana, text="Generar QR EPS (Vector)", command=generar_codigo_vectorial).pack(pady=10)

ventana.mainloop()
