#Merge two dictionaries into one. If there are overlapping keys, sum their values.
d1 = {'a' :23,
     'b':11}
d2 = {'b': 11,
      'c':1
     }
result = {}
for key, value in d1.items():
    result[key] = value
for key, value in d2.items():
    if key in result:
        result[key] = result[key] + value
    else:
        result[key] = value

print(result)

ANS:
{'a': 23, 'b': 22, 'c': 1}
