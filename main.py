from functions.functions import create_dict, get_shop_list_by_dishes

file = 'source/recipes.txt'
# Задача 1: делаем словарь из файла
cook_book = create_dict(file)

# Задача 2:
dish_list = ['Омлет', 'млет']
persons = 2
# для наглядности(удобства) напечатаем так
for keys, values in get_shop_list_by_dishes(dish_list, persons, cook_book).items():
    print(keys, values)


