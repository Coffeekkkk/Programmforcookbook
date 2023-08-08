from functions.functions import create_dict, get_shop_list_by_dishes, sort_files

file = 'source/recipes.txt'
# Задача 1: делаем словарь из файла
cook_book = create_dict(file)

# Задача 2:
dish_list = ['Омлет', 'Фахитос', 'Запеченный картофель']
persons = 2
# для наглядности(удобства) напечатаем так
for keys, values in get_shop_list_by_dishes(dish_list, persons, cook_book).items():
    print(keys, values)


#Задача 3
path = 'source/'
name_file_list = ['1.txt', '2.txt', '3.txt']
sort_files(path, name_file_list)
