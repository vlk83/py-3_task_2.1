
#########################################################################
def get_cook_book_dict():
    with open('list_of_recipes.txt', 'r', encoding='utf-8') as f:
        
        # создаем словарь в который поместим рецепты из файла
        cook_book = {}
        
        # создаем список построчным чтением файла
        content = [line.strip() for line in f]
        
        # удаляем какой-то странный символ вначале списка
        # погуглил - хз, что-то связано с кодировками юникода )
        content[0] = content[0].replace('\ufeff', '')

        # проходимся по списку и ищем значение с количеством ингридиетов
        # от него и пляшем
        for counter, value in enumerate(content):
            if value.isdigit():
                ingridients_number = int(value)
                
                # название блюда - это предыдущий элемент списка
                dish = content[counter-1]
                
                # создаем список для ингридиентов каждого блюда
                ingridient_list = []

                # и путём расщепления строчек последующих элементов списка
                for i in range(ingridients_number):
                    
                    ingridient_name, quantity, measure = content[counter+i+1].split(' | ')

                    ingridient_dict = {}
                    ingridient_dict['ingridient_name'] = ingridient_name
                    ingridient_dict['quantity'] = int(quantity)
                    ingridient_dict['measure'] = measure
                    
                    # складываем в него словари с характеристиками этих ингридиентов
                    ingridient_list.append(ingridient_dict)
                    
                # добавляем в словарь рецептов блюдо
                cook_book[dish] = ingridient_list

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

