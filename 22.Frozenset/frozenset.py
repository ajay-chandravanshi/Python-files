s='ajay'
fs=frozenset(s)
print(type(fs))
print(fs)
print(max((fs)))
y=fs.copy()
print(y)
A={2,4,6,8}
x=frozenset(A)
B={1,2,3,4,6,8}
y=frozenset(B)
print(x.difference(y))
print(x.symmetric_difference(y))
print(x.union(y))
print(x.intersection(y))
print(x.isdisjoint(y))

print(y.issuperset(x))
print(x.issubset(y))