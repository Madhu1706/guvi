n=int(input())
m=[]
for i in range(n): 
    lst=[] 
    lst=list(map(int,input().split()))
    m.append(lst) 
r=[] 
for i in m: 
    for j in i: 
        r.append(j)
r.sort()
for i in r: 
    print(i,end=" ")
