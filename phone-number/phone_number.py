class PhoneNumber:
    def __init__(self, number):
        import string

        if any(c.isalpha() for c in number):
            raise ValueError("letters not permitted")
        if any(c in string.punctuation and c not in " .-+()" for c in number):
            raise ValueError("punctuations not permitted")

        digits = "".join(c for c in number if c.isdigit())

        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(digits) == 11:
            if digits[0] != "1":
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]

        if digits[0] == "0":
            raise ValueError("area code cannot start with zero")
        if digits[0] == "1":
            raise ValueError("area code cannot start with one")
        if digits[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = digits

    @property
    def area_code(self):
        return self.number[:3]

    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"