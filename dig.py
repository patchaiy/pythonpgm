a,b=input().strip().split(" ")
b=int(b)
c=0
while c<len(a)-1 and b:
	if(a[c]>a[c+1]):
		b-=1
		a=a[:c]+a[c+1:]
		if(c!=0):
			c-=1
	else:
		c+=1
r=a[:len(a)-b]
print(r)
