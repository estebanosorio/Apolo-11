import json

class ParametersEditor:

    def __init__(self):
        self.parameters = None

    def run(self):
        self.load_parameters()
        self.show_options()
        self.edit_parameters()
        self.save_parameters()

    def load_parameters(self):
        with open("parameters.json") as f:
            self.parameters = json.load(f)
        

    def show_options(self):
        print("Elige la variable que quieres editar:")
        print("1) file_min")
        print("2) interval_seconds")
        print("3) file_max")
        print("4) device_statuses")
        print("5) device_types")
        print("6) missions")

    def edit_parameters(self):
        option: int = int(input("¿Que quieres editar? : "))
        value: str = input("Nuevo valor: ")

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

    def save_parameters(self):
        with open("parameters.json", "w") as f:
            json.dump(self.parameters, f)

    def print_parameters(self):
        if self.parameters is None:
            self.load_parameters()  # Carga los parámetros si aún no se han cargado

        print("Los parámetros actuales son:")
        for key, value in self.parameters.items():
            print(f"{key}: {value}")

