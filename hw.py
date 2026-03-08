result = []

def divider(a, b):
    if a < b:
        raise ValueError
    if b > 100:
        raise IndexError
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except ValueError:
        print("Помилка, так не можна")
    except ZeroDivisionError:
        print("Помилка, на нуль ділити не можна")
    except TypeError:
        print("Помилка: це не число, так не можна")

print(result)