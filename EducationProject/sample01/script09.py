city = {'name': 'Kyiv', 'people': 4e6}
print(city['name'], city['people'])

rec = {'name': {'first': 'Yuri', 'last': 'Biliai'},
       'job': ['lecturer'],
       'age': 33}

print(rec)
print(rec['name'])
print(rec['name']['first'])
print(rec['job'])
rec['job'].append('dev')
print(rec)


