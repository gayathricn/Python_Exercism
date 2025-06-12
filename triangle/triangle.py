def equilateral(sides):
    a, b, c = sorted(sides)
    if a + b <= c:
        return False
    return a == b == c

def isosceles(sides):
    a, b, c = sorted(sides)
    if a + b <= c:
        return False
    return a == b or b == c or a == c


def scalene(sides):
    a, b, c = sorted(sides)
    if a + b <= c:
        return False
    return a != b and b != c and a != c
