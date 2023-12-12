# Operaciones basicas y tipos de datos
# Operación 1: Suma dos números enteros
numero_entero1 = 3
numero_entero2 = 6
resultado_suma = numero_entero1 + numero_entero2
print(f"1. Suma: {numero_entero1} + {numero_entero2} = {resultado_suma}")

# Operación 2: Resta dos números de punto flotante
numero_flotante1 = 4.5
numero_flotante2 = 8.5
resultado_resta = numero_flotante1 - numero_flotante2
print(f"2. Resta: {numero_flotante1} - {numero_flotante2} = {resultado_resta}")

# Operación 3: Multiplica dos números enteros
numero_entero3 = 12
numero_entero4 = 3
resultado_multiplicacion = numero_entero3 * numero_entero4
print(f"3. Multiplicación: {numero_entero3} * {numero_entero4} = {resultado_multiplicacion}")

# Operación 4: Divide dos números de punto flotante
numero_flotante3 = 30.0
numero_flotante4 = 5.0
resultado_division = numero_flotante3 / numero_flotante4
print(f"4. División: {numero_flotante3} / {numero_flotante4} = {resultado_division}")

# Manipulacion de cadenas de texto
# Declara una variable de tipo string que contenga tu nombre completo.
nombre_completo = "Nicolas Sebastian Abril Ochoa"

# Utiliza la función len() para obtener la longitud de tu nombre completo y guárdalo en una variable.
longitud_nombre = len(nombre_completo)

# Imprime en pantalla tu nombre completo y su longitud, utilizando la función print().
print(f"Nombre completo: {nombre_completo}")
print(f"Longitud del nombre completo: {longitud_nombre}")

# Comentario explicativo sobre el propósito de este programa.
"""
Este programa tiene como objetivo mostrar cómo declarar una variable de tipo string con un nombre completo,
utilizar la función len() para obtener la longitud de esa cadena y luego imprimir el nombre completo y su longitud.
"""

# Conversion de tipos de datos
# Declara una variable entera
entero_original = 53

# Declara una variable de punto flotante
flotante_original = 5.14

# Imprime el tipo de dato original
print(f"Tipo de dato original para 'entero_original': {type(entero_original)}")
print(f"Tipo de dato original para 'flotante_original': {type(flotante_original)}")

# Convierte la variable entera a punto flotante
entero_a_flotante = float(entero_original)

# Convierte la variable de punto flotante a entera
flotante_a_entero = int(flotante_original)

# Imprime el tipo de dato después de la conversión
print(f"Tipo de dato después de la conversión para 'entero_a_flotante': {type(entero_a_flotante)}")
print(f"Tipo de dato después de la conversión para 'flotante_a_entero': {type(flotante_a_entero)}")


# Comentarios y documentos
# Propósito general del programa:
# Este programa demuestra la conversión entre variables enteras y de punto flotante,
# y muestra los tipos de dato antes y después de la conversión.

# Declara una variable entera
entero_original = 53

# Declara una variable de punto flotante
flotante_original = 5.14

# Imprime el tipo de dato original
print(f"Tipo de dato original para 'entero_original': {type(entero_original)}")
print(f"Tipo de dato original para 'flotante_original': {type(flotante_original)}")

# Convierte la variable entera a punto flotante
entero_a_flotante = float(entero_original)

# Convierte la variable de punto flotante a entera
flotante_a_entero = int(flotante_original)

# Imprime el tipo de dato después de la conversión
print(f"Tipo de dato después de la conversión para 'entero_a_flotante': {type(entero_a_flotante)}")
print(f"Tipo de dato después de la conversión para 'flotante_a_entero': {type(flotante_a_entero)}")
