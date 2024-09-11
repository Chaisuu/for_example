def clear_names(file_names:str) -> list:
    """ Функция для отвисви мет от лишних символов"""
    new_name_list = list()
    with open('data/'+ file_names, encoding="utf-8") as names_file: # Открываем файл и для него создали переменную name_file
        names_list = names_file.read().split() # мы только что открытый файл читаем и разлеяем на строки
        for name_item in names_list:  # начинается блок где мы имена т.е. строки чистим, каждую строку итерируем по буквам в строке
            new_name = ''
            for symbol in name_item:   # для каждого символа в строке
                if symbol.isalpha():  # условие которое должно удовлетврорять
                    new_name += symbol   # добавлять этот символ та то же место
            if new_name.isalpha():
                new_name_list.append(new_name)
    return new_name_list


if __name__ == '__main__':
    cleared_name = clear_names('names.txt')

    for i in cleared_name:
        print(i)