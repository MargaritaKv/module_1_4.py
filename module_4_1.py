from fake_math import divide as fake_divide
from true_math import divide as true_divide
first_value = 10
second_value = 0
fake_result = fake_divide (first_value, second_value)
true_result = true_divide (first_value, second_value)
print ("Результат fake_math.divide:", fake_result)
print ("Результат true_math.divide:", true_result)