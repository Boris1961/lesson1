import collections

c = collections.Counter()

dic = ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']

for word in dic :
    c[word] += 1

print(c)

"""
print(c['counter'])

print(c['collections'])

"""
