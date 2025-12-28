from . import create

def start():
    budget = create.read_file()
    if budget == {}:
        print('Файл не найден или пуст')
        is_fill = input('Вы хотите заполнить файл? (y/n): ')
        while not is_fill.lower() in ('y','n'):
            print('Ошибка')
            is_fill = input('Вы хотите заполнить файл? (y/n): ')
        if is_fill == 'y':
            filed_budget = create.fill_file()
            return filed_budget
        else:
            raise FileExistsError
    else:
        return budget
        
budget_file = start()

