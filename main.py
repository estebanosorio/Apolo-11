import file_generator 
import report


def mostrar_menu() -> None:
    '''
    Muestra el menu de opciones al usuario
    '''
    print("Elige una opción:")
    print("1) Generar archivos ")
    print("2) Generar Reporte")
    print("3) Salir")

seguir = True

while seguir:
    mostrar_menu()
    opcion: int = int(input("¿Que quieres hacer? : "))
    if (opcion == 1):
        basepath: str = file_generator.os.path.dirname("main.py")
        generator: file_generator.FileGenerator = file_generator.FileGenerator(basepath)
        generator.create_folder()
        generator.run_file_generation()

    if (opcion == 2):
        x= report.create_report()
        
    if (opcion == 3):
        print("Adiós")
        seguir = False

    else: 
        print("Opcion Invalida")
