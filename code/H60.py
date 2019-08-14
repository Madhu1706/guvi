b=int(input())
l1=[int(x) for x in input().split()] 
l2=[int(x) for x in input().split()]
l=[]
for i in range(0,b):
    l=l1[i:]+l1[:i]
    if(l==l2):
        print(i)
        break
