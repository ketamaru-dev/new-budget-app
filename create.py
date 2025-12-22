import category
import json

def load_file(budget, file_name='budget', file_path='.'):
    try:
        with open(f'{file_path}\\{file_name}.json', 'w') as file:
            json.dump(budget, file)
            print('Файл записан')
        return 1
    except (FileNotFoundError, json.decode.JSONDecodeError):
        print('FILE ERROR!')
        return 0
    finally:
        return 0
    
def create_categories():
    categories = []
    while True:
        try:
            name = input('Введите имя категории: ')
            limit = float(input('Введите лимит категории: '))
            new_cat = category.Category(name, limit)
            print('Категория созданна')
            categories.append(new_cat)
        except ValueError:
            print('Ошибка, Попробуйте еще раз')
            continue
        finally:
            is_continue = input('Хотите добавить еще одну категорию?(y/n): ')
            if is_continue.lower() == 'y':
                continue
            else:
                break
    return categories            

def fill_file():
    categories = create_categories()
    load_file(categories)