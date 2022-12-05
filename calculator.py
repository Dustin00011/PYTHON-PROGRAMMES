print("#########CALCULATOR###########")
a=int(input("FIRST NO:"))
b=int(input("SECOND NO:"))
c=input("YOUR OPERATOR:")
if c=="+":
    print(int(a)+int(b))
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)
elif c=="//":
    print(a//b)
else:
    print("invalid wrong1")
    
print("HERE'S YOUR ANS/nNOW ENJOY!!!!!")