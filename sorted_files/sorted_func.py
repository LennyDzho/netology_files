
def get_sorted_files_file():
    list_words = [] #список, в который я запихну все содержимое файлов
    num = 1

    try:
        for i in range(1, 4):
            with open(f'sorted_files/files_for_ex_three/{i}.txt', 'r', encoding='utf-8') as file:
                content = file.read()  # читаем всё содержимое файла как одну строку
                num_newlines = content.count('\n')  # считаем количество символов новой строки
                list_words.append((num_newlines, content))
    except Exception as e:
        print(e)
        return -1
    list_words = sorted(list_words, key=lambda x: x[1])


    with open('sorted_files/sorted_files.txt', 'w', encoding='utf-8') as f:
        for file in list_words:
            f.write(f'{num}.txt \n')
            f.write(str(file[0]))
            f.write(f'{file[1]}\n')
            num += 1

    return 0
