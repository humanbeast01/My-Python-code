menu={
    'Pizza':40,
    'Burger':50,
    'Salad':60,
    }
print("Welcome to our Dilip Bhaiya restaurant")
print("Pizza: Rs40\n Burger: Rs50 \n Salad:60")
order_total=0

item_1=input("Enter the item do you want to add=")
if item_1 in menu:
    order_total=order_total+menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print("ordered item is not available yet")

another_order=input("Do you want add another item ? (Yes/No)")
if another_order=="Yes":
    item_2=input("Enter your another item =")
    if item_2 in menu:
        order_total=order_total+menu[item_2]
        print(f"Ordered item {item_2} is added")

    else:
        print(f"Ordered item {item_2} is not available")
else:
    print("Please check another item ")

another_order=input("Do you want to add more item(Yes/No)")
if another_order=="Yes":
    item_3=input("Enter your item= ")
    if item_3 in menu:
        order_total=order_total+menu[item_3]
        print(f"Orderd item {item_3} added successfully")
    else:
            print(f"Ordered item {item_3} is not available")
else:
    print("Thank you for your order Sir/Madam ")

print("Your total amount to be pay",order_total)
print("Dilip Bhaiya Cafe always Available for  your Service")
print ("Visit Again")
