from collections import Counter, defaultdict, namedtuple

elements = ['apple', 'banana', 'apple', 'banana', 'mango', 'berry','banana']
#print(Counter(elements).most_common(1))
dd = defaultdict(list)
dd['a'].append(1)
dd['a'].append(2)
dd['b'].append(3)
#print(dd)
Point = namedtuple('Point', 'x y')
p =Point(3, 5)
print(p.x, p.y)