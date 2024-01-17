# lista de variables iniciadoras
# Tener en cuenta validador de argumentos
import random
import os
from report import Report
import pprint

missions = ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"]
device_type = ["Satelites","Naves espaciales","Vehículos espaciales"]
device_status = ["excellent", "good", "warning", "faulty", "killed"]
mission_selected = random.choice(missions)

rp = Report()

while True:
    option = input("""
                APOLO 11
                Elija una opcion
                1. Iniciar simulacion
                2. Generar reportes
                3. Salir\n""")
    match option:
        case '1':
            pass
        case '2':
            if rp.verify_devices():
                file_list = rp.get_file_list()
                mission_data = rp.read_file(file_list)
                pprint.pprint(mission_data)
                rp.event_analysis(mission_data)
                #rp.killed_devices(mission_data)
        case '3':
                break
        case _:
            print("Opcion invalida")
        
        

