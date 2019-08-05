s=input()
j=0
for i in range(len(s)): 
    if(s[j]<s[i]):
        print(s[i:]) 
        break
