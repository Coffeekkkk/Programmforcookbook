import os
def create_dict(file_):
    cook_book = {}
    with open(file_, encoding='utf-8') as work_file:
        for line in work_file:
            dish_name = line.lower().strip()
            count_ing = int(work_file.readline())
            ingredient_list = []
            for quant in range(count_ing):
                ingredient_name, quantity, measure = work_file.readline().lower().strip().split('|')
                ingr_dict = {
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure,
                }
                ingredient_list.append(ingr_dict)
            work_file.readline()
            cook_book[dish_name] = ingredient_list

    if len(cook_book) > 0:
        return cook_book
    else:
        return 'Файл пуст'


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    ingredient_for_person = {}
    for dish in dishes:
        if dish.lower() in cook_book:
            for ingredient in cook_book[dish.lower()]:
                if ingredient['ingredient_name'] not in ingredient_for_person:
                    ingredient_for_person[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                            'quantity': int(
                                                                                ingredient['quantity']) * person_count}
                else:
                    ingredient_for_person[ingredient['ingredient_name']]['quantity'] += int(
                        ingredient['quantity']) * person_count
        else:
            print(f'Блюда "{dish.capitalize()}" нет в кулинарной книге')

    return ingredient_for_person


def sort_files(path, file_):
    result = []
    for file in file_:
        with open(f'{path}{file}', encoding='utf-8') as f:
            read_all_file = f.readlines()
            strcount = len(read_all_file)
            file_name = f.name.split('/')[1]
            item = strcount, file_name, "".join(read_all_file)
            result.append(item)
    result.sort()
    out_file = 'result/result.txt'
    if os.path.isfile(out_file):
        os.remove(out_file)

    with open(out_file, 'a', encoding='utf-8') as f:
        for data in result:
            count, name, text = data
            f.write(f'{name}\n')
            f.write(f'{count}\n')
            f.write(f'{text}\n')

