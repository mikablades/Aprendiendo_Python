""" 
    Para este primer ejercicio busque en internet algunas pruebas tecnicas de nivel basico e intentare resolverlas
    en este caso opte por seguir las intrucciones de la pagina https://www.pythondiario.com y pretendo avanzar 
    con todos los ejercicios propuestos.
"""
"""
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio."""

#lo que hare es crear una funcion donde me asegure que los valores de entrada seran tomados como enteros
#luego agregare un condicional if para saber si (numero 1) < (numero 2), en dicho caso retornara (numero 2)
#agregare un else al final de la funcion en caso de que el if resulte False. y entre medio de la funcion
#incorporare un elif para el caso no contemplado por el ejercicio donde los numeros sean iguales.
#por ultimo llamare a la funcion le asignare valores de prueba y agregare un print del resultado.

def new_max(n1=int, n2=int):
    if n1 < n2:
        return n2
    elif n1==n2:
        print("son iguales no es contemplado en el egercicio")
    else:
        return n1    
    
resultado = new_max (-68,-1)
print (resultado)