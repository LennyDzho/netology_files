from for_organization.organizations_dishes import get_shop_list_by_dishes
from for_read.txt_to_dict import to_dict
from sorted_files.sorted_func import get_sorted_files_file

'''
Задание 1

Функция, которая создает словарь на основе файлике лежит 
в папке в for_read в файлике txt_to_dict

'''

cook_dict = to_dict('recipes.txt')
print(cook_dict)

'''
Задание 2
Функция лежит в папке в for_organization
 в файлике organizations_dishes

Не знаю, как сделать без цикличного импорта, и при этом повторно не считывать файлик recipes.txt,
поэтому передаю cook_dict как аргумент.
Так бы просто вызвал to_dict повторно в get_shop_list_by_dishes.

'''

new_cook_dict = get_shop_list_by_dishes(cook_dict, ['Запеченный картофель', 'Омлет'], 2)
print(new_cook_dict)


'''
Задание 3
Функция лежит в папке в sorted_files
 в файлике sorted_func
'''

get_sorted_files_file()
