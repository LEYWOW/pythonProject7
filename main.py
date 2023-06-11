result = []


def divider(a, b):
    try:
        a = float(a)
        b = float(b)

        if a < b:
            raise ValueError("a менше, ніж b")  # a is less than b
        if b > 100:
            raise IndexError("b більше 100")  # b is greater than 100
        if b == 0:
            raise ZeroDivisionError("ділення на нуль")  # division by zero

        return a / b

    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(
            f"Виняток: {type(e).__name__} - {str(e)}")  # Exception occurred: <тип винятку> - <повідомлення про помилку>
        return None


data = {"10": "2", "2": "5", "123": "4", "18": "0", "": "15", "8": "4"}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
