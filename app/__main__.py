from . import create, category, create
import json

def show(budget: list):  #Выводим все категории и траты
    print('Категория'.rjust(30) + 'Лимит по категории'.rjust(30) + 'Траты'.rjust(30))
    print('-' * 90)
    ctgs = dict(enumerate(budget))
    for key in ctgs:
        ctg = ctgs[key].pack_to_save()
        print(ctg['category_name'].rjust(30) + str(ctg['limit']).rjust(30), end='')
        if len(ctg['transactions']) == 0:
            print()
        for date in ctg['transactions']:
            print(str(ctg['transactions'][date]).rjust(30))
            print(' ' * 60, end='')
        print('-' * 90)
        
def rm_transaction(budget: list):
    ctgs = dict(enumerate(budget))
    print('Выберите категорию:')
    for key in ctgs:
        print(f'{key + 1} - {ctgs[key].get_name_ctg()}')
    cat = int(input('>'))
    ctg = ctgs[cat - 1]
    cat = ctgs[cat - 1].pack_to_save()
    for date in cat['transactions']:
        print(f'{date} - {cat['transactions'][date]} руб.')
    tr = input('Введите дату транзакции для удаления: ')
    ctg.rm_transaction(tr)

def add_waste(budget: list):
    ctgs = dict(enumerate(budget))
    print('Выберите категорию:')
    for key in ctgs:
        print(f'{key + 1} - {ctgs[key].get_name_ctg()}')
    
    cat = int(input('>'))
    ctgs[cat - 1].add_transaction()
    print('Транзакция добавлена!')

def add_category(budget: list):
    pass

def rm_category(budget: list):
    pass

def chose_cat_act(budget):
    act = int(input('Выберите действие:\n1 - Добавить категорию\n2 - Удалить категорию\n'))
    if act == 1:
        add_category(budget)
    elif act == 2:
        rm_category(budget)
    else:
        print('Ошибка повторите еще раз')

def chose_tr_act(budget: list):
    act = int(input('Выберите действие:\n1 - Добавить транзакцию\n2 - Удалить транзакцию\n'))
    if act == 1:
        add_waste(budget)
    elif act == 2:
        rm_transaction(budget)
    else:
        print('Ошибка повторите еще раз')

def change_limit(budget:list):
    pass

def exit(budget:list):
    create.load_file(create.pack_to_json(budget))
    raise StopIteration

def control_panel(budget: list):
    print('Welcome to budget app')
    show_actions = {
                        1: 'Показать всё',
                        2: 'Добавить/удалить категорию',
                        3: 'Изменить лимит',
                        4: 'Добавить/Удалить транзакцию',
                        5: 'Выход'
                    }
    actions = {
                        1: show,
                        2: chose_cat_act,
                        3: change_limit,
                        4: chose_tr_act,
                        5: exit
                    }
    while True:
        for key in show_actions:
            print(f'{key} - {show_actions[key]}')
        action = int(input('Выберите действие: '))
        actions[action](budget)
        

if __name__ == '__main__':
    control_panel(create.unpack_json(create.read_file()))
