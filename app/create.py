from . import category
import json

def load_file(budget, file_name='budget', file_path='.'):
    try:
        with open(f'{file_path}\\{file_name}.json', 'w') as file:
            json.dump(budget, file, indent=4)
            print('Файл записан')
        return 1
    except (FileNotFoundError):
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

def read_file(file_name='budget', file_path='.'):
    try:
        with open(f'{file_path}\\{file_name}.json', 'r') as file:
            budget = json.load(file)
        return budget
    except (FileNotFoundError):
        print('FILE ERROR!')
        return {}

def pack_to_json(categories: list) -> dict:
    ctgs = [ctg.pack_to_save() for ctg in categories]
    return {
        'categories': ctgs,
        'amount': len(ctgs)
           }

def unpack_json(ctg: dict) -> list:
    categories = [category.Category(cat['category_name'], cat['limit'], cat['transactions']) for cat in ctg['categories']]
    return categories

def fill_file():
    categories = create_categories()
    load_file(pack_to_json(categories))
    return pack_to_json(categories)