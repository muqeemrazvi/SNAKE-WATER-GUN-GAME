import random

cmp=random.randint(1,3)
if(cmp==1):
    a="s"
elif(cmp==2):
    a="w"    
elif(cmp==3):
    a="g"

b=input("your  turn : snake(s) , water(w) , gun(g) : ")
print("compueter choice :" +a)
if((a=="s" and b=="w") or (a=="g" and b=="s") or (a=="w" and b=="g")):
    print("computer win")
elif(a==b):
    print("draw")    
else:
   print("You win")

    