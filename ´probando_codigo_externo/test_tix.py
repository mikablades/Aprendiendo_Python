from tkinter import tix
root = tix.Tk()
boton = tix.LabelEntry()
boton.pack()
root.tk.eval('package require Tix')
root.mainloop()