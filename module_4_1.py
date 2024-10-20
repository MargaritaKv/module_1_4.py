from fake_math import divide as fake_divide
from True_math import divide as True_divide
def run_divisions ():
    num1 = 10
    num2 = 0
    result_fake = fake_divide(num1, num2)
    try:
        result_True = True_divide(num1, num2)
    except ValueError as e: result_True = str (e)
    print (f"Результат fake_divide: {result_fake}")
    print (f"Результат True_divide: {result_True}")
if __name__ == "__main__": run_divisions()
