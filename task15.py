import os
import logging
from collections import namedtuple

# Конфигурация логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Определение объекта namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def gather_directory_info(directory_path):
    # Проверка существования директории
    if not os.path.exists(directory_path):
        logging.error(f"Directory '{directory_path}' does not exist.")
        return

    # Сбор информации о содержимом директории
    directory_info = []

    for entry in os.listdir(directory_path):
        entry_path = os.path.join(directory_path, entry)

        # Получение имени файла или каталога без расширения и расширения (если есть)
        if os.path.isdir(entry_path):
            name = entry
            extension = None
            is_directory = True
        else:
            name, extension = os.path.splitext(entry)
            is_directory = False

        # Получение названия родительского каталога
        parent_directory = os.path.basename(directory_path)

        # Создание объекта FileInfo и добавление его в список directory_info
        file_info = FileInfo(name=name, extension=extension, is_directory=is_directory,
                             parent_directory=parent_directory)
        directory_info.append(file_info)

    return directory_info


def main():
    # Получение пути к директории из аргументов командной строки
    import sys
    from pathlib import Path

    directory_path = input('Введите название директории: ')

    # Получение информации о содержимом директории
    directory_info = gather_directory_info(directory_path)

    # Сохранение данных в текстовый файл и запись лога
    with open('directory_info.txt', 'w', encoding='utf-8') as f:
        f.write('Имя файла, Расширение, Диретория/Файл, Родительская директория')
        f.write('\n')
        for file_info in directory_info:
            f.write(
                f"{file_info.name}, {file_info.extension}, {'Directory' if file_info.is_directory else 'File'}, {file_info.parent_directory}\n")
            logging.info(f"Processed {file_info.name}")
        print('Данные сохранены в файл directory_info.txt')

if __name__ == "__main__":
    main()
