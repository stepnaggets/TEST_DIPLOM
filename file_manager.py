"""
Менеджер файлов: чтение, запись, копирование.
"""

import os
import shutil
from typing import List


class FileManager:
    """
    Управление файлами: создание, удаление, копирование.
    """

    @staticmethod
    def read_file(file_path: str) -> str:
        """
        Читает содержимое файла.
        
        Args:
            file_path (str): Путь к файлу.
        
        Returns:
            str: Текст файла.
        
        Raises:
            FileNotFoundError: Если файл не существует.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found!")
        
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(file_path: str, content: str, mode: str = 'w') -> None:
        """
        Записывает текст в файл.
        
        Args:
            file_path (str): Путь к файлу.
            content (str): Текст для записи.
            mode (str): Режим ('w' – перезапись, 'a' – дозапись).
        """
        with open(file_path, mode) as file:
            file.write(content)

    @staticmethod
    def copy_file(src: str, dest: str) -> None:
        """
        Копирует файл.
        
        Args:
            src (str): Исходный путь.
            dest (str): Путь назначения.
        """
        shutil.copy(src, dest)

    @staticmethod
    def list_files(directory: str) -> List[str]:
        """
        Возвращает список файлов в директории.
        
        Args:
            directory (str): Путь к директории.
        
        Returns:
            List[str]: Список файлов.
        """
        return os.listdir(directory)


if __name__ == "__main__":
    manager = FileManager()
    manager.write_file("test.txt", "Hello, World!")
    content = manager.read_file("test.txt")
    print(content)