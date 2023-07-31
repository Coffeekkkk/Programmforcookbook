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


file = 'source/recipes.txt'

print(create_dict(file))
