import os
import random
import time
from datetime import datetime
from generate_hash import Hash

class FileGenerator:
    def __init__(self, base_path):
        self.base_path = base_path
        self.missions = ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"]
        self.device_types = ["satelite", "celular", "carro", "avion", "jet", "moto", "arma", "telefono", "traje", "casco", "pantalon_espacial"]
        self.device_statuses = ["EXCELLENT", "GOOD", "WARNING", "FAULTY", "KILLED", "UNKNOWN"]
        self.consecutive_count = {}

    def create_folder(self):
        folder_path = os.path.join(self.base_path, "devices")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def generate_filename(self, mission):
        if mission not in self.consecutive_count:
            self.consecutive_count[mission] = 1
        else:
            self.consecutive_count[mission] += 1

        consecutive_number = str(self.consecutive_count[mission]).zfill(4)
        return f"APL{mission}-{consecutive_number}.log"

    def generate_file_content(self, mission):
        hash = Hash()
        current_date = datetime.now().strftime("%d-%m-%Y")
        device_type = random.choice(self.device_types)
        device_status = random.choice(self.device_statuses)
        hash_value = hash.generate_hash(current_date, mission, device_type, device_status)  # You can replace this with your actual hash generation logic
    
        return {
            "date": current_date,
            "mission": mission,
            "device_type": device_type.capitalize(),
            "device_status": device_status.lower(),
            "hash": hash_value
        }
    
    def generate_file(self, mission):
        filename = self.generate_filename(mission)
        file_content = self.generate_file_content(mission)
        file_path = os.path.join(self.base_path, "devices", filename)

        with open(file_path, "w") as file:
            file.write(str(file_content))

    def generate_files(self, num_files):
        for _ in range(num_files):
            mission = random.choice(self.missions)
            self.generate_file(mission)

if __name__ == "__main__":
    base_path = r"C:\Users\004076661\Documents\Bootcamp\Apolo11"
    generator = FileGenerator(base_path)
    generator.create_folder()

    num_files = int(input("Ingrese la cantidad de archivos a crear: "))
    interval_seconds = int(input("Ingrese cada cuántos segundos desea ejecutar la creación de archivos: "))

    try:
        while True:
            generator.generate_files(num_files)
            print(f"Archivos creados en {datetime.now().strftime('%H:%M:%S')}")
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
        