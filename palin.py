'''x=int(input("Enter the number you wnt to check="))
reverse=0
temp=x
while(x>0):
    dig=x%10 #153%10=3 #15%10=5 1
    reverse=(reverse*10)+dig #3 #35 351
    x=x//10 #153//10=15 1
if(temp==reverse):
    print("The number is palindrom")
else:
    print("not")''' 

x=int(input("Enter the value :"))
reverse=0
temp=x
dig=x%10 #3 5 1
reverse=reverse+(dig*dig*dig)#9 125 1 
x=x//10 #15 1 
if(temp==reverse):
    print("Armstrong ")
else:
    print("Not")
