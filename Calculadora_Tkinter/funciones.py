import sqlite3
import math
from tkinter import *

# Conexión a la base de datos (creará un archivo si no existe)
base_datos = sqlite3.connect('Calculadora_Tkinter/historial.bd')

# Crear tabla de tareas si no existe
base_datos.execute('''
    CREATE TABLE IF NOT EXISTS historial (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cuenta TEXT NOT NULL,
        resultado TEXT NOT NULL
    )
''')


base_datos.commit()
base_datos.close()

i = 0

def click_boton(valor, entrada_texto):
    global i
    entrada_texto.insert(i, valor)
    i += 1
    return i

def borrar(entrada_texto):
    entrada_texto.delete(0,END)
    i = 0
    return i

def borrar_uno(entrada_texto):
	global i 
	if i==-1:
		pass
	else:
		entrada_texto.delete(i,last =None)
		i-=1

def resultado(ecuacion, entrada_texto, ventana):
    ecuacion = entrada_texto.get()
    # Reemplazar '^' por '**'
    ecuacion = ecuacion.replace('^', '**') 
    
    try:
        igual = eval(ecuacion)
        entrada_texto.delete(0, END)
        entrada_texto.insert(0, igual)
        i = 0
    except:
        # Verificar si hay una raíz cuadrada
        try:
            if '√' in ecuacion: 
                # Reemplazar para la función sqrt 
                ecuacion = ecuacion.replace('√', 'math.sqrt(')  
                igual = eval(ecuacion+')')
                
                entrada_texto.delete(0, END)
                entrada_texto.insert(0, igual)
                i = 0
            else:
                entrada_texto.delete(0, END)
                entrada_texto.insert(0, "Error")
                i = 0
        except:
            entrada_texto.delete(0, END)
            entrada_texto.insert(0, "Error")
            i = 0

    conn = sqlite3.connect('Calculadora_Tkinter/historial.bd')
    conn.execute('INSERT INTO historial (cuenta, resultado) VALUES (?, ?)', (ecuacion, igual))
    conn.commit()
    conn.close()
    mostrar_historial(ventana)
    return(igual, i)


# Función para mostrar el historial
def mostrar_historial(ventana):
    boton_eliminar_historial = Button(ventana, text='Eliminar Historial', command= lambda: eliminar_historial(ventana))
    boton_eliminar_historial.grid(row='5', column='5')

    conn = sqlite3.connect('Calculadora_Tkinter/historial.bd')
    cursor = conn.execute('SELECT * FROM historial')
    historial = cursor.fetchall()
    conn.close()
    
    texto_mostrar = Label(ventana, text='Historial:')
    texto_mostrar.grid(row=0, column=5)
    # Usar un índice para la posición de la fila en la ventana
    fila = 1
    
    for registro in historial:
        id, cuenta, resultado = registro  # Desempaquetar la tupla del registro
        
        etiqueta_cuenta = Label(ventana, text=f'{cuenta}')
        etiqueta_resultado = Label(ventana, text=f'Resultado: {resultado}')
        
        etiqueta_cuenta.grid(row=fila, column=5, sticky=W)
        etiqueta_resultado.grid(row=fila, column=6, sticky=W)
        
        fila += 1

def eliminar_historial(ventana):
    conn = sqlite3.connect('Calculadora_Tkinter/historial.bd')
    conn.execute('DELETE FROM historial')
    conn.commit()
    conn.close()
    mostrar_historial(ventana)
    