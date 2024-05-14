import json
class Transaction:
    def __init__(self,id: str, date: str,type: str,summ: int,description: str): #Инициализация
        self.id = id
        self.date = date
        self.type = type
        self.summ = summ
        self.description = description
    

    def add_object(self, file: str): #Добавление объекта в JSON
        with open(file,'r') as fp:
            data = json.load(fp)
            data_array = list(data["operations"])
        with open(file,'w') as fp:
            if self.type == 'gain':
                new_balance = int(data["balance"]) + int(self.summ)
            elif self.type == 'loss':
                new_balance = int(data["balance"]) - int(self.summ)
            data["balance"] = str(new_balance)
            data_array.append(self.__dict__)
            data["operations"] = data_array
            json.dump(data,fp)
    

    def get_object(filter: str,file: str): #Получение нужного объекта из JSON
        with open(file,'r') as fp:
            data = json.load(fp)
            data_array = list(data["operations"])
        for word in data_array:
            if word["id"] == filter:
                obj = Transaction(filter,word["date"], word["type"], word["summ"], word["description"])
                return obj
            else:
                return "Error"
            

    def output_data(find_data: str, file: str): #Вывод данных в консоль
        with open(file,'r') as fp:
            data = json.load(fp)
            data_array = list(data["operations"])
        print(f"\nБаланс: {data["balance"]}\n")
        for word in data_array:
            obj = Transaction(word["id"],word["date"],word["type"],word["summ"],word["description"])
            if find_data == None or find_data == obj.type or find_data == obj.summ or find_data == obj.description:
                print(f"ID: {obj.id}\nДата: {obj.date}\nКатегория: {obj.type}\nСумма: {obj.summ}\nОписание: {obj.description}\n")