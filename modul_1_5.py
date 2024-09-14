immutable_var = ("dress", "shirt", 2, 8)
print(immutable_var)
immutable_var [1] = "hat"
print(immutable_var)
mutable_list = (immutable_var,'energy', 'sun', 'bulb')
print(mutable_list)

#почему нельзя изменить - числа выведены строкой, если я захочу изменить тип,
# то пишу команду int. но тогда
# не получим тот результат, который нужно, потому что будут разные типы данных -
# они между собой несовместимы