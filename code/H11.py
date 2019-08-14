s=input()
p=s.split()
for i in range(0,len(p)):
    n=p[i] 
    res=list(n)
    res.reverse()
    x="".join(res)
    print(x,end=" ")
