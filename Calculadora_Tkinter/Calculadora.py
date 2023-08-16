from tkinter import * 
from tkinter.font import Font
import math
from funciones import *



ventana = Tk()
ventana.title('Calculadora')

ventana.configure(bg='black')
ventana.iconbitmap('Calculadora_Tkinter\icono.ico')
ventana.resizable(width=False, height=False)
fuente_botones =('Arial',14)
#Entrada de Texto

entrada_texto = Entry(ventana, font =('Arial', 22), justify=RIGHT, bg='black', fg='white')
entrada_texto.grid(row=0, column = 0, columnspan=4)

#Botones Numeros 0 al 9

boton0 = Button(ventana,font=fuente_botones, text= '0', width= 14 , height= 2, command= lambda: click_boton(0, entrada_texto), bg='#363636', fg='white')
boton0.grid(row = '7', column = '0',columnspan=2)

boton1 = Button(ventana, text= '1',font=fuente_botones, width= 6, height= 2, command= lambda: click_boton(1, entrada_texto), bg='#363636', fg='white')
boton1.grid(row = '6', column = '0')

boton2 = Button(ventana, text= '2',font=fuente_botones, width= 6, height= 2, command= lambda: click_boton(2, entrada_texto), bg='#363636', fg='white')
boton2.grid(row = '6', column = '1')

boton3 = Button(ventana, text= '3',font=fuente_botones, width= 6, height= 2, command= lambda: click_boton(3, entrada_texto), bg='#363636', fg='white')
boton3.grid(row = '6', column = '2')

boton4 = Button(ventana, text= '4',font=fuente_botones, width= 6, height= 2, command= lambda: click_boton(4, entrada_texto), bg='#363636', fg='white')
boton4.grid(row = '5', column = '0')

boton5 = Button(ventana, text= '5',font=fuente_botones, width= 6, height= 2, command= lambda: click_boton(5, entrada_texto), bg='#363636', fg='white')
boton5.grid(row = '5', column = '1')

boton6 = Button(ventana, text= '6',font=fuente_botones, width= 6, height= 2, command= lambda: click_boton(6, entrada_texto), bg='#363636', fg='white')
boton6.grid(row = '5', column = '2')

boton7 = Button(ventana, text= '7',font=fuente_botones, width= 6, height= 2, command= lambda: click_boton(7, entrada_texto), bg='#363636', fg='white')
boton7.grid(row = '4', column = '0')

boton8 = Button(ventana, text= '8',font=fuente_botones, width= 6, height= 2, command= lambda: click_boton(8, entrada_texto), bg='#363636', fg='white')
boton8.grid(row = '4', column = '1')

boton9 = Button(ventana, text= '9',font=fuente_botones, width= 6, height= 2, command= lambda: click_boton(9, entrada_texto), bg='#363636', fg='white')
boton9.grid(row = '4', column = '2')

#Botones Operaciones Matematicas

boton_suma = Button(ventana, text = '+',font=fuente_botones,  width=6, height=2,command= lambda: click_boton('+', entrada_texto), bg='#252525', fg='white')
boton_suma.grid(row = '5', column = '3')

boton_resta = Button(ventana, text = '-',font=fuente_botones, width= 6, height=2, command= lambda: click_boton('-', entrada_texto), bg='#252525', fg='white')
boton_resta.grid(row = '4', column = '3')

boton_multiplicacion = Button(ventana, text = 'X',font=fuente_botones, width= 6, height=2, command= lambda: click_boton('*', entrada_texto), bg='#252525', fg='white')
boton_multiplicacion.grid(row = '3', column = '3')

boton_division = Button(ventana, text = '/',font=fuente_botones, width= 6, height=2, command= lambda: click_boton('/', entrada_texto), bg='#252525', fg='white')
boton_division.grid(row = '3', column = '2')

boton_potencia = Button(ventana, text='^',font=fuente_botones,width= 6, height=2, command= lambda: click_boton('^', entrada_texto), bg='#252525', fg='white')
boton_potencia.grid(row='3', column='1')

boton_raiz = Button(ventana, text='√',font=fuente_botones, width=6, height=2, command=lambda: click_boton('√', entrada_texto), bg='#252525', fg='white')
boton_raiz.grid(row='3', column='0')

#Botones Extra

boton_igual = Button(ventana, text = '=',font=fuente_botones, width= 6, height=5, command= lambda: resultado(entrada_texto.get(),entrada_texto, ventana), bg='#2C94BE', fg='white')
boton_igual.grid(row = '6', column = '3',rowspan=2)

boton_borrar = Button(ventana, text = 'AC',font=fuente_botones, width= 6, height=2, command= lambda: borrar(entrada_texto), bg='#252525', fg='white')
boton_borrar.grid(row = '2', column = '0')

boton_borrar_uno = Button(ventana, text='←',font=fuente_botones, width=6, height=2,command= lambda: borrar_uno(entrada_texto), bg='#252525', fg='white')
boton_borrar_uno.grid(row='2', column='3')

boton_parentesis1 = Button(ventana, text = '(',font=fuente_botones, width= 6, height=2, command= lambda: click_boton('(', entrada_texto), bg='#252525', fg='white')
boton_parentesis1.grid(row = '2', column = '1')

boton_parentesis2 = Button(ventana, text = ')',font=fuente_botones, width= 6, height=2, command= lambda: click_boton(')', entrada_texto), bg='#252525', fg='white')
boton_parentesis2.grid(row = '2', column = '2')

boton_punto = Button(ventana, text = '.',font=fuente_botones, width= 6, height=2, command= lambda: click_boton('.', entrada_texto), bg='#252525', fg='white')
boton_punto.grid(row = '7', column = '2')



ventana.mainloop()