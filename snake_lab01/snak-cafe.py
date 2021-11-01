MenuList = [

{'type':'Appetizers','foods':['Wings','Cookies','Spring Rolls',]},
{'type':'Entrees','foods':['Salmon','Steak','Meat Tornado','A Literal Garden',]},
{'type':'Desserts','foods':['Ice Cream','Cake','Pie',]},
{'type':'Drinks','foods':['Coffee','Tea','Unicorn Tears',]},

      ]




print("""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our Menu below.    **
**
** To quit at any time, type "quit" **
**************************************""")
print("""Appetizers
----------
Wings
Cookies
Spring Rolls
""")
print("""Entrees
----------
Salmon
Steak
Meat Tornado
A Literal Garden
""")
print("""Desserts
--------
Ice Cream
Cake
Pie
""")
print("""Drinks
------
Coffee
Tea
Unicorn Tears
""")

ordersList = []
count = 0
flare = 1
while flare == 1:
    order = input("""***********************************
    ** What would you like to order? **
    ***********************************
    >""")

    if order == "quit":
        flare = 0
        break
    else:
        for foodtype in MenuList:
            for kind in foodtype["foods"]:
                if order.lower() == kind.lower():
                    ordersList.append(order)
                    if order in ordersList:
                        count = ordersList.count(order)
                        print(f"** {count} orders of {order} has\have been added to your meal **")
                        break
                    else:
                        print(f"** {count} orders of {order} has\have been added to your meal **")