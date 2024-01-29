import os
import random
import time
import json
from datetime import datetime
from generate_hash import Hash
from typing import List, Dict
import logging


class FileGenerator:
    """
    Clase para generar archivos de log con información aleatoria.

    Args:
        base_path (str): Ruta base para almacenar los archivos generados.

    Attributes:
        base_path (str): Ruta base para almacenar los archivos generados.
        missions (List[str]): Lista de misiones obtenidas de 'parameters.json'.
        device_types (List[str]): Lista de tipos de dispositivos obtenidos de 'parameters.json'.
        device_statuses (List[str]): Lista de estados de dispositivos obtenidos de 'parameters.json'.
        consecutive_count (Dict[str, int]): Diccionario para realizar un seguimiento de los conteos consecutivos por misión.
    """

    def __init__(self, base_path: str):
        """
        instanciar un objeto de FileGenerator.

        Args:
            base_path (str): Ruta base para almacenar los archivos con la informacion de las misiones.
        """
        self.base_path: str = base_path
        with open("parameters.json", "r") as parameters_file:
            parameters: Dict[str, List[str]] = json.load(parameters_file)
            self.missions: List[str] = parameters["missions"]
            self.device_types: List[str] = parameters["device_types"]
            self.device_statuses: List[str] = parameters["device_statuses"]
        self.consecutive_count: Dict[str, int] = {}

    def create_folder(self) -> None:
        """
        Crea la carpeta 'devices' en la ruta base si no existe.
        """
        folder_path: str = os.path.join(self.base_path, "devices")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def generate_filename(self, mission: str) -> str:
        """
        Genera un nombre de archivo único usando la misión y el conteo consecutivo.

        Args:
            mission (str): Misión para la cual se genera el nombre de archivo.

        Returns:
            str: Nombre de archivo único.
        """
        if mission not in self.consecutive_count:
            self.consecutive_count[mission] = 1
        else:
            self.consecutive_count[mission] += 1

        consecutive_number: int = self.consecutive_count[mission]
        return f"APL{mission}-{consecutive_number:04}.log"

    def generate_file_content(self, mission: str) -> Dict[str, str]:
        """
        Generar el contenido del archivo con la información de manera aleatoria.

        Args:
            mission (str): Misión para la cual se genera el contenido.

        Returns:
            Dict[str, str]: Contenido del archivo en formato de diccionario.
        """
        hash_obj: Hash = Hash()
        current_date: str = datetime.now().strftime("%d-%m-%Y")
        device_type: str = random.choice(self.device_types)
        device_status: str = random.choice(self.device_statuses)
        hash_value: str = hash_obj.generate_hash(current_date, mission, device_type, device_status)
        return {
            "date": current_date,
            "mission": mission,
            "device_type": device_type.capitalize(),
            "device_status": device_status.lower(),
            "hash": hash_value
        }

    def generate_file(self, mission: str) -> None:
        """
        Crea un archivo con el contenido generado y lo guarda en la carpeta 'devices'.

        Args:
            mission (str): Misión para la cual se genera el archivo.
        """
        file_name: str = self.generate_filename(mission)
        file_content: Dict[str, str] = self.generate_file_content(mission)
        file_path: str = os.path.join(self.base_path, "devices", file_name)

        with open(file_path, "w") as file:
            file.write(json.dumps(file_content, indent=4))
        logging.info(f"Archivo '{mission}' creado en {datetime.now().strftime('%H:%M:%S')}")

    def generate_files(self, num_files: int) -> None:
        """
        Crea múltiples archivos aleatorios.

        Args:
            num_files (int): Número de archivos para generar.
        """
        try:
            for _ in range(num_files):
                mission: str = random.choice(self.missions)
                self.generate_file(mission)
        except Exception as e:
            logging.error(f"Error durante la generación de archivos: {str(e)}")

    def run_file_generation(self) -> None:
        """
        Ejecuta la generación de archivos de forma continua con los intervalos de tiempo
        .

        Raises:
            Exception: Se produce un error durante la ejecución del script.
        """
        try:
            with open("parameters.json", "r") as parameters_file:
                parameter: Dict[str, int] = json.load(parameters_file)

            num_files: int = random.randint(parameter["file_min"], parameter["file_max"])
            interval_seconds: int = parameter["interval_seconds"]

            logging.info(f"Número de archivos a generar: {num_files}")
            logging.info(f"Tiempo intervalo para la siguiente creación: {interval_seconds} segundos")

            while True:
                self.generate_files(num_files)
                logging.info(f"Archivos creados en {datetime.now().strftime('%H:%M:%S')}")
                time.sleep(interval_seconds)
                num_files: int = random.randint(parameter["file_min"], parameter["file_max"])
                logging.info(f"Número de archivos a generar: {num_files}")
                logging.info(f"Tiempo de intervalo para la siguiente creación: {interval_seconds} segundos")

        except Exception as e:
            logging.error(f"Error durante la ejecución del script: {str(e)}")
