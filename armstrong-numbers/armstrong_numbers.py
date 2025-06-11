def is_armstrong_number(number):
    return number == sum(map(lambda i: int(i) ** len(str(number)), str(number)))
