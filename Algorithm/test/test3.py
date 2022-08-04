from collections import Counter, defaultdict, OrderedDict

a = defaultdict(int)
print(a)
a['B'] = 3
a['C'] += 1
a['B'] += 1
print(a)

b = [2, 3, 3, 4, 5, 6]

c = Counter(b)

print(c)
print(c.most_common(2))

T = {'1': 1, '2': 4}
OrderedDict(T)
print(T)

print(T)
