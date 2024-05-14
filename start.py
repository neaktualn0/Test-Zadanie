from transaction import Transaction
import uuid
from dotenv import load_dotenv
from os import getenv

load_dotenv()
file = getenv("DATA_JSON_PATH")


def output(check_input: str):
    res = Transaction.output_data(check_input, file)
    if res == None:
        return "Неверный параметр"
    return res

def add(date: str, type_data: str, summ: int, description: str):
    obj = Transaction(str(uuid.uuid4()),date,type_data,summ,description)
    return Transaction.add_object(obj, file)
    


def edit(id_edit: str, category_edit: str, new_data_edit: str):
    obj = Transaction.get_object(id_edit, file)
    if obj == "Error":
        return "Неверный ID"
    match category_edit:
        case "1":
            obj.type = new_data_edit
        case "2":
            obj.summ = int(new_data_edit)
        case "3":
            obj.description = new_data_edit
    return Transaction.add_object(obj, file)


def find(filter_par: str):
    filter_par = input()
    return Transaction.output_data(filter_par, file)


def start(): #Функция работы с консолью
    print("Добро пожаловать в личный электронный кошелек\nПожалуйста, выберите необходимое действие: \n\nOutput: Вывод баланса и операции, можно отфильтровать по типу")
    print("Add: Добавить новую запись в кошелек\nEdit: Изменить запись по UUID\nFind: Поиск записи по категории, сумме или дате\nExit: Выключить приложение\n")
    user_input = input().split()
    match user_input[0].lower():
        case "output":
            print("Введите параметр для поиска(необязательно): ")
            output(input())
            start()
        case "exit":
            exit()
        case "add":
            print("Введите данные операций, которую вы хотите добавить: ")
            add(input("Дата операции: "), input("Тип(loss или gain): "),int(input("Сумма операции: ")),input("Описание операции: "))
            Transaction.output_data(None,file)
            start()
        case "edit":
            Transaction.output_data(None,file)
            edit(input("Вставьте ID операции, которую вы хотите отредактировать: "), input("Выберите тип данных: тип транз., сумму или описание?(1,2,3)"), input("Введите новое значение: "))
            start()
        case "find":
            find(input("Введите значение для фильтрации: "))
            start()
        case _:
            print("Неверные символы")
            start()
    

if __name__ == '__main__':
   start()