
def to_dict(file_name: str) -> dict:
    cook_book = {} #сам словарь, который мы вернем для первого задания
    index = 0


    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()


    while index < len(lines):

        if not lines[index].strip(): #пропуск пустых строк
            index += 1
            continue


        dish_name = lines[index].strip()
        index += 1
        num_ingredients = int(lines[index].strip())
        index += 1

        ingredients = []

        for num in range(num_ingredients):
            ingredients_line = lines[index].strip()
            index += 1
            name, quantity, measure = map(str.strip, ingredients_line.split('|')) #извлекаем инфу об ингридиенте

            ingredient = {
                'ingredient_name': name,
                'quantity': int(quantity),
                'measure': measure
            }
            ingredients.append(ingredient)

        cook_book[dish_name] = ingredients #заполняем словарь

        if index < len(lines) and lines[index].strip() == '':
            index += 1

    return cook_book






