import time
import os
import keyboard

# Definir una clase para manejar los archivos
class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def crear(self):
        # Crear un archivo con el nombre dado
        try:
            with open(self.nombre, "w") as f:
                f.write(f"Este es el archivo {self.nombre}\n")
        except IOError:
            print(f"Error al crear el archivo {self.nombre}")

    def leer(self):
        # Leer el contenido del archivo y mostrarlo en la pantalla
        try:
            with open(self.nombre, "r") as f:
                print(f.read())
        except IOError:
            print(f"Error al leer el archivo {self.nombre}")

# Definir una función para mostrar el menú de opciones
def mostrar_menu():
    print("Elige una opción:")
    print("1) Crear archivos .txt cada 5 segundos")
    print("2) Leer los 5 archivos creados")
    print("3) Salir")

# Definir una lista para almacenar los objetos de la clase Archivo
archivos = []

# Definir una variable para controlar el bucle principal
seguir = True

# Iniciar el bucle principal
while seguir:
    # Mostrar el menú
    mostrar_menu()
    # Pedir al usuario que ingrese una opción
    opcion = input("¿Qué quieres hacer? ")
    # Ejecutar la acción correspondiente a la opción elegida
    if opcion == "1":
        # Crear un archivo cada 5 segundos hasta que se presione la tecla "a"
        print("Creando archivos .txt cada 5 segundos. Presiona la tecla 'a' para detener.")
        i = 1 # Contador de archivos creados
        while True:
            # Crear un objeto de la clase Archivo con el nombre "archivo_i.txt"
            archivo = Archivo(f"archivo_{i}.txt")
            # Llamar al método crear del objeto
            archivo.crear()
            # Agregar el objeto a la lista de archivos
            archivos.append(archivo)
            # Mostrar un mensaje indicando que se ha creado el archivo
            print(f"Se ha creado el archivo {archivo.nombre}")
            # Esperar 5 segundos
            time.sleep(5)
            # Incrementar el contador
            i += 1
            # Verificar si se ha presionado la tecla "a"
            if keyboard.is_pressed("a"):
                # Detener el bucle
                break
    elif opcion == "2":
        # Leer los 5 archivos creados
        print("Leyendo los 5 archivos creados.")
        # Verificar si hay al menos 5 archivos en la lista
        if len(archivos) >= 5:
            # Recorrer los primeros 5 elementos de la lista
            for archivo in archivos[:5]:
                # Llamar al método leer del objeto
                archivo.leer()
        else:
            # Mostrar un mensaje de error
            print("No hay suficientes archivos creados. Debes crear al menos 5 archivos antes de leerlos.")
    elif opcion == "3":
        # Salir del programa
        print("Adiós")
        # Cambiar el valor de la variable seguir a False
        seguir = False
    else:
        # Mostrar un mensaje de opción inválida
        print("Opción inválida. Inténtalo de nuevo.")
