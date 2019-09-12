import time
from collections import Counter
start = time.time()
perimeters = []
for a in xrange(1, 500):
    for b in xrange(a, 500):
        c = (a**2 + b**2)**0.5
        if int(c) == c and a + b + c <= 1000:
            perimeters.append(a+b+c)

p = Counter(perimeters)

print(p.most_common(1)[0])
 t = time.time()
print(t) 