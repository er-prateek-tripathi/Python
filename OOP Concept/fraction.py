class Fraction:

    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def __str__(self):  # gets triggered when something is to be printed
        return '{}/{}'.format(self.numerator, self.denominator)

    def __add__(self, other):  # gets triggered when some values are given to add

        temp_num = self.numerator * other.denominator + other.numerator * self.denominator
        temp_den = self.denominator * other.denominator
        return Fraction(temp_num, temp_den)

    def __sub__(self, other):  # gets triggered when some values are given to subtract

        temp_num = self.numerator * other.denominator - other.numerator * self.denominator
        temp_den = self.denominator * other.denominator
        return Fraction(temp_num, temp_den)

    def __mul__(self, other):  # gets triggered when some values are given to multiply

        temp_num = self.numerator * other.numerator
        temp_den = self.denominator * other.denominator
        return Fraction(temp_num, temp_den)

    def __truediv__(self, other):  # gets triggered when some values are given to divide

        temp_num = self.numerator * other.denominator
        temp_den = self.denominator * other.numerator
        return Fraction(temp_num, temp_den)
