import os
import random
import time
import json
from datetime import datetime
from generate_hash import Hash
from typing import List, Dict

class FileGenerator:

    def __init__(self, base_path: str):
        self.base_path: str = base_path
        with open("parameters.json", "r") as parameters_file:
            parameters = json.load(parameters_file)
            self.missions = parameters["missions"]
            self.device_types = parameters["device_types"]
            self.device_statuses = parameters["device_statuses"]
        self.consecutive_count: Dict[str, int] = {}

    def create_folder(self) -> None:
        folder_path: str = os.path.join(self.base_path, "devices")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def generate_filename(self, mission: str) -> str:
        if mission not in self.consecutive_count:
            self.consecutive_count[mission] = 1
        else:
            self.consecutive_count[mission] += 1

        consecutive_number: int = self.consecutive_count[mission]
        return f"APL{mission}-{consecutive_number:04}.log"

    def generate_file_content(self, mission: str) -> Dict[str, str]:
        hash = Hash()
        current_date: datetime = datetime.now().strftime("%d-%m-%Y")
        device_type: str = random.choice(self.device_types)
        device_status: str = random.choice(self.device_statuses)
        hash_value: str = hash.generate_hash(current_date, mission, device_type, device_status)
        return {
            "date": current_date,
            "mission": mission,
            "device_type": device_type.capitalize(),
            "device_status": device_status.lower(),
            "hash": hash_value
        }

    def generate_file(self, mission: str) -> None:
        file_name: str = self.generate_filename(mission)
        file_content: Dict[str, str] = self.generate_file_content(mission)
        file_path: str = os.path.join(self.base_path, "devices", file_name)

        with open(file_path, "w") as file:
            file.write(str(file_content))

    def generate_files(self, num_files: int) -> None:
        for _ in range(num_files):
            mission: str = random.choice(self.missions)
            self.generate_file(mission)

    def run_file_generation(self) -> None:
        with open("parameters.json", "r") as parameters:
            parameter: Dict[str, int] = json.load(parameters)

        num_files: int = random.randint(parameter["file_min"], parameter["file_max"])
    
        interval_seconds: int = parameter["interval_seconds"]

        print("El numero de archivos a generar es:", num_files)
        print("el tiempo intervalo para la sigueinte creacion es:",interval_seconds)


        try:
            while True:
                self.generate_files(num_files)
                print(f"Archivos creados en {datetime.now().strftime('%H:%M:%S')}")
                time.sleep(interval_seconds)
                num_files: int = random.randint(parameter["file_min"], parameter["file_max"])
                print("El número de archivos a generar es:", num_files)
                print("El tiempo de intervalo para la siguiente creación es:", interval_seconds)
        except:
            print("\nTermino el tiempo de creacion de archivos")
