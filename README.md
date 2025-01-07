# Organize_downloads

## Descripción
Script en Python para ordenar los archivos de descargas en Windows

## Instalación del Script

Debe contar con Python 3.13 o superior y Poetry como gestor de dependencias.

Utilizando pip instale Poetry `pip install poetry`. Ingrese a la carpeta del proyecto y ejecute los siguientes comandos: `poetry install` y `poetry shell`.

## Exportación a PIP

En el archivo `pyproject.toml` realice las siguientes modificaciones:
* `name = "app" -> "organize_downloads"`
*  en [tool.poetry.scripts] agregue `organize_downloads = "organize_downloads.main:main"`. Además cambie el nombre de la carpeta "app" por "organize_downloads".

Utilice el comando `poetry build`.

Finalmente, instale el archivo .whl de la carpeta dist utilizando pip.
EJ: `pip install organize_downloads-0.2.0-py3-none-any.whl`.

## Iniciar Script

Tras la configuración e instalación, para correr el script ejecute `poetry run start`

Si exportó mediante PIP el programa, ejecutelo de esta manera: `organize_downloads` en la consola.