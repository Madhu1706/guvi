n=int(input())
s=[int(x) for x in input().split()]
for i in range(0,n):
    a=s[i]
    s.remove(s[i])
    prod=1
    for j in s:
        prod*=j
    print(prod,end=" ")
    s.insert(i,a)
