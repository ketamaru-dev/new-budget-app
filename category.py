class Category:
    
    def __init__(self, name_of_cat: str, cat_limit: float):
        self.name_of_cat = name_of_cat
        self.cat_limit = cat_limit

        #Создаем словарь транзакции key = date, value = summ
        self.transactions = {}

    def check_limit(self):  #this method is check if limit is out
        total_amount = self.count_total()
        if self.cat_limit >= total_amount:
            print(f"It's ok you in limit\n Current limit is {total_amount}/{self.cat_limit}")
            return True
        else:
            print(f"You limit is full, stop it \n Current limit is {total_amount}/{self.cat_limit}")
            return False

    def count_total(self):  #this method is count all transactions
            total = 0
            for date_key in self.transactions:
                total += self.transactions[date_key]
            return total

    def add_transaction(self):  #the method is add new transaction to category
            summ = float(input('Enter the amount of transaction: '))
            date = input('Enter the date in format YEAR:MONTH:DAT (if empty, created currently date): ')
            if date == '':
                from datetime import datetime
                date = datetime.now().strftime("%Y-%m-%d")
            new_transaction = Transaction(summ, date)
            self.transactions[date] = new_transaction
            self.check_limit()

    def pack_to_save(self):
        packed_category = {
            'category name': self.name_of_cat,
            'limit': self.cat_limit,
            'transactions': self.transactions
        }
        return packed_category

    def get_all_transactions(self):
        category_transaction = []
        for date_key in self.transactions:
            category_transaction.append(self.transactions[date_key].get_transaction())
        return category_transaction

    def get_name_ctg(self):
        return self.name_of_cat
    
    def change_limit(self, new_limit: float):
        self.cat_limit = new_limit
        print('Лимит изменен')

    def rm_transaction(self, date:str):
        del self.transactions[date]
        print('Транзакция удалена')

    
class Transaction:

    def __init__(self, amount_of_transaction: float, date_of_transaction: str):
        self.amount_of_transaction = amount_of_transaction
        self.date_of_transaction = date_of_transaction
        
    def get_amount(self):
        return self.amount_of_transaction

    def get_transaction(self):
        return (self.date_of_transaction, self.amount_of_transaction)
    