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


seguir = True
rp = Report()
while seguir:
    mostrar_menu()
    opcion: int = int(input("¿Que quieres hacer? : "))
    if (opcion == 1):
        basepath: str = file_generator.os.path.dirname("main.py")
        generator: file_generator.FileGenerator = file_generator.FileGenerator(basepath)
        generator.create_folder()
        generator.run_file_generation()

    if (opcion == 2):
        if rp.verify_devices():
            file_list = rp.get_file_list()
            mission_data = rp.read_file(file_list)
            rp.create_report(mission_data)
            rp.move_to_backup(mission_data)

    if (opcion == 3):
        editor = ParametersEditor()
        editor.run()

    if (opcion == 4):
        editor = ParametersEditor()
        editor.load_parameters()  # Carga los parámetros antes de imprimirlos
        editor.print_parameters()

    if (opcion == 5):
        seguir = False

    else:
        print("Opcion Invalida")

