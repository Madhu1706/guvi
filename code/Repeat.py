n=int(input())
a=list(map(int,input().split(" ")))
s={}
for key in a:
    s[key]=a.count(key)

l=[]
for key,values in s.items():
    if(s[key]>1):
        l.append(key)
        
if l==[]:
    print("unique") 
else:       
  l.sort()
  for i in l:
    print(i,end=" ")    
