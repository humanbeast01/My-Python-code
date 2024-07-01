'''my_list=lambda x,y:x//y
print(my_list(82,9),end="")
print()

string='Mukulgoswami'
x=string.swapcase()
print(x)

def my_fun():
      print(x)
x="Mukul Goswami"
my_fun()    
print(x)

    
        
for i in range(10):
    if(i>=5):
        continue
    print(i)

import math
print(math.floor(-23.11))
print(math.floor(300.154))

print(math.ceil(-24.99))
print(math.ceil(520.01))

x=int(input("Enter the value"))
for i in range (1,10,1):
    print(i*x)'''
#armstrong number
'''x=int(input("Enter the value="))

dig=x%10 #3
dig=dig**3 #9
dig3=x//10 #15
dig3=dig3%10 #5
dig3=dig3**3#125
dig6=dig3//10 #1
dig6=dig6**3 #1
sum=dig+dig3+dig6
if(sum==x):
    print("Armstrong")
else:
    print("Not")'''
#Calculator
'''a=int(input("Enetr the value of a"))
b=int(input("Enter the value of b"))
print("Addition=", a+b)
print("Subtraction=", a-b)
print("Multiplcation", a*b)
print("divide", a/b)'''
#Typecasting
'''a='2'
b='6'
print(int(a)+int(b))'''
#String in a loop
'''name="Mukul"

for i in name:
    print(i)'''


#string slicing
'''name="Mukul"
print(name[0:3])
print(name[1:-3])
print(name[1:-2])'''


#string method

'''name='Goswami!!'
print(name.upper())
print(name.lower())
print(name.rstrip('!'))
print(name.replace('Goswami','Mukul'))
print(name.split(" "))
print(name.isalnum())
print(name.islower())
print(name.isspace())
print(name.istitle())
print(name.swapcase())'''


#if else statement
'''a=int(input("Enter the age=="))
if(a>=18):
    print("Valid For voting")
else:
    print("Not Valid For Voting")'''
    
#elif statement
'''num=int(input("Enter the value of number="))
if(num<0):
    print("Number is less than num value")
elif(num==0):
    print("Number is equal to zero")
elif(num==25):
    print("Number is special")
else:
    print("Number is greater than zero")'''
    

#nested if else statement
'''num=int(input("Enter the number of your choice=="))
if(num<0):
    print("Number is less negative")
elif(num>0):
    print("Number is positive")
    if(num<=10):
        print("Number is greater than 10")
    elif(num>=11 and num<=20):
        print("Number lies between 11 and 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")'''

#match case
'''num=int(input("Enter the value of number=="))
match num:
    case 0:
        print("number is zero")
    case 1:
        print("number is 1")
    case 4:
        print("Number is 4")
    case _:
        print(num)'''


#for loop
'''num=int(input("Enter the value=="))
for i in range(1,100,10):
     print(i+1)'''
     
#WHILE LOOP
'''i=int(input("Enter the value of i="))
while(i<=3):
     print(i)
     i=i+1
else:
     print("Mukul Goswami")'''
#BREAK AND CONTINUE STATEMENT
for i in range(12):
     if(i==10):
          continue 
     
     print('5X',i+1,"=",5*(i+1))
     if(i==10):
          break
     
     
print("Exit")     






































     
        
        
