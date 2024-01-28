import file_generator
import time
import file_generator 
from report import Report


def mostrar_menu():
    print("Elige una opción:")
    print("1) Generar archivos ")
    print("2) Generar Reporte")
    print("3) Salir")

seguir = True
rp = Report()
while seguir:
    mostrar_menu()
    opcion = int(input("¿Que quieres hacer? : "))
    if (opcion == 1):
        basepath = file_generator.os.path.dirname("main.py")
        generator = file_generator.FileGenerator(basepath)
        generator.create_folder()
        generator.run_file_generation()

    if (opcion == 2):
        if rp.verify_devices():
                file_list = rp.get_file_list()
                mission_data = rp.read_file(file_list)
                rp.create_report(mission_data)
                rp.move_to_backup(mission_data)
        
    if (opcion == 3):
        print("Adiós")
        seguir = False

    else: 
        print("Opcion Invalida")
