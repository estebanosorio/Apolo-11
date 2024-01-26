import file_generator
import time
import report
from datetime import datetime
import json
import random



def mostrar_menu():
    print("Elige una opción:")
    print("1) Generar archivos ")
    print("2) Generar Reporte")
    print("3) Salir")

seguir = True

while seguir:
    mostrar_menu()
    opcion = int(input("¿Que quieres hacer? : "))
    if (opcion == 1):
        with open("parameters.json", "r") as parameters:
            parameter = json.load(parameters)
        basepath = file_generator.os.path.dirname("main.py")
        generator = file_generator.FileGenerator(basepath)
        generator.create_folder()
        num_files = random.randint(parameter["file_min"],parameter["file_max"])
        interval_seconds = parameter["interval_seconds"]
        print("Archivos a generar ",num_files)
        print("Cada ", interval_seconds ," Segundos")
        try:
            while True:
                generator.generate_files(num_files)
                print(f"Archivos creados en {datetime.now().strftime('%H:%M:%S')}")
                time.sleep(interval_seconds)
                
        except:
            print("\nTermino el tiempo de creacion de archivos")
    if (opcion == 2):
        x= report.create_report()
    if (opcion == 3):
        print("Adiós")
        seguir = False
    else: 
        print("Opcion Invalida")
