Item_name= { 'bread':35,
             'choco chips':50,
             'lassi':60,
             'kurkare':90,
             'butter':55,
             'chicken':80,
             'waffle':60
}

# function one for showing all item in stock
def show_all():
    print("\navailable items:")
    for key,value in Item_name.items():
        print(f"{key}:{value}")

# function second for ordering items
def order_now(product_name,quantity):

    if product_name in Item_name:
        price = Item_name[product_name]   # FIXED (item_name -> Item_name)
        total_price= price * quantity
        print("\norder summary")
        print("Item:",product_name)
        print("Price:",price)
        print("Total price:",total_price)
        return total_price
    else:
        print("Sorry, product not found")
        return 0

# function for payment
def payment_option(total_price):
    while True:
        amount = int(input("\nHow much money do you want to pay: "))
        if amount >= total_price:     # FIXED (== -> >=)
            print("\npayment was successful")
            print("Change:", amount-total_price)
            break
        else:
            print("\npayment was not successful\nplease try again later")

# funtion to add new item in dict
def add_item():
    while True:
        product_name=input("\nEnter product name: ")
        price=int(input("Enter price: "))
        Item_name[product_name]=price
        print("Item added","item name:",product_name)

        choice = input("\nWould you like to add another item? (yes/no): ")
        if choice != 'yes':
            break


show_all()

product_name=input("\nEnter product name: ")
quantity=int(input("Enter quantity: "))
total_price=order_now(product_name,quantity)

if total_price>0:
    payment_option(total_price)

# optionally allow adding items
add_more=input("\nWould you like to add another item? (yes/no): ")
if add_more == 'yes':
    add_item()
    show_all()
