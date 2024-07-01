import random
target = random.randint(1,100)
while True:
   userchoice = input("Guess the target or Quit")
   if(userchoice == "Quit"):
     break

   userchoice=int(userchoice)
   if(userchoice == target):
      print("Success:")
      break
if(userchoice < target):
        print("Your no. is small")
else:
     print("Your number is big")



print("Game over.....")      
