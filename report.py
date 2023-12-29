import pandas as pd
import os
import json
import shutil
import pprint
from datetime import datetime

class Report():
    
    def __init__(self):
        pass
    
    #método para verificar que exista la carpeta devices
    def verify_devices(self):
        try:
            if os.path.exists("devices/"):
                print("Carpeta devices encontrada")
                return True
            else: 
                print("No existe la carpeta devices")
                return False
        except:
            print("Ha ocurrido un error buscando la carpeta devices")
            return False
        
    #método para devolver la lista de archivos dentro de la carpeta devices
    def get_file_list(self):
        files = os.listdir("devices/")
        file_list = []
        for file in files:
            if os.path.isfile(os.path.join("devices/",file)) and file.endswith(".log"):
                file_list.append(file)
        return file_list

    #método para leer y listar el contenido de los archivos .log
    def read_file(self, file_list):
        missions_data = []
        discarded_files = []
        for element in file_list:
            with open("devices/"+element,"r") as file:
                preview = file.read()
                try:
                    preview = json.loads(preview)
                    missions_data.append(preview)
                except:
                    discarded_files.append(preview)
        return missions_data
    
    #Se debe mejorar con el fin de que se cree una carpeta del ciclo de ejecución con base en la última existente
    def verify_backup(self):
        print("entro a verify backup")
        try:
            if not os.path.exists("backup/"):
                os.mkdir("backup")
            print("debio crear backup")
            return True    
        except:
            return False
        
    #Crear función para validar la estrucutura de cada diccionario
    
    #Método para generar el reporte de análisis de eventos
    def event_analysis(self, mission_data):
        df = pd.json_normalize(mission_data)
        data = df.groupby(['mission', 'device_type', 'device_status']).size().reset_index(name='count')
        return data
    
    #Método para mover los archivos al backup
    #Se debe mejorar para que se guarden en la carpeta del ciclo indicado
    def move_to_backup(self, list_files):
        if self.verify_backup():
            for file in list_files:
                try:
                    shutil.move("devices/"+file, "backup")
                    print("Se han movido los archivos exitosamente")
                except:
                    print(f"No fue posible mover el archivo {file}")

#DATA PARA PRUEBAS
"""move_to_backup(["testfile.txt"
,"APLCLNM-0006.log"
,"APLCLNM-0002.log"
,"APLCLNM-0003.log" 
,"APLCLNM-0004.log" 
,"APLCLNM-0005.log"])"""

#Método para generar el reporte consolidación de misiones
def killed_devices(mission_data):
    df = pd.json_normalize(mission_data)
    print(df.groupby(['mission', 'device_type']).filter(lambda x: set(x['device_status'])=='killed'))
    #print(df[df['device_status']=="killed"])

"""killed_devices([{'date': '21-12-2023',
  'device_status': 'warning',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'warning',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'warning',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'warning',
  'device_type': 'Traje espacial',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'faulty',
  'device_type': 'Traje espacial',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'killed',
  'device_type': 'Traje espacial',
  'hash': 'XXX',
  'mission': 'GalaxyTwo'},
 {'date': '21-12-2023',
  'device_status': 'killed',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'GalaxyTwo'},
 {'date': '21-12-2023',
  'device_status': 'excellent',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'OrbitOne'}])"""

fecha = datetime.now().strftime("%d%m%Y%H%M%S")
print(fecha)
#Método para crear el reporte
rp = Report()
def create_report():
    file_name = f'APLSTATS-CICLO_1-{fecha}.log'
    with open(file_name,'a') as file:
        data = rp.event_analysis([{'date': '21-12-2023',
  'device_status': 'warning',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'warning',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'warning',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'warning',
  'device_type': 'Traje espacial',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'faulty',
  'device_type': 'Traje espacial',
  'hash': 'XXX',
  'mission': 'ColonyMoon'},
 {'date': '21-12-2023',
  'device_status': 'killed',
  'device_type': 'Traje espacial',
  'hash': 'XXX',
  'mission': 'GalaxyTwo'},
 {'date': '21-12-2023',
  'device_status': 'killed',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'GalaxyTwo'},
 {'date': '21-12-2023',
  'device_status': 'excellent',
  'device_type': 'Satelite',
  'hash': 'XXX',
  'mission': 'OrbitOne'}])
        file.write(data.to_string())

create_report()
