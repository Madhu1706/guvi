n,q=map(int,input().split())
m=list(map(int,input().split()))
m.sort()
m.reverse()
s=q
r=0
for i in m: 
    if(s>=i):
        no=int(s/i) 
        r=r+no 
        s=s-no*i 
    if s==0: 
        break
if(s==0):
    print(r)
else: 
    print("it's not posiible to select coins in such a way that they sum upto",q)
