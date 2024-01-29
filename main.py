import file_generator
from report import Report
from parameters_editor import ParametersEditor


def mostrar_menu() -> None:
    """
    Muestra el menu de opciones al usuario
    """
    print("Elige una opción:")
    print("1) Generar archivos ")
    print("2) Generar Reporte")
    print("3) Editar Parametros")
    print("4) Imprimir Parametros")
    print("5) Salir")

def main_menu(opcion: int, rp: Report) -> None:
    if opcion == 1:
        basepath = file_generator.os.path.dirname("main.py")
        generator: file_generator.FileGenerator = file_generator.FileGenerator(basepath)
        generator.create_folder()
        generator.run_file_generation()
    elif opcion == 2:
        if rp.verify_devices():
            file_list = rp.get_file_list()
            if file_list:
                mission_data = rp.read_file(file_list)
                rp.create_report(mission_data)
                rp.move_to_backup(file_list)
            else:
                print("No se encontraron archivos que cumplan con las condiciones especificadas")
    elif opcion == 3:
        editor = ParametersEditor()
        editor.run()
    elif opcion == 4:
        editor = ParametersEditor()
        editor.load_parameters()
        editor.print_parameters()
    elif opcion == 5:
        seguir = False
    else:
        print("Opcion Invalida")

if __name__ == "__main__":
    seguir = True
    rp = Report()
    while seguir:
        mostrar_menu()
        opcion = int(input("¿Que quieres hacer? : "))
        main_menu(opcion, rp)
        if opcion == 5:
            seguir = False
