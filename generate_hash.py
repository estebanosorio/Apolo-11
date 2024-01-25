import hashlib

class Hash():
    def generate_hash(self, current_date, mission, device_type, device_status):
        # Concatenar la información
        info_concatenada = f'{current_date}-{mission}-{device_type}-{device_status}'
        # Calcular el hash usando SHA-256
        hasher = hashlib.sha256()
        hasher.update(info_concatenada.encode('utf-8'))

        # Devolver el hash en formato hexadecimal
        return hasher.hexdigest()
