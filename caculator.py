print("Smart Calculator")
calculator={
    1:'Addition or sum or plus or +',
    2:'Subtraction or sub or -',
    3:'Multiply or mul or *',
    4:'Division or div or /',
    };
print(calculator)

choice=input("Enter your Choice=")
if choice in ('+','-','*','/'):
           x=int(input("Enter the value of x="))
           y=int(input("Enter the value of y="))
           if choice == '+':
              print(x+y)
           if choice == '-':
               print(x-y)
           if choice == '*':
               print(x*y)
           if choice == '/':
               print(x/y)
        
'''choice=input("Enter your choice=")
#if choice in ('Add' or 'Addition','3','4'):
x=int(input("Enter the value of x="))
y=int(input("Enter the value of y="))
if (choice == 'Add'or 'sum' or '+'):
     print(x+y)
elif (choice == 'Subtract' or 'sub' or '-'):
    print(x-y)
elif (choice == 'Multiplication' or '*'):
    print(x*y)
else:
    choice == 'Division' or '/'
    print(x/y)'''
    
        













'''x=int(input("Enter the value of x="))
y=int(input("Enter the value of y="))
result=input("Your result=")
if(result == 'Addition' and 'Sum' or 'Plus'):{
    
    print(x+y)
     
       
}
elif(result == 'Subtraction' or 'Sub'):{
    
    print(x-y)
    
    }

elif(result == 'Multiply' or 'Mul'):{
    print(x*y)
 
    }
elif(result == 'Divide' or 'Div'):{
    print(x/y)
   
    }
    
else:
    print("Not defined")'''

