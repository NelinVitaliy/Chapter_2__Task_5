a = int(input('Number of students in class A: '))
b = int(input('Number of students in class B: '))
c = int(input('Number of students in class C: '))
if (a%2) == 0:
  x1= int(a/2)
elif (a%2) == 1:
  x1= int(a/2) + 1
if (b%2) == 0:
  x2= int(b/2)
elif (b%2) == 1:
  x2 = int(b/2) + 1
if (c%2) == 0:
  x3= int(c/2)
elif (c%2) == 1:
  x3 = int(c/2) + 1
print('Number of benches needed is:', x1+x2+x3)