x=int(input("Enter the value="))
if(x<=1):
 print("Not prime")
elif(x==2):
 print("prime number")
 for i in range (1,x):
    if(x%i==0):
     print("NOt Prime")
    else:
        print("Prime")
else:
    print("Prime")
