import json
import uuid
class Transaction:
    def __init__(self,id,date,type,summ,description): #Инициализация
        self.id = id
        self.date = date
        self.type = type
        self.summ = summ
        self.description = description
    
    def add_object(self): #Добавление объекта в JSON
        with open("data.json",'r') as fp:
            data = json.load(fp)
            data_array = list(data["operations"])
        with open("data.json",'w') as fp:
            if self.type == 'gain':
                new_balance = int(data["balance"]) + int(self.summ)
            elif self.type == 'loss':
                new_balance = int(data["balance"]) - int(self.summ)
            data["balance"] = str(new_balance)
            data_array.append(self.__dict__)
            data["operations"] = data_array
            json.dump(data,fp)
    
    def get_object(filter): #Получение нужного объекта из JSON
        with open("data.json",'r') as fp:
            data = json.load(fp)
            data_array = list(data["operations"])
        for word in data_array:
            if word["id"] == filter:
                obj = Transaction(filter,word["date"], word["type"], word["summ"], word["description"])
                return obj
            else:
                return "Error"
    def output_data(find_data): #Вывод данных в консоль
        with open("data.json",'r') as fp:
            data = json.load(fp)
            data_array = list(data["operations"])
        print(f"\nБаланс: {data["balance"]}\n")
        for word in data_array:
            obj = Transaction(word["id"],word["date"],word["type"],word["summ"],word["description"])
            if find_data == None or find_data == obj.type or find_data == obj.summ or find_data == obj.description:
                print(f"ID: {obj.id}\nДата: {obj.date}\nКатегория: {obj.type}\nСумма: {obj.summ}\nОписание: {obj.description}\n")

def start(): #Функция работы с консолью
    print("Добро пожаловать в личный электронный кошелек\nПожалуйста, выберите необходимое действие: \n\nOutput: Вывод баланса и операции, можно отфильтровать по типу")
    print("Add: Добавить новую запись в кошелек\nEdit: Изменить запись по UUID\nFind: Поиск записи по категории, сумме или дате\nExit: Выключить приложение\n")
    user_input = input()
    match user_input[0]:
        case "output":
            print("Введите параметр для поиска(необязательно): ")
            check_input = input()
            Transaction.output_data(check_input)
            start()
        case "exit":
            exit()
        case "add":
            print("Введите данные операций, которую вы хотите добавить: ")
            date = input("Дата операции: ")
            type_data = input("Тип(loss или gain): ")
            summ = input("Сумма операции: ")
            description = input("Описание операции: ")
            obj = Transaction(str(uuid.uuid4),date,type_data,summ,description)
            Transaction.add_object(obj)
            Transaction.output_data(None)
            start()
        case "edit":
            Transaction.output_data(None)
            print("Скопируйте ID операции, которую вы хотите отредактировать и вставьте его")
            id_edit = input()
            print("Что вы хотите отредактировать: тип, сумму или описание?(1,2,3)")
            category_edit = input()
            print("Введите новое значение: ")
            new_data_edit = input()
            obj = Transaction.get_object(id_edit)
            if obj == "Error":
                print("Неверный ID")
                start()
            match category_edit:
                case "1":
                    obj.type = new_data_edit
                case "2":
                    obj.summ = new_data_edit
                case "3":
                    obj.description = new_data_edit
            Transaction.add_object(obj)
            start()
        case "find":
            print("Введите значение для фильтрации: ")
            filter_par = input()
            Transaction.output_data(filter_par)
            start()

start()
