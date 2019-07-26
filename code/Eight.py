a=int(input())
b=[]
for i in range(a):
    l=[]
    l=list(map(int,input().split()))
    b.append(l)
 
m=[]   
for i in b:
    for j in i:
        m.append(j)
m.sort()
for i in m:
    print(i,end=" ")
