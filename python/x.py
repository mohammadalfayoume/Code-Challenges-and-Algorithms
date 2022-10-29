s= input()
AB = s.find("AB")
BA = s.find("BA", AB+2)
BA2 = s.find("BA")
AB2 = s.find("AB",BA2+2 )

if AB != -1 and BA != -1 and BA2 != -1 and AB2 != -1:
    print("YES")
else:
    print("NO")
