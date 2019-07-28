a=int(input())
b=[]*a
for i in range(0,2**a):
    s=[]
    for j in range(a-1,0,-1):
        s.append(int(i/2**j)%2)
    s.append(i%2)    
    b.append(k) 
    
for i in  b:
    k=''
    for j in i:
        j=str(j)
        k=k+j
    print(k)    
