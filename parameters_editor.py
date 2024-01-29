from typing import Dict, List, Union
import json


class ParametersEditor:
    """
    Clase para editar y gestionar parámetros almacenados en el archivo "parameters.json"

    Atributos:
    - parameters (Union[None, Dict[str, Union[int, List[int], List[str]]]]):
        Almacena los parámetros cargados desde el archivo JSON.
    """

    def __init__(self) -> None:
        """
        Inicializa la instancia de ParametersEditor.
        """

        self.parameters: Union[None, Dict[str, Union[int, List[int], List[str]]]] = None

    def run(self) -> None:
        """
        Ejecuta el flujo para cargar, mostrar opciones, editar y guardar parámetros.
        """
        self.load_parameters()
        self.show_options()
        self.edit_parameters()
        self.save_parameters()

    def load_parameters(self) -> None:
        """
        Carga los parámetros desde el archivo "parameters.json".
        """
        with open("parameters.json") as f:
            self.parameters = json.load(f)

    def show_options(self) -> None:
        """
        Muestra las opciones disponibles para editar los parametros.
        """
        print("Elige la variable que quieres editar:")
        print("1) file_min")
        print("2) interval_seconds")
        print("3) file_max")
        print("4) device_statuses")
        print("5) device_types")
        print("6) missions")

    def edit_parameters(self) -> None:
        """
        Edita los parámetros según la opción seleccionada por el usuario.
        """
        option: int = int(input("¿Qué quieres editar? : "))
        value: Union[int, str, List[str]] = input("Nuevo valor: ")

        if option == 1:
            self.parameters["file_min"] = int(value)
        elif option == 2:
            self.parameters["interval_seconds"] = int(value)
        elif option == 3:
            self.parameters["file_max"] = int(value)
        elif option == 4:
            self.parameters["device_statuses"] = value.split(",")
        elif option == 5:
            self.parameters["device_types"] = value.split(",")
        elif option == 6:
            self.parameters["missions"] = value.split(",")

    def save_parameters(self) -> None:
        """
        Guarda los parámetros modificados en el archivo "parameters.json".
        """
        with open("parameters.json", "w") as f:
            json.dump(self.parameters, f)

    def print_parameters(self) -> None:
        """
        Imprime en la consola los parámetros actuales del archivo "parameters.json".
        """
        if self.parameters is None:
            self.load_parameters()

        print("Los parámetros actuales son:")
        for key, value in self.parameters.items():
            print(f"{key}: {value}")
