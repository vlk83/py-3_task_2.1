
#########################################################################
def get_cook_book_dict():
    with open('list_of_recipes.txt', 'r', encoding='utf-8') as f:
        
        cook_book = {}
        dishes_number = 0

        for line in f:
            if line.strip().isdigit():
                dishes_number += 1
        f.seek(0)

        for _ in range(dishes_number):
            dish = f.readline().strip().replace('\ufeff', '')
            ingridients_number = int(f.readline().strip())
            ingridient_list = []
            for _ in range(ingridients_number):
                
                ingridient_name, quantity, measure = f.readline().strip().split(' | ')
                ingridient_dict = {}
                ingridient_dict['ingridient_name'] = ingridient_name
                ingridient_dict['quantity'] = int(quantity)
                ingridient_dict['measure'] = measure
                ingridient_list.append(ingridient_dict)
                
            cook_book[dish] = ingridient_list
            f.readline()
    return cook_book

#########################################################################
def get_shop_list_by_dishes(dishes, person_count, cook_book):
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

#########################################################################
def print_shop_list(shop_list):
  print('')
  for shop_list_item in shop_list.values():
    print('{ingridient_name} {quantity} {measure}'.format(**shop_list_item))
    
#########################################################################
def create_shop_list():
  person_count = int(input('Введите количество персон: '))
  dishes = input('Введите блюда через запятую: ').split(', ')
  cook_book = get_cook_book_dict()
  shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
  print_shop_list(shop_list)
  
#########################################################################
create_shop_list()

