a=int(input())
l1=[int(x) for x in input().split()] 
l2=[int(x) for x in input().split()]
l3=[]
for i in range(0,a):
    l3.append(l1[i]+l2[i])
print(*l3)
