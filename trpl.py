a=int(input())
b=list(map(int,input().split()))
c=0
for i in range(a):
  for j in range(i,a):
    for m in range(j,a):
      if(b[i]<b[j]<b[m]):
        c+=1
print(c)
