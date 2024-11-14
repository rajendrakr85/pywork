from collections import Counter,ChainMap
x='abcabacbacbacbacabac'

cc = Counter(x)
d1={'name':'rajan'}
d2={'age':20}
d3={'salary':3000}
cmp= ChainMap(d1,d2,d3)

print(cmp.maps)