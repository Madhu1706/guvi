a=int(input())
for i in range(1,a+1):
    if(i%2==0):
        if(a%i==0):
            print(i,end=" ")
