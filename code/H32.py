n=int(input())
a=[int(x) for x in input().split()]
lst=[]
for i in range(0,len(a),2):
    lst.append(a[i])
if(len(lst)<=2):
    print(lst[0])
else:
    print(lst[1])
