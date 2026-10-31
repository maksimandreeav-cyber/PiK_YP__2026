class Microprocessor:
    def __init__(self, id: int, model: str, price: int, manufacturer: str):
        self.id = id
        self.model = model
        self.price = price
        self.manufacturer = manufacturer

class Computer:
    def __init__(self, id: int, name: str, processor_id: int, ram: int):
        self.id = id
        self.name = name
        self.processor_id = processor_id
        self.ram = ram



class ComputerProcessor:
    def __init__(self, computer_id: int, processor_id: int):
        self.computer_id = computer_id
        self.processor_id = processor_id



processors = [
    Microprocessor(id=1, model="Intel Core i3-10100", price=12000, manufacturer="Intel"),
    Microprocessor(id=2, model="AMD Ryzen 3 3200G", price=11000, manufacturer="AMD"),
    Microprocessor(id=3, model="Intel Core i5-10400", price=18000, manufacturer="Intel"),
    Microprocessor(id=4, model="AMD Ryzen 5 3600", price=19000, manufacturer="AMD"),
    Microprocessor(id=5, model="Intel Core i7-10700", price=25000, manufacturer="Intel")
]

computers = [
    Computer(id=1, name="Домашний ПК", processor_id=1, ram=8),
    Computer(id=2, name="Офисный ПК", processor_id=3, ram=16),
    Computer(id=3, name="Игровой ПК", processor_id=4, ram=32),
    Computer(id=4, name="Сервер", processor_id=5, ram=64),
    Computer(id=5, name="Ноутбук базовый", processor_id=2, ram=4),
    Computer(id=6, name="Ноутбук продвинутый",processor_id=3,ram=16),
    Computer(id=7, name="Рабочая станция", processor_id=4, ram=32)
    
]

computer_processor_links = [
    ComputerProcessor(computer_id=1, processor_id=1),
    ComputerProcessor(computer_id=1, processor_id=2),
    ComputerProcessor(computer_id=2, processor_id=3),
    ComputerProcessor(computer_id=3, processor_id=4),
    ComputerProcessor(computer_id=4, processor_id=5),
    ComputerProcessor(computer_id=5, processor_id=1),
    ComputerProcessor(computer_id=6, processor_id=3),
    ComputerProcessor(computer_id=7, processor_id=4)
]


from operator import itemgetter

one_to_many = [(c.name, mp.model, mp.price) for c in computers for mp in processors if c.processor_id == mp.id]

many_to_many_temp = [(c.name, cp.computer_id, cp.processor_id) for c in computers for cp in computer_processor_links if c.id == cp.computer_id]

many_to_many = [(mp.model, mp.price, comp_name) 
                for comp_name, comp_id, proc_id in many_to_many_temp 
                for mp in processors if mp.id == proc_id]


print("\nЗапрос 1: Компьютеры с 'ПК' в названии")
res_1 = {}
for name, model, price in one_to_many:
    if 'ПК' in name:
        if name not in res_1:
            res_1[name] = []
        res_1[name].append(model)
print(res_1)


print("\nЗапрос 2: Средняя цена процессоров по компьютерам")
res_2_unsorted = []
for c in computers:
    c_procs = list(filter(lambda x: x[0] == c.name, one_to_many))
    if c_procs:
        prices = [price for _, _, price in c_procs]
        avg_price = round(sum(prices) / len(prices), 2)
        res_2_unsorted.append((c.name, avg_price))
res_2 = sorted(res_2_unsorted, key=itemgetter(1))
print(res_2)

print("\nЗапрос 3: Процессоры Intel")
res_3 = {}
for model, _, comp_name in many_to_many:
    if model.startswith('I'):
        if model not in res_3:
            res_3[model] = []
        res_3[model].append(comp_name)
print(res_3)

