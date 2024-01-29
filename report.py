import pandas as pd
import os
import json
import shutil
from datetime import datetime
#from typing import groupby, DataFrame


class Report():
    def __init__(self) -> None:
        pass

    def verify_devices(self) -> bool:
        """método para verificar que exista la carpeta devices
        
        :return: retorna la confirmación de la existencia de la carpeta devices
        :rtype: bool
        """
        try:
            if os.path.exists("devices/"):
                print("Carpeta devices encontrada")
                return True
            else:
                print("No existe la carpeta devices")
                return False
        except Exception as e:
            print(f"Ha ocurrido un error buscando la carpeta devices {e}")
            return False

    def get_file_list(self) -> list:
        """método para devolver la lista de archivos dentro de la carpeta devices

        :return: retorna una lista de archivos
        :rtype: list
        """
        files: list[str] = os.listdir("devices/")
        file_list: list = []
        for file in files:
            if os.path.isfile(os.path.join("devices/", file)) and file.endswith(".log"):
                file_list.append(file)
        return file_list

    def read_file(self, file_list: str) -> list:
        """método para leer y listar el contenido de los archivos .log

        :param file_list: Lista de archivos
        :type file_list: str
        :return: retorna la lectura de los datos en una lista de Json
        :rtype: list
        """
        missions_data: list = []
        discarded_files: list = []
        for element in file_list:
            with open("devices/"+element, "r") as file:
                preview = file.read()
                try:
                    preview = json.loads(preview)
                    missions_data.append(preview)
                except Exception as e:
                    discarded_files.append(preview)
                    print(f'Ha ocurrido un error inesperado {e}')
        return missions_data
    
    def search_execution (self) -> str:
        """Método para buscar el número de la última ejecución y devolver el nombre de la proxima carpeta execution

        :return: retorna el nombre de la carpeta correspondiente al ciclo de ejecución dentro de backup
        :rtype: str
        """
        try:
            if os.path.exists(os.path.join("backup/")):
                list_dir = os.listdir(os.path.join("backup/"))
                list_aux: list = []
                if list_dir != []:
                    for item in list_dir:
                        list_aux.append(int(item.split("_")[1]))
                    list_aux.sort()
                    return("execution_"+str(list_aux[-1]+1))
                else:
                    return("execution_1")
        except Exception as e:
            return(f"Ha ocurrido un error leyendo los ficheros dentro de la carpeta backup {e}")
    
    
    def verify_backup(self) -> bool:
        """Verifica la existencia y creacion de la carpeta backup

        :return: retorna un bool indicando la existencia de la carpeta
        :rtype: bool
        """
        print("entro a verify backup")
        try:
            if not os.path.exists("backup/"):
                os.mkdir("backup")
            print("debio crear backup")
            return True   
        except Exception as e:
            print(f'Ha ocurrido un error inesperado {e}')
            return False

    # Crear función para validar la estrucutura de cada diccionario

    # Método para mover los archivos al backup
    # Se debe mejorar para que se guarden en la carpeta del ciclo indicado
    def move_to_backup(self, list_files: list) -> None:
        """Este metodo realiza el desplazamientos de los archivos al backup

        :param list_files: contiene la lista de archivos
        :type list_files: list
        """
        if self.verify_backup():
            next_dir = self.search_execution()
            os.mkdir("backup/"+next_dir)
            for file in list_files:
                try:
                    shutil.move("devices/"+file, "backup/"+next_dir+"/")
                    print("Se han movido los archivos exitosamente")
                except Exception as e:
                    print(f"No fue posible mover el archivo {file} motivo {e}")

    
    def event_analysis(self, mission_data: list) -> pd.DataFrame:
        """Método para generar el reporte de análisis de eventos

        :param mission_data: Lista de los datos leidos de cada archivo
        :type mission_data: list
        :return: retorna un dataframe con el análisis de eventos
        :rtype: pd.DataFrame
        """
        df: pd.DataFrame = pd.DataFrame(mission_data)
        data: pd.DataFrame = df.groupby(['mission', 'device_type', 'device_status']).size().reset_index(name='count')
        return data
    
    def killed_devices(self, mission_data: list) -> pd.DataFrame:
        """Método para generar el reporte consolidación de misiones
        
        :param mission_data: Lista de los datos leidos de cada archivo
        :type mission_data: list
        :return: retorna un dataframe con el análisis de los dispositivos inoperables
        :rtype: pd.DataFrame
        """
        try:
            df: pd.DataFrame = pd.DataFrame(mission_data)
            # filtra las filas donde el estado es 'killed'
            devices: pd.DataFrame = df[df['device_status'] == 'killed']
            # agrupa por misión y cuenta la cantidad de dispositivos 'killed'
            data: pd.DataFrame = devices.groupby('mission')['device_status'].count().reset_index(name='killed_devices_count')
            return data
        
        except Exception as e:
            data = pd.DataFrame()
            print(f"Ha ocurrido un error al realizar el reporte de dispositivos inoperables {e}")
            return data

    def percentage_calculation(self, mission_data: list) -> pd.DataFrame:
        """Este metodo permite calcular el porcentaje de los datos generados para cada disposivo y mision 
        con respecto a la cantidad total de datos

        :param mission_data: Lista de los datos leidos de cada archivo
        :type mission_data: list
        :return: retorna un dataframe con el porcentaje sobre la cantidad de datos en cada archivo
        :rtype: pd.DataFrame
        """
        try:
            df: pd.DataFrame = pd.DataFrame(mission_data)
            total_data: int = len(df)
            grouped_data: pd.DataFrame = df.groupby(['mission', 'device_type']).size().reset_index(name='data_count')
            grouped_data['percentage'] = (grouped_data['data_count'] / total_data) * 100
            return grouped_data

        except Exception as e:
            grouped_data = pd.DataFrame()
            print(f"Ha ocurrido un error al realizar el reporte de dispositivos inoperables {e}")
            return grouped_data
    
    def create_report(self, data_prueba: list) -> None:
        
        fecha = datetime.now().strftime("%d%m%y%H%M%S")
        file_name = f'APLSTATS-{1}-{fecha}.log'
        with open(file_name, 'a') as file:
            event_analysis = self.event_analysis(data_prueba)
            killed_devices = self.killed_devices(data_prueba)
            percentage_calculation = self.percentage_calculation(data_prueba)

            file.write("Analisis de eventos")
            file.write("\n\n"+event_analysis.to_string())
            file.write("\n\nConsolidacion de misiones")
            file.write("\n\n"+killed_devices.to_string(index=False))
            file.write("\n\nCalculo de porcentajes")
            file.write("\n\n"+percentage_calculation.to_string(index=False))
            os.startfile(os.path.join(file_name))