
def get_shop_list_by_dishes(cook_dict, dishes, person_count):
    dict_for_shop = {}
    for dish in dishes:
        if dish in cook_dict:
            for ingredient in cook_dict[dish]:
                ingredient_name = ingredient['ingredient_name']
                if ingredient_name not in dict_for_shop:
                    dict_for_shop[ingredient_name] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
                else:
                    dict_for_shop[ingredient_name]['quantity'] += ingredient['quantity'] * person_count

    return dict_for_shop
