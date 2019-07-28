b=input()
j=0
for i in range(len(b)):
    if(b[j]<b[i]):
        print(b[i:])
        break
