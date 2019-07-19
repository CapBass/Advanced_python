import re
import csv
import json
import yaml


# Работа с CSV
def get_data():
    file_names = ['info_1.txt', 'info_2.txt', 'info_3.txt']

    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for file_name in file_names:
        with open(file_name, 'r') as file:
            document = file.read()
            os_prod_list.append(re.search(r'Изготовитель системы:\s+(\S+)', document)[1])
            os_name_list.append(re.search(r'Название ОС:\s+(.+\S)', document)[1])
            os_code_list.append(re.search(r'Код продукта:\s+(.+\S)', document)[1])
            os_type_list.append(re.search(r'Тип системы:\s+(.+\S)', document)[1])

    main_data = [['Изготовитель системы', 'Название системы', 'Код продукта', 'Тип системы'],
                 os_prod_list,
                 os_name_list,
                 os_code_list,
                 os_type_list]

    return main_data


def write_to_csv(file_name):
    data = get_data()
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in data:
            writer.writerow(row)


write_to_csv('test_csv.csv')


# Работа с JSON
def write_order_to_json(item, quantity, price, buyer, date):
    data = {'item': item, 'quantity': quantity, 'price': price, 'buyer': buyer, 'date': date}
    with open('orders.json', mode='r') as json_file:
        orders = json.load(json_file)
        orders['orders'].append(data)

    with open('orders.json', mode='w') as json_file:
        json.dump(orders, json_file, indent=4)


write_order_to_json('Тест', 'Хорошее', '100', 'Вася', '10.10.2015')

# Работа с YAML
yaml_dict = {'key_1': ['value_1', 'value_2', 'value_3'],
             'key_2': 50,
             'key_3': {'sub_key_1': '34\u0024'}}


def write_to_yaml(data):
    with open('test.yaml', 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False, allow_unicode=True)


def read_from_yaml(file_name):
    with open('test.yaml', 'r') as yaml_file:
        return yaml.load(yaml_file)


write_to_yaml(yaml_dict)
# print(read_from_yaml('test.yaml'))
