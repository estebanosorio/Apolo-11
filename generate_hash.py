import hashlib
import logging
from typing import Any

logging.basicConfig(level=logging.WARN)

class Hash():
    def generate_hash(self, current_date:str, mission:str, device_type:str, device_status:str) -> str:
        # Concatenar la información
        """Esta función toma unos argumentos de tipo str y los concatena, luego los vuelve hexadecimales y lo convierte en un valor hash
        Args:
            current_date (str): Fecha
            mission (str): Mision
            device_type (str): Tipo de dispositivo
            device_status (str): Estado del dispositivo

        Returns:
            str: Retorna el hash code para cada archivo
        """
        info_concatenada: str = f'{current_date}-{mission}-{device_type}-{device_status}'
        # Calcular el hash usando SHA-256
        hasher: Any = hashlib.sha256()
        hasher.update(info_concatenada.encode('utf-8'))
        logging.info("Los archivos han sido incriptados")
        # Devolver el hash en formato hexadecimal
        return hasher.hexdigest()