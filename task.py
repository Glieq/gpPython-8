# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

def imp():
    with open('guide.txt', 'a', encoding='utf-8') as file:
        fio = input("")
        file.write('' + fio)
        print("Человек добавлен")


def exp():
    with open('guide.txt', 'r', encoding='utf-8') as file:
        all_text = file.read()
        all_text_list = all_text.split('\n')
        find_fio = input("Введите фамилию для поиска: ")
        # print(file.readline())
        print(all_text_list)
        for member in all_text_list:
            member = member.split(' ')
            for need_member in member:
                if need_member == find_fio:
                    print(" ".join(member))


def interface():
    while True:
        mode = input("Режим работы: imp - import, exp - export, 0 - выход \n")
        if mode == "imp":
            imp()
        elif mode == "exp":
            exp()
        elif mode == "0":
            break
        else:
            print("Вы ввели неккоректный режим работы")


interface()
