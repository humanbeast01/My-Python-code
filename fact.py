#progrtam to print factorial of number
num=int(input("Enter The number=")) #5
fact=1
a=1
while a<=num: #1<5,2<5,3<5,4<5,5=5,(6>5 condition false here)
    fact=fact*a #1*1,1*2,2*3,4*6,5*24
    a=a+1 #2,3,4,5,6

    print("Result of ",num,"is",fact)
    
