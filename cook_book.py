# netology_[py-3]_[2.1]
# Занятие 2.1. Открытие и чтение файла, запись в файл

# Открываем файл с рецептами и создаём словарь
cook_book = {}
f = open('list_of_recipes.txt', 'r')

def fill_cook_book():
    dish = f.readline()
    dish = dish.strip()
    ingridient_list = []
    ingridients_number = int(f.readline())
    for i in range(ingridients_number):
        
        ingridient_dict = {}
        ingridient_line = f.readline()
        ingridient_name, quantity, measure = ingridient_line.split(' | ')
        quantity = int(quantity)
        measure = measure.strip()
        
        ingridient_dict['ingridient_name'] = ingridient_name
        ingridient_dict['quantity'] = quantity
        ingridient_dict['measure'] = measure
        
        ingridient_list.append(ingridient_dict)
        
    cook_book[dish] = ingridient_list
    if f.readline() == '\n':
        fill_cook_book()
 
fill_cook_book()
f.close()



def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  print('')
  for shop_list_item in shop_list.values():
    print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
      
def create_shop_list():
  person_count = int(input('Введите количество персон: '))
  dishes = input('Введите блюда через запятую: ').split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()

