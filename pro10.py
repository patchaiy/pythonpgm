a1=int(input())
b1=list(map(int,input().split()))
c=0
for m in range(0,a1):
	for p in range(0,m):
		if b1[p]<b1[m]:
			c=c+b1[p]
print(c)
