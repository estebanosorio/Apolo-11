import keyboard
import FileGenerator 
import time
from datetime import datetime
#import report

if __name__ == "__main__":
    vlr=int(input("1) Generador de Archivos:\n 2) Reportes"))
    if(vlr == 1 ):
        base_path = FileGenerator.os.path.dirname("main.py")
        generator = FileGenerator.FileGenerator(base_path)
        generator.create_folder()

        num_files = int(input("Ingrese la cantidad de archivos a crear: "))
        interval_seconds = int(input("Ingrese cada cuántos segundos desea ejecutar la creación de archivos: "))

        try:
            while True:
                generator.generate_files(num_files)
                print(f"Archivos creados en {datetime.now().strftime('%H:%M:%S')}")
                time.sleep(interval_seconds)
                if keyboard.is_pressed('a'):
                    
                    break
        except:
            print("\nProceso interrumpido por el usuario.")
    
    # else:
    #     if(vlr == 2):
    #         report.create_report()

<<<<<<< HEAD
while True:
    option = input("""
                APOLO 11
                Elija una opcion
                1. Iniciar simulacion
                2. Generar reportes
                3. Salir\n""")
    match option:
        case '1':
            pass
        case '2':
            if rp.verify_devices():
                file_list = rp.get_file_list()
                mission_data = rp.read_file(file_list)
                pprint.pprint(mission_data)
                rp.event_analysis(mission_data)
                #rp.killed_devices(mission_data)
        case '3':
                break
        case _:
            print("Opcion invalida")
        
=======
>>>>>>> main
        

