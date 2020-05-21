m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(m)
print(m[1])
col2 = [row[1] for row in m]
print(col2)
print([row[1] for row in m if row[1] % 2 == 0])
print([m[i][i] for i in [0, 1, 2]])

print([c * 2 for c in 'Hello'])

g = (sum(r) for r in m)
print(next(g))
print(next(g))
print(next(g))

l = list(map(sum, m))
print(l)

print({sum(r) for r in m})
print({i: sum(m[i]) for i in range(3)})

print([ord(x) for x in 'Hello'])
print({ord(x) for x in 'Hello'})
print({x: ord(x) for x in 'Hello'})
