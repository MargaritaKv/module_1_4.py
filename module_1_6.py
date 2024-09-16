my_dict = {'Анна' : 2013, 'Юлия' : 2013, 'Валерия' : 2003}
print ("Мои дети:", my_dict)
print ('Год рождения Анны:', my_dict.get('Анна'))
missing_value = my_dict.get ('Юлия', 'ключ не найден')
print ('Год рождения Юлии:', missing_value)
my_dict["Маргарита"] = 1982
my_dict["Алексей"] = 1978
removed_value = my_dict.pop ("Валерия" , "Ключ не найден")
print("Удаленный год рождения Валерии:", removed_value)
print("Обновленные данные", my_dict)

my_set = {5, 7, 9, "Lessi", 3.15, "Lessi", True, False}
print (my_set)
my_set.add(99)
my_set.add("Dolly")
my_set.pop()
print("Обновленные данные:", my_set)
