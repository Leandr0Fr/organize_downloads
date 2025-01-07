import logging
import os
import shutil
from pathlib import Path

from .constants import *

logging.basicConfig(
    filename="script_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main():
    create_folders()
    organize_files()


def create_folders() -> None:
    """
    Params: None
    Returns None

    Creates folders in downloads
    that are in the list of constants
    """
    for k in FOLDERS:
        try:
            new_folder = f"{DOWNLOADS_FOLDER}/{k}"
            os.mkdir(new_folder)
        except FileExistsError:
            logging.error(f"La carpeta ya existe: {new_folder}")


def organize_files() -> None:
    """
    Params: None
    Returns None

    Organize files into folders
    that are in the constants list
    """
    name_files = get_name_files(DOWNLOADS_FOLDER)
    for file in name_files:
        extension = get_extension_file(file)
        for k, _ in FOLDERS.items():
            if extension in FOLDERS[k]:
                move_file(file, k)
                continue
        move_file(file, "Others")


def move_file(file_name: str, folder_name: str) -> None:
    """
    Params: file_name: str -> name of file into downloads folder.
            folder_move: str -> name folder for move file.
    Returns None

    Move file into folder_move.
    """
    try:
        os.makedirs(folder_name, exist_ok=True)
        shutil.move(f"{DOWNLOADS_FOLDER}/{file_name}", f"{DOWNLOADS_FOLDER}/{folder_name}")
        print(f"Archivo movido exitosamente a {folder_name}")
    except FileNotFoundError:
        logging.error(f"Error: El archivo {folder_name} no existe.")
    except Exception as e:
        logging.error(f"Ocurrió un error al mover el archivo: {e}")


def get_extension_file(file_name: str) -> str:
    """
    Params: file_name: str
    Returns extension_file: str

    get extension of file_name
    """
    file = Path(file_name)
    return file.suffix


def get_name_files(path_downloads: str) -> list:
    """
    Params: path_downloads: str
    Returns files name: list

    get files name of path_downloads
    """
    files = []
    for file in os.listdir(path_downloads):
        path = os.path.join(path_downloads, file)
        if os.path.isfile(path):
            files.append(file)
    return files


if __name__ == "__main__":
    main()
