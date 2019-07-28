n=int(input())
a=list(map(int,input().split(" ")))
l=[]
while(len(m)!=0):
   if len(m)>1: 
    l.append(max(a))
    l.append(min(a))
    a.remove(max(a))
    a.remove(min(a))
   else:
       l.append(max(a))
       a.remove(max(a))
for i in l:
     print(i,end=" ")   
