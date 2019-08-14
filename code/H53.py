a,n=input().split()
n=int(n)
for i in range(0,len(a)):
    print(a[i:n],end=" ")
    if(n<len(a)):
        n=n+1
    else:
        break
