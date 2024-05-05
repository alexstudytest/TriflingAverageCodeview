'''
a = input()
print("+7 (" + a[1:4] + ") " + a[4:7] + "-" + a[7:9] + "-" + a[9:11])
'''


'''
a = int(input())
b = int(input())
operate = str(input())
if operate == "+":
  print(a + b)
elif operate == "-":
  print(a - b)
elif operate == "*":
  print(a * b)
elif operate == "/":
  print(a / b)
'''
'''
a = int(input())
b = int(input())

for i in range(a, b + 1):
  print(i, end=" ")
  '''
'''
n = int(input())
a = 1
for i in range(2, n + 1):
 a += i ** i
print(a)
'''
'''
n = int(input())
c = 1
for i in range(n + 1):
  if i % 2 == 0:
    c -= i ** i
  elif i % 2 != 0:
    c += i ** i
print(c)
'''
'''
a = int(input())
b = int(input())
for i in range (a,b + 1):
  print(i)
  '''   
'''
a = int(input())
b = int(input())
c = 0
while a >= b:
  a -= b
  c += 1
print(c, a)
 
a = [str(input()), str(input()), str(input())]
print(a[0], a[2])
'''
'''
n = int(input()) * 2
list =[]
for i in range(n):
  if i % 2 != 0:
    list.append(i)
print(list)
'''
'''
a = [int(input()), int(input()), int(input()), int(input())]
print(sum(a) / 4)
'''

a = int(input())
b = []
for i in range(a):
  b.append(input())
for i in b:
  print(i)