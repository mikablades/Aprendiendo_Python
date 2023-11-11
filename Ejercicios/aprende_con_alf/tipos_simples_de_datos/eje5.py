"""_summary_
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.
"""
horas = float(input("Introduce el numero de horas: \n"))
coste = float(input("Introduce el coste por hora: \n"))
paga = horas * coste
print ("Tu paga es: ", paga)
