from tkinter import *
from tkinter import messagebox,filedialog,ttk,PhotoImage #libreria IMPRESCINDIBLE para meter ventanas emergentes
from PIL import Image,ImageTk,ImageDraw #libreria que necesito para imagenes
import openpyxl

#Definición de variables globales

raiz=Tk()

prueba=StringVar()

libro = openpyxl.load_workbook('C:/Users/jose.velazquez/Downloads/Prueba.xlsx')
hoja = libro['Datos']

ancho_ventana = 500 #ancho de la ventana
alto_ventana = 250 #alto de la ventana


def inserta_proyecto(num,hoja):
    hoja.append({"E":num})    

x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2 #posición del ancho de la ventana
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2 #posición del alto de la ventana

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana) #determinación de la posición de la pantalla

prueba.set("")

pregunta=Label(raiz, text="Inserta un nuevo proyecto")
pregunta.place(x=50,y=75)
cuadro=Entry(raiz,textvariable=prueba)
cuadro.place(x=215,y=75)
boton=Button(raiz,text="Actualizar",command=lambda: inserta_proyecto(cuadro.get(),hoja))
boton.place(x=200,y=120)



raiz.geometry(posicion)
raiz.resizable(0,0)



raiz.mainloop()