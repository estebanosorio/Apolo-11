from typing import List
import logging
import file_generator
from report import Report
from parameters_editor import ParametersEditor


def mostrar_menu() -> None:
    """Muestra el menu de opciones al usuario"""
    print("Elige una opción:")
    print("1) Generar archivos ")
    print("2) Generar Reporte")
    print("3) Editar Parametros")
    print("4) Imprimir Parametros")
    print("5) Salir")


def main_menu(opcion: int, rp: Report) -> None:
    """
    Maneja la selección del menú principal.

    Args:
        opcion (int): La opción seleccionada por el usuario.
        rp (Report): Una instancia de la clase Report para realizar operaciones.

    Returns:
        None

    Raises:
        ValueError: Cuando la opción ingresada no es un número válido.
    """
    if opcion == 1:
        basepath: str = file_generator.os.path.dirname("main.py")
        generator: file_generator.FileGenerator = file_generator.FileGenerator(basepath)
        generator.create_folder()
        generator.run_file_generation()
    elif opcion == 2:
        if rp.verify_devices():
            file_list: List[str] = rp.get_file_list()
            if file_list:
                mission_data: dict = rp.read_file(file_list)
                rp.create_report(mission_data)
                rp.move_to_backup(file_list)
            else:
                logging.warning("No se encontraron archivos que cumplan con las condiciones especificadas.")
    elif opcion == 3:
        editor: ParametersEditor = ParametersEditor()
        editor.print_parameters()
        editor.run()
    elif opcion == 4:
        editor: ParametersEditor = ParametersEditor()
        editor.load_parameters()
        editor.print_parameters()
    elif opcion == 5:
        print("Adiós")
    else:
        logging.warning("Opción inválida.")


if __name__ == "__main__":
    seguir: bool = True
    rp: Report = Report()
    while seguir:
        try:
            mostrar_menu()
            opcion: int = int(input("¿Qué quieres hacer? : "))
            main_menu(opcion, rp)
            if opcion == 5:
                seguir = False
        except ValueError:
            logging.error("Por favor, introduce un número válido.")
