# Sistema de Generación de Archivos y Reportes

Este proyecto proporciona un sistema para generar archivos de log con información aleatoria y generar informes basados en estos archivos. El sistema está implementado en Python.

## Archivos Principales

### `main.py`

Este archivo contiene el programa principal que interactúa con el usuario a través de un menú de opciones. Las opciones incluyen la generación de archivos, la creación de informes, la edición de parámetros, la impresión de parámetros y la salida del programa.

### `file_generator.py`

El módulo `file_generator` contiene la clase `FileGenerator`, que se encarga de generar archivos de log con información aleatoria. También incluye funciones para crear carpetas, generar nombres de archivos únicos y crear el contenido de los archivos.

### `report.py`

Contiene la clase Report que realiza el análisis de eventos, generación de informes consolidados y cálculos de porcentajes sobre los datos de los archivos de log generados.

### `generate_hash.py`

Implementa la generación de un hash utilizando la biblioteca hashlib para garantizar la integridad de los datos en los archivos generados.

### `generateparameters_editor.py`

Este archivo define una clase (`ParametersEditor`) que permite al usuario editar los parámetros del sistema. Los parámetros se cargan desde un archivo JSON llamado 'parameters.json', y el usuario puede editar valores como el número mínimo y máximo de archivos a generar, el intervalo de tiempo, tipos de dispositivos, estados de dispositivos, y misiones.

## Archivos de Configuración

### `parameters.json`

Este archivo contiene los parámetros de configuración del sistema, como el rango de archivos a generar, el intervalo de tiempo entre generaciones, las misiones disponibles, tipos de dispositivos y estados de dispositivos.

## Instrucciones de Ejecución

1. Asegúrate de tener Python instalado en tu sistema.
2. Ejecuta `main.py` para iniciar el programa.
3. Selecciona la opción correspondiente en el menú para realizar las operaciones deseadas.

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
