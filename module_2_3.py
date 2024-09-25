from ast import Index

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Index = 0
while Index < len(my_list):
    number = my_list[Index]
    if number > 0:
        print (number)
    if number < 0:
        break
    Index += 1
