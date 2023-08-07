from tkinter import * 
import math
from funciones import *

ventana = Tk()
ventana.title('Calculadora')

#Entrada de Texto

entrada_texto = Entry(ventana, font = ('Calibri 20'))
entrada_texto.grid(row=0, column = 0, columnspan = 4, padx = 5, pady = 5 )

#Botones Numeros 0 al 9

boton0 = Button(ventana, text= '0', width= 13 , height= 2, command= lambda: click_boton(0, entrada_texto))
boton0.grid(row = '5', column = '0',columnspan=2, padx = 5, pady = 5)

boton1 = Button(ventana, text= '1', width= 5, height= 2, command= lambda: click_boton(1, entrada_texto))
boton1.grid(row = '4', column = '0', padx = 5, pady = 5)

boton2 = Button(ventana, text= '2', width= 5, height= 2, command= lambda: click_boton(2, entrada_texto))
boton2.grid(row = '4', column = '1', padx = 5, pady = 5)

boton3 = Button(ventana, text= '3', width= 5, height= 2, command= lambda: click_boton(3, entrada_texto))
boton3.grid(row = '4', column = '2', padx = 5, pady = 5)

boton4 = Button(ventana, text= '4', width= 5, height= 2, command= lambda: click_boton(4, entrada_texto))
boton4.grid(row = '3', column = '0', padx = 5, pady = 5)

boton5 = Button(ventana, text= '5', width= 5, height= 2, command= lambda: click_boton(5, entrada_texto))
boton5.grid(row = '3', column = '1', padx = 5, pady = 5)

boton6 = Button(ventana, text= '6', width= 5, height= 2, command= lambda: click_boton(6, entrada_texto))
boton6.grid(row = '3', column = '2', padx = 5, pady = 5)

boton7 = Button(ventana, text= '7', width= 5, height= 2, command= lambda: click_boton(7, entrada_texto))
boton7.grid(row = '2', column = '0', padx = 5, pady = 5)

boton8 = Button(ventana, text= '8', width= 5, height= 2, command= lambda: click_boton(8, entrada_texto))
boton8.grid(row = '2', column = '1', padx = 5, pady = 5)

boton9 = Button(ventana, text= '9', width= 5, height= 2, command= lambda: click_boton(9, entrada_texto))
boton9.grid(row = '2', column = '2', padx = 5, pady = 5)

#Botones Operaciones Matematicas

boton_suma = Button(ventana, text = '+', width= 5, height=2, command= lambda: click_boton('+', entrada_texto))
boton_suma.grid(row = '3', column = '3', padx = 5, pady = 5)

boton_resta = Button(ventana, text = '-', width= 5, height=2, command= lambda: click_boton('-', entrada_texto))
boton_resta.grid(row = '4', column = '3', padx = 5, pady = 5)

boton_multiplicacion = Button(ventana, text = '*', width= 5, height=2, command= lambda: click_boton('*', entrada_texto))
boton_multiplicacion.grid(row = '2', column = '3', padx = 5, pady = 5)

boton_division = Button(ventana, text = '/', width= 5, height=2, command= lambda: click_boton('/', entrada_texto))
boton_division.grid(row = '1', column = '3', padx = 5, pady = 5)

boton_potencia = Button(ventana, text='^',width= 5, height=2, command= lambda: click_boton('^', entrada_texto))
boton_potencia.grid(row='1', column='4', padx=5, pady=5)

boton_raiz = Button(ventana, text='√', width=5, height=2, command=lambda: click_boton('√', entrada_texto))
boton_raiz.grid(row='2', column='4', padx=5, pady=5)

#Botones Extra

boton_igual = Button(ventana, text = '=', width= 5, height=2, command= lambda: resultado(entrada_texto.get(),entrada_texto, ventana))
boton_igual.grid(row = '5', column = '3', padx = 5, pady = 5)

boton_borrar = Button(ventana, text = 'AC', width= 5, height=2, command= lambda: borrar(entrada_texto))
boton_borrar.grid(row = '1', column = '0', padx = 5, pady = 5)

boton_parentesis1 = Button(ventana, text = '(', width= 5, height=2, command= lambda: click_boton('(', entrada_texto))
boton_parentesis1.grid(row = '1', column = '1', padx = 5, pady = 5)

boton_parentesis2 = Button(ventana, text = ')', width= 5, height=2, command= lambda: click_boton(')', entrada_texto))
boton_parentesis2.grid(row = '1', column = '2', padx = 5, pady = 5)

boton_punto = Button(ventana, text = '.', width= 5, height=2, command= lambda: click_boton('.', entrada_texto))
boton_punto.grid(row = '5', column = '2', padx = 5, pady = 5)



ventana.mainloop()