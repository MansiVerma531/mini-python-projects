menu={
    'pizza':80,
    'pasta':90,
    'burger':60,
    'sandwich':100,
    'honey chili potato':120}
print("welcome to our restaurant")
print("what would you like to eat.Select from the menu below:")
print("'pizza:80 rs'\n 'pasta:90 rs'\n 'burger:60 rs'\n 'sandwich:100 rs'\n 'honey chili potato:120 rs")


order_total=0
while True:

    c=input("enter your choice").lower()
    if c in menu:
        print("you have to pay {} rs for {}" .format(menu[c],c))
    else:
        print("sorry,not available")
        order_total=order_total+menu[c]


    i=input("want something else ?")
    
    if i == "yes":
          c = input("enter your choice: ").lower()
          print("you have to pay {} rs for {}".format(menu[c], c))
          order_total = order_total + menu[c]
          print("total is", order_total)
    else:
          order_total = order_total + menu[c]
          print("total is", order_total, ", you can pay either by cash or UPI.")