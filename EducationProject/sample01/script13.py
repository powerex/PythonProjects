import decimal
from fractions import Fraction
print(1 / 3)
print((2 / 3) + (1 / 2))

d = decimal.Decimal('3.1415')
print(d + 1)

decimal.getcontext().prec = 2
d2 = decimal.Decimal('1') / decimal.Decimal('3')
print(d2)

f = Fraction(2, 3)
print(f + 1)
print(f + Fraction(1, 2))
