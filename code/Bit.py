n=int(input())
a=[]*n
for i in range(0,2**n):
    k=[]
    for j in range(n-1,0,-1):
        k.append(int(i/2**j)%2)
    k.append(i%2)    
    a.append(k) 
    
for i in  a:
    b=''
    for j in i:
        j=str(j)
        b=b+j
    print(b)
