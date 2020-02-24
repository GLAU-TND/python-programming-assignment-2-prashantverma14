print('enter the number you want to enter ')
n = int(input())
a = []
for i in range(n) :
	a.append(input())
a.sort(reverse = True)
c = int(''.join(map(str,a)))
print(c)
