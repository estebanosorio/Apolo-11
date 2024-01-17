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

        

