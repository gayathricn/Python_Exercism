def is_valid(isbn):
    isbn = isbn.replace("-", "").replace(" ", "")
    if len(isbn) != 10:
        return False

    total = 0
    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (10 - i)

    # Handle last digit
    last = isbn[9]
    if last == 'X':
        total += 10
    elif last.isdigit():
        total += int(last)
    else:
        return False

    return total % 11 == 0

 

        
        



