p=int(input())
s=[]
for i in range(p):
    l=[]
    l=list(map(int,input().split()))
    s.append(l)
 
m=[]   
for i in s:
    for j in i:
        m.append(j)
m.sort()
for i in m:
    print(i,end=" ")
