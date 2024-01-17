import keyboard
import FileGenerator 
import time
from datetime import datetime
import json
import random
#import report

if __name__ == "__main__":
    vlr=int(input("1) Generador de Archivos:\n 2) Reportes"))
    if(vlr == 1 ):
        with open("parameters.json", "r") as parameters:
            parameter = json.load(parameters)
        base_path = FileGenerator.os.path.dirname("main.py")
        generator = FileGenerator.FileGenerator(base_path)
        generator.create_folder()

        print(parameter)
        num_files = random.randint(parameter["fileMin"],parameter["fileMax"])
        interval_seconds = parameter["interval_seconds"]
        print(num_files)
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

        

