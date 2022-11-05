import random
import json

FILE_PATH = '/home/kunduz/Desktop/evening_25/hakaton/CRUD/data.json'
ID_FILE_PATH = '/home/kunduz/Desktop/evening_25/hakaton/CRUD/data.txt'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)


# CRUD

def list_of_products():
    data = get_data()
    return f'Список всех товаров: {data}'
def detail_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: id == x['id'], data))
        return product[0]
    except:
        return 'Неверный id!'
    
def get_id():
    with open(ID_FILE_PATH, 'r') as file:
        id = int(file.read())
        id += 1
    with open(ID_FILE_PATH, 'w') as file:
        file.write(str(id))
    return id

def create_product():
    data = get_data()
    try:
        prodduct = {
            'id': get_id(),
            'marka': input('Введите марку продукта: '), 
            'model': input('Введите модель продукта: '), 
            'year': int(input('Введите год выпуска: ')),
            'description': input('Введите  описание: '),
            'price': float(input('Введите цену продукта: '))
        }
    except Exception as e:
        print(e)
        return 'Неверные данные!'
    
    data.append(prodduct)
    save_data(data)
    return 'Создан новый товар!'

def update_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, data)) [0]
        print('Товар для обновления: {product["marka"]}')
    except:
        return 'Неверный id!'
    index = data.index(product)
    choice = input('Что вы хотите изменить?(1-marka, 2-model, 3-year, 4-description, 5-price): ')
    if choice.strip() == '1':
        data[index]['marka'] = input('Введите новое значение: ')
    elif choice.strip() == '2':
        data[index]['model'] == input('Введите новое значение: ')
    elif choice.strip() == '3':
        data[index]['year'] == int(input('Введите новое значение: '))
    elif choice.strip() == '4':
        data[index]['description'] == input('Введите новое описание: ')
    elif choice.strip() == '5':
        try:
            data[index]['price'] == float(input('Введите новую цену для товара: '))
        except:
            return 'Неверное значение!'
    else:
        return 'Неверное значение для обновления!'
    save_data(data)
    return 'Товар обнавлен!'

def delete_product():
    data = get_data()
    try:
        id = int(input('Введите id продукта: '))
        product = list(filter(lambda x: x['id'] == id, data)) [0]
        print(f'Товар для удаления {product["marka"]}')
    except:
        return 'Неверный id!'
    choice = input('Удалить этот товар?(yes/no)')
    if choice.lower().strip() != 'yes':
        return 'Товар не удален!'
    data.remove(product)
    save_data(data)
    return 'Товар удален!'


        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    