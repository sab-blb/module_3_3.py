print(f"{"Задача"} {'"Распаковка"'}")

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print("Функция с параметрами по умолчанию:")
print_params()
print_params(b = 25)
print_params(c = [1,2,3])


values_list = [30, "Alexandr", False]
values_dict = {'a': 28, 'b': "Balabanov", 'c': True}
print("\nРаспаковка параметров:")
print_params(*values_list)
print_params(**values_dict)


values_list_2 = [54.32, 'Строка']
print("\nРаспаковка + отдельные параметры:")
print_params(*values_list_2, 42)
