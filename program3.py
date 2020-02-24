print('enter the no')
n = int(input())
b = list(bin(n))
print(b)
d = []
str = ""
for i in b :
	if i == '1' :
		str += i
	else :
		d.append(str)
		str = ""
d.sort(reverse = True)
print(len(d[0]))	

