cb=int(input())
s=list(map(int,input().split()))
a=0
for f in range(cb):
    for e in range(f,cb):  
        for r in range(e,cb):
            if s[f]<s[e]<s[r]:
                a+=1
print(a)
