import pandas as pd
import os
import json
import shutil
import pprint
from datetime import datetime
import subprocess
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
        df = pd.DataFrame(mission_data)
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
                    
    #Método para generar el reporte consolidación de misiones
    def killed_devices(self, mission_data):
        try:
            df = pd.DataFrame(mission_data)
            #filtra las filas donde el estado es 'killed'
            devices = df[df['device_status'] == 'killed']
            #agrupa por misión y cuenta la cantidad de dispositivos 'killed'
            data = devices.groupby('mission')['device_status'].count().reset_index(name='killed_devices_count')
            return data
        except:
            print("Ha ocurrido un error al realizar el reporte de dispositivos inoperables")
    
    def percentage_calculation(self, mission_data):
        try:
            df = pd.DataFrame(mission_data)
            total_data = len(df)
            grouped_data = df.groupby(['mission', 'device_type']).size().reset_index(name='data_count')
            grouped_data['percentage'] = (grouped_data['data_count'] / total_data) * 100
            return grouped_data
            
        except:
            print("Ha ocurrido un error al realizar el reporte de dispositivos inoperables")

#DATA PARA PRUEBAS
"""move_to_backup(["testfile.txt"
,"APLCLNM-0006.log"
,"APLCLNM-0002.log"
,"APLCLNM-0003.log" 
,"APLCLNM-0004.log" 
,"APLCLNM-0005.log"])"""




data_prueba = [{'date': '21-12-2023',
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
  'mission': 'OrbitOne'}]

fecha = datetime.now().strftime("%d%m%y%H%M%S")
print(fecha)
#Método para crear el reporte
rp = Report()
def create_report():
    file_name = f'APLSTATS-CICLO_1-{fecha}.log'
    with open(file_name,'a') as file:
        event_analysis = rp.event_analysis(data_prueba)
        killed_devices = rp.killed_devices(data_prueba)
        percentage_calculation = rp.percentage_calculation(data_prueba)
        
        file.write("Analisis de eventos")
        file.write("\n\n"+event_analysis.to_string())
        file.write("\n\nConsolidacion de misiones")
        file.write("\n\n"+killed_devices.to_string(index=False))
        file.write("\n\nCalculo de porcentajes")
        file.write("\n\n"+percentage_calculation.to_string(index=False))
        os.startfile(os.path.join(file_name))

create_report()