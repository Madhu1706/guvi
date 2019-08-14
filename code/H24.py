def func(n,p,x):
    for i in range(0,n):
        j=i+1
        for m in range(j,n):
            if((x[i]+x[m])==int(p)):
                return "YES"
    return "NO"   
n,p=[int(x) for x in input().split()] 
x=[int(x) for x in input().split()]
print(func(n,p,x))
