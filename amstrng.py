p=int(input())
tmp=p
sum=0
while tmp>0:
  digit=tmp%10
  sum=sum+digit**3
  tmp=tmp//10
if p==sum:
  print("yes")
else:
  print("no")
