# Sistema de Generación de Archivos y Reportes

Este proyecto proporciona un sistema para generar archivos de log con información aleatoria y generar informes basados en estos archivos. El sistema está implementado en Python.

## Archivos Principales

### `main.py`

Este archivo contiene el programa principal que interactúa con el usuario a través de un menú de opciones. Las opciones incluyen la generación de archivos, la creación de informes, la edición de parámetros, la impresión de parámetros y la salida del programa.

### `file_generator.py`

El módulo `file_generator` contiene la clase `FileGenerator`, que se encarga de generar archivos de log con información aleatoria. También incluye funciones para crear carpetas, generar nombres de archivos únicos y crear el contenido de los archivos.

## Otros Archivos

### `report.py`

Este archivo define la clase `Report` que se utiliza para realizar operaciones relacionadas con la generación de informes. Incluye funciones para verificar dispositivos, obtener listas de archivos y leer archivos.

### `parameters_editor.py`

El archivo `parameters_editor.py` contiene la clase `ParametersEditor`, que se utiliza para editar y manipular los parámetros del sistema.

### `generate_hash.py`

El módulo `generate_hash` proporciona la clase `Hash` que se utiliza para generar hash a partir de la información de los archivos.

## Instrucciones de Ejecución

1. Asegúrate de tener Python instalado en tu sistema.
2. Ejecuta `main.py` para iniciar el programa.
3. Selecciona la opción correspondiente en el menú para realizar las operaciones deseadas.

## Configuración

La configuración del sistema se realiza a través del archivo `parameters.json`. Este archivo incluye información sobre misiones, tipos de dispositivos, estados de dispositivos y parámetros de generación de archivos.

## Dependencias

El proyecto utiliza las siguientes dependencias externas:

- `json`: Para la carga de parámetros desde el archivo JSON.
- `logging`: Para registrar eventos y errores.
- `time`: Para gestionar intervalos de tiempo en la generación continua de archivos.
- `random`: Para la selección aleatoria de misiones y otros elementos.

## Notas Adicionales

- Se recomienda revisar y ajustar los parámetros en `parameters.json` según sea necesario.
- Si encuentras algún problema, consulta los registros de eventos en el archivo `log.txt` para obtener más información.

¡Disfruta utilizando el sistema de generación de archivos y reportes!
