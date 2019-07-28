n=input()
l=[]
for i in range(len(n)):
    if n[i]!=' ':
        l.append(n[i])
for i in l:
 if ord(i)>=65 and ord(i)<=90:
     l.remove(i)
     l.append(i.lower())        
        
d={'a':l.count('a'),'b':l.count('b'),'c':l.count('c'),'d':l.count('d'),'e':l.count('e'),
   'f':l.count('f'),'g':l.count('g'),'h':l.count('h'),'i':l.count('i'),'j':l.count('j'),
   'k':l.count('k'),'l':l.count('l'),'m':l.count('m'),'n':l.count('n'),'o':l.count('o'),
   'p':l.count('p'),'q':l.count('q'),'r':l.count('r'),'s':l.count('s'),'t':l.count('t'),
   'u':l.count('u'),'v':l.count('v'),'w':l.count('w'),'x':l.count('x'),'y':l.count('y'),
   'z':l.count('z')}
count=1
for key,value in d.items():
    if d[key]==0:
        count=0
        break
if(count):
   print("yes")
else:
   print("no")    
