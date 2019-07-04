lowr,uppr=map(int,input().split())
for numr in range(lowr,uppr + 1):
   if numr > 1:
       for n in range(2,numr):
           if (numr % n) == 0:
               break
       else:
           print(numr,end=' ')
