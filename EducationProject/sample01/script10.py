d = {'a': 1, 'b': 2, 'c': 3}
print(d)

keys = list(d.keys())
print(keys)

keys.sort()
print(keys)

for k in keys:
    print(k, '=>', d[k])

for k in reversed(sorted(d)):
    print(k, '=>', d[k])

for c in "Hello":
    print(c.upper())

x = 4
while x > 0:
    print('Hi' * x)
    x -= 1

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)
squares2 = {x: x ** 2 for x in [1, 2, 3, 4, 5]}
print(squares2)

sq = squares2.get(5, 0)
print(sq)
