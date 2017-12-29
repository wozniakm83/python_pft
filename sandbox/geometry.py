from geom2d import *

a = Point(0, 0)
b = Point(3, 4)
print(a.distance(b))
print(a == b)
print(a == Point(0, 0))

l1 = [Point(3, 1), Point(1, 2), Point(2, 1)]
#l2 = [Point(0, 0), Point(1, 2), Point(2, 1)]
l2 = list(l1)
l2[0] = Point(0, 0)

print(l1 == l2)

l2 = sorted(l1)
print(l2)

def x(p):
    return p.x

l2 = sorted(l1, key=x)
print(l2)

def y(p):
    return p.y

l2 = sorted(l1, key=y)
print(l2)

l2 = sorted(l1, key=lambda p: p.x)
print(l2)

l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))
print(l2)

l = []

for i in range(-5, 6):
    l.append(Point(i, i*1))

for el in l:
    print(el)

l2 = []

for el in l:
    l2.append(Point(el.x, -el.y))

print(l)
print(l2)

l = [Point(i, i*i) for i in range(-5, 6)]
l2 = [Point(el.x, -el.y) for el in l]

print(l)
print(l2)

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))
l2 = list(map(lambda p: Point(p.x, -p.y), l))

print(l)
print(l2)

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))
l2 = list(filter(lambda p: p.x > 0, l))

print(l2)

l = list(map(lambda i: Point(i, i*i), range(-5, 6)))
l2 = list(filter(lambda p: p.x % 2 == 0, l))

print(l2)

