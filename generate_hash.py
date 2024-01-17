import hashlib

class Hash():
    
    def generate_hash(self,current_date, mission, device_type, device_status):
        # Concatenar la información
        info_concatenada = f'{current_date}-{mission}-{device_type}-{device_status}'

        # Calcular el hash usando SHA-256
        hasher = hashlib.sha256()
        hasher.update(info_concatenada.encode('utf-8'))

        # Devolver el hash en formato hexadecimal
        return hasher.hexdigest()

# Ejemplo de uso
'''
current_date = '2024-01-11'
mision = 'MisiónX'
device_type = 'TipoA'
device_status = 'Activo'

hash = Hash()
hash_resultado = hash.generate_hash(current_date, mision, device_type, device_status)
print(f'El hash resultante es: {hash_resultado}')'''