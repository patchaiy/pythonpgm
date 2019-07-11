def longest(st1,st2):
        if(st1 in st2):
            return st1
        else:
            return longest(st1[0:len(st1)-1],st2)
a = int(input())
n= []
for _ in range(0,a):
    n.append(input())
n.sort()
print(longest(n[0],n[a-1]))
