def longest(st1,st2):
        if(st1 in st2):
            return st1
        else:
            return longest(st1[0:len(st1)-1],st2)
j = int(input())
p= []
for _ in range(0,j):
    p.append(input())
p.sort()
print(longest(p[0],p[j-1]))
