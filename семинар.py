# first_list = [1,2,3]
# second_list = ['a', 'b', 'c']
# some_dict = {}
# for i in range(len(second_list)):
#     some_dict[first_list[i]]=second_list[i]
# print (some_dict)

#1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:>>> num_translate("one")"один"
# >>> num_translate("eight")"восемь"
# Если перевод сделать невозможно, вернуть None. 
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

# first_list = ['zero', 'one', 'two','three','four']
# second_list = [1,2,3,4]
# some_dict = {}
# for i in range(len(second_list)):
#      some_dict[first_list[i]]=second_list[i]
# print (some_dict)

# print(some_dict.get(input('введите слово: '),'Нет значения'))

#2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): 
# реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One") "Один"
# >>> num_translate_adv("two") "два"
# some_dict = {"One" : "Один","one" : "один","Two" : "Два","two" : "два",}
# print(some_dict.get(input('введите слово: '),'Нет значения'))
# def num_translate(number):
#     translate_dict = {'one': 'один', 'two':'два', 'three':'три'}
#     if number[0].isupper():
#         print(translate_dict.get(number.lower()).capitalize())
#     else:
#         print(translate_dict.get(number))

# num_translate('One')
# num_translate('one')

# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья"){"И": ["Иван", "Илья"],"М": ["Мария"], "П": ["Петр"]}
# some_list = ["Иван", "Мария", "Петр", "Илья"]
# some_dict = {}
# for i in range(len(some_list)):
#     if some_list[i][0] in some_dict:
#         some_dict[some_list[i][0]].append(some_list[i])
#     else:
#      some_dict[some_list[i][0]] = [some_list[i]]
# print(some_dict)

def thesaurus(*args):
    some_dict = {}
    for i in args:
        if i[0] in some_dict.keys():
            some_dict[i[0]].append(i)
        else:
            some_dict[i[0]] = [i]
    print(some_dict)

thesaurus("Иван", "Мария", "Петр", "Илья")

# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую словарь, 
# в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, 
# в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {"А": {"П": ["Петр Алексеев"]},"И": {"И": ["Илья Иванов"]},"С": {"И": ["Иван Сергеев", "Инна Серова"],"А": ["Анна Савельева"]}}