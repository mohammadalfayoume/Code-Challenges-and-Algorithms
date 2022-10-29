s= input()
cout_AB=0
cout_BA=0
p1=0
p2=1
while p2< len(s):
    if s[p1]+s[p2]== "AB":
        cout_AB+=1
    if s[p1]+s[p2]== "BA":
        cout_BA+=1
    if len(s)%2 !=0 and p2 == len(s) -2:
        p1+=1
        p2+=1
    else:
        p1+=2
        p2+=2
if cout_AB==1 and cout_BA==1:
    print("YES")
else:
    
    print("NO")