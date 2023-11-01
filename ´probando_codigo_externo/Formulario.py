# Registro de datos en excel desde una GUI en Tkinter 
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

"""
	1. a este código me gustaría agregarle una function para ir agregando datos sin requerir
	crear un archivo nuevo
	2. Me gustaría cambiar la interfaz gráfica por una que se adecue más a mi objetivo
	3. quiero agregarle un retorno en gráfico del seguimiento de los datos entregados
	4. quiero cambiar el método de entrada a opciones predefinidas para generar estadística
	"""

from tkinter import Tk, Label, Button, Entry, Frame, END
import pandas as pd

ventana = Tk()
ventana.config(bg='black')
ventana.geometry('560x388')
ventana.resizable(None, None)
ventana.title('Guardar datos en Excel')
nombre1, apellido1, edad1, correo1, telefono1 = [], [], [], [], []


def get_data(file):
    data = pd.read_excel(file)
    return data

def get_empty_row(data):
    for i in range(len(data.index)+1):
        row = data.loc[i]
        if row.isnull().all():
            return row.name
    return len(data.index)

def save_data(data, file):
    writer = pd.ExcelWriter(file, engine='openpyxl')
    data.to_excel(writer, index=False)
    writer.save()
    
def add_data(file, new_data):
    data = get_data(file)
    empty_row = get_empty_row(data)
    for i, col in enumerate(data.columns):
        data.at[empty_row, col] = new_data[i]
    save_data(data, file)


def agregar_datos():
	global nombre1, apellido1, dni1, correo1, telefono1
	nombre1.append(ingresa_nombre.get())
	apellido1.append(ingresa_apellido.get())
	edad1.append(ingresa_edad.get())
	correo1.append(ingresa_correo.get())
	telefono1.append(ingresa_telefono.get())
	ingresa_nombre.delete(0, END)
	ingresa_apellido.delete(0, END)
	ingresa_edad.delete(0, END)
	ingresa_correo.delete(0, END)
	ingresa_telefono.delete(0, END)


def guardar_datos():  # esta funcion guarda los datos
	global nombre1, apellido1, edad1, correo1, telefono1
	datos = {'Nombres': nombre1, 'Apellidos': apellido1, 'Edad': edad1, 'Correo': correo1, 'Telefono': telefono1}
	nom_excel = str(nombre_archivo.get() + ".xlsx")
	df = pd.DataFrame(datos, columns=['Nombres', 'Apellidos', 'Edad', 'Correo', 'Telefono'])
	df.to_excel(nom_excel)
	nombre_archivo.delete(0, END)


frame1 = Frame(ventana, bg='gray15')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(ventana, bg='gray16')
frame2.grid(column=1, row=0, sticky='nsew')

nombre = Label(frame1, text='Nombre', width=10).grid(column=0, row=0, pady=20, padx=10)
ingresa_nombre = Entry(frame1, width=20, font=('Arial', 12))
ingresa_nombre.grid(column=1, row=0)

apellido = Label(frame1, text='Apellido', width=10).grid(column=0, row=1, pady=20, padx=10)
ingresa_apellido = Entry(frame1, width=20, font=('Arial', 12))
ingresa_apellido.grid(column=1, row=1)

edad = Label(frame1, text='Edad', width=10).grid(column=0, row=2, pady=20, padx=10)
ingresa_edad = Entry(frame1, width=20, font=('Arial', 12))
ingresa_edad.grid(column=1, row=2)

correo = Label(frame1, text='Correo', width=10).grid(column=0, row=3, pady=20, padx=10)
ingresa_correo = Entry(frame1, width=20, font=('Arial', 12))
ingresa_correo.grid(column=1, row=3)

telefono = Label(frame1, text='Telefono', width=10).grid(column=0, row=4, pady=20, padx=10)
ingresa_telefono = Entry(frame1, width=20, font=('Arial', 12))
ingresa_telefono.grid(column=1, row=4)

agregar = Button(frame1, width=20, font=('Arial', 12, 'bold'), text='Agregar', bg='orange', bd=5, command=agregar_datos)
agregar.grid(columnspan=2, row=5, pady=20, padx=10)

archivo = Label(frame2, text='Ingrese Nombre del archivo', width=25, bg='gray16', font=('Arial', 12, 'bold'), fg='white')
archivo.grid(column=0, row=0, pady=10, padx=10)

nombre_archivo = Entry(frame2, width=23, font=('Arial', 12), highlightbackground="green", highlightthickness=4)
nombre_archivo.grid(column=0, row=1, pady=1, padx=10)

guardar = Button(frame2, width=20, font=('Arial', 12, 'bold'), text='Guardar', bg='green2', bd=5, command=guardar_datos)
guardar.grid(column=0, row=2, pady=20, padx=10)
ventana.mainloop()
