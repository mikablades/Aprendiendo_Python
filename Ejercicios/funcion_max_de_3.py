""" 
    Para este segundo ejercicio busque en internet algunas pruebas tecnicas de nivel basico e intentare resolverlas
    en este caso opte por seguir las intrucciones de la pagina https://www.pythondiario.com y pretendo avanzar 
    con todos los ejercicios propuestos.
"""
"""
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

def max_tres(n1=int,n2=int,n3=int):
    if n1 > n2 and n1 > n3:
        return (n1)
    elif n2 > n1 and n2 > n3:
        return (n2)
    elif n3 > n1 and n3 > n2:
        return (n3)
    else:
        return ("Son iguales no contemplado en el ejercicio")

resultado=max_tres(2,2,2)
print(resultado)
        
    
