class FileError(Exception):

    def __str__(self):
        print('Ошибка создания файла!')