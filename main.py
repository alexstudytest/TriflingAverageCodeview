


'''

n, m = [int(i) for i in input().split()]

#for k in range(n):
  #matrix.append([int(x) for x in input().split()])

matrix = [["."] * m for i in range(n)]

for i in range(n):
  if i == 0 or i % 2 == 0:
    for j in range(1, m, 2):
      matrix[i][j] = '*'
  else:
    for j in range(0, m, 2):
      matrix[i][j] = '*'

for i in matrix:
  print(*i)
'''


"""
n = int(input())
matrix = []

for k in range(n):
  matrix.append([int(x) for x in range(n)])

for i in range(n):
    for j in range(n):
        if i == n - 1 -j:
            matrix[i][j] == 1
        elif i < n - 1 - j:
            matrix[i][j] == 0
        elif i > n - 1 -j:
            matrix[i][j] == 2
for i in range(n):
    print(*matrix[i])


def f(i, j, n):
  if i == n - j - 1:
    return 1
  elif i < n - j - 1:
    return 0
  else:
    return 2

n = int(input())

res = [[f(i, j, n) for j in range(n)] for i in range(n)]

for x in res:
  print(*x)
"""
"""
myset = {'python'}
print(type(myset))
item = myset.pop()
print(item, len(myset))


myset = set('python')
print(type(myset))
item = myset.pop()
print(item, len(myset))
"""
"""
set1 = {'a', 'b', 'c', 'd', 'h'}
set2 = {'b', 'd', 'f', 'h'}

set3 = set1 - set2 & set1
print(set3)
set1, set2, set3 = [set(int(num) for num in input().split()) for i in range(3)]
print(*sorted(set(set1.intersection(set2).difference(set3)))[::-1])"""


a = "123"
b = "456"
ab = a.replace("1", "0") + b
print(ab)
a.replace("1", "0")
print(a)
