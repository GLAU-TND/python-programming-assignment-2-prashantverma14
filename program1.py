print('enter the value')
n = int(input())
a = []
for i in n :
	a.append(input())
print(a)
b = []
count = 1
b.append(a[0])
while count!=n :
	for j in a:


		if b[-1].endswith(j[0])
			if j not in b :
				b.append(j)
				count += 1
print(b)
