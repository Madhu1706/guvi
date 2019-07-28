import string
n=int(input())
a=list(map(int,input().split(" ")))
l=[]
while(len(a)!=0):
    l.append(str(max(a)))
    a.remove(max(a))
if(l[0]=='0'):
    if(l.count(l[0])==len(l)):
        k=0
        print(k)
else:    
   print("".join(l))
