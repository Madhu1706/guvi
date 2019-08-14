m=int(input())
n=[int(x) for x in input().split()] 
c=min(n)
d=max(n)
a1=n.index(c)
a2=n.index(d)
print(a1+1,a2+1)
