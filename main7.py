def create_dict():
    first_list = input("Введите список слов через запятую: ").split(',')
    first_set = set(first_list)
    len_first_set = len(first_set)
    print('Количество слов в сформированном списке без повторений: ', len_first_set)
    second_list = input('Для формирования второго списка введите {} слов(а): '.format(len_first_set)).split(',')
    return dict(zip(first_set, second_list))


file_name = input('Введите имя файла: ')
file = open(file_name + '.txt', 'w')
file.write(str(create_dict()))
file.close()
print('Словарь записан в файл {}.txt'.format(file_name))
