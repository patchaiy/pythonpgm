k1=int(input())
s1=0
for p in range(0,k1):
  if(pow(2,p)>k1):
    break
  s1=k1-pow(2,p)
print(s1)
