# 1. Imprime "Hola, mundo"
print("Hola, Mundo...")

# 2. Imprime "Hola, Valeria" con el nombre en una variable
nombre = "Valeria"
print("Hola,", nombre) # con una coma
print("Hola, "+ nombre) # con un +

# 3. Imprimir "Hola 156!" con el número en una variable
numero = 156
print("Hola",str(numero), "!") # con una coma
print("Hola "+str(numero)+ "!") # con un + -- este debería arrojar un error!, corrígelo con conversión

# 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
comida1 = "tacos"
comida2 = "arepas"
print("Me encanta comer {} y {}!".format(comida1, comida2)) # con .format()
print(f"Me encanta comer {comida1} y {comida2}!") # con una cadena f

print("")
"""
Codigo personal
"""

"""<Ejercicio 1>--- Escribe el código para que se imprima la cadena “Hola, mundo” (1)"""
print("Hola, mundo")

"""<Ejercicio 2>--- Reemplaza el texto que aparece en la variable nombre con tu nombre y usa la variable para imprimir la cadena “Hola, 
{{tu nombre}}” utilizando la concatenación con + (2b)"""
nombre = "Miguel"
print("Hola, "+ nombre)

"""<Ejercicio 3>--- Almacena tu número de la suerte en la variable numero y usa la variable para imprimir la cadena 
“Hola {{número}} !” utilizando la concatenación con coma (3a)"""
numero = 10
print("Hola",str(numero), "!")

"""<Ejercicio 4>--- Almacena tu número de la suerte en la variable numero y usa la variable para imprimir la cadena 
“Hola {{número}}!” utilizando la concatenación con + (3b)"""
numero = 10
print("Hola "+str(numero)+ "!")

"""<Ejercicio 5>--- Guarda dos de tus comidas favoritas en las variables comida1 y comida2 y úsalas para imprimir la cadena 
“¡Me encanta comer {{comida1}} y {{comida2}}!” con el método format (4a)"""
comida1 = "Pizza"
comida2 = "Hamburguesa"
print("Me encanta comer {} y {}!".format(comida1, comida2))

"""Guarda dos de tus comidas favoritas en las variables comida1 y comida2 y úsalas para imprimir la cadena 
“¡Me encanta comer {{comida1}} y {{comida2}}!” con cadena “f” (4b)"""
comida1 = "Pizza"
comida2 = "Hamburguesa"
print(f"Me encanta comer {comida1} y {comida2}!")

"""BONUS NINJA: Busca otros métodos de cadena y utilízalos en el archivo. ¡Existen muchísimas opciones para esto!"""
nombre = "Miguel"
edad = 35
print("Mi nombre es: %s y tengo %d años"% (nombre, edad))