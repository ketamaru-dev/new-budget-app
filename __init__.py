import json
import create, category

def read_file(file_name='budget', file_path='.'):
    try:
        with open(f'{file_path}\\{file_name}.json', 'r') as file:
            budget = json.load(file)
        return budget
    except (FileNotFoundError, json.decode.JSONDecodeError):
        print('FILE ERROR!')
        return 0
    finally:
        return 0

def start():
    budget = read_file()
    if budget == 0:
        print('Файл не найден или пуст')
        is_fill = input('Вы хотите заполнить файл? (y/n): ')
        while not is_fill.lower() in ('y','n'):
            print('Ошибка')
            is_fill = input('Вы хотите заполнить файл? (y/n): ')
        if is_fill == 'y':
            budget = create.fill_the_file()
            return budget
        else:
            return 0
    else:
        return budget
        
budget_file = start()
