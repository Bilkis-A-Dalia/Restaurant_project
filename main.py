from Menu import Pizza,Burger,Drinks,Menu
from Restaurant import Restaurant
from User import Chef,Customer,Manager,Server
from Order import Order

def main():
    menu = Menu()

    # add pizza to the menu
    pizza_1 = Pizza('Marinara pizza',600,'large',['Garlic','Olive'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2 = Pizza('Capri pizza',400,'large',['Mozaewlla','Tomato'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3 = Pizza('Etna pizza',800,'large',['Tomato','Olive'])
    menu.add_menu_item('pizza',pizza_3)

    # add burgur to the menu
    burger_1 = Burger('Nut burger',500,'Nuts',['burger bun','beef'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Naga burger',300,'Chicken',['onion','chili'])
    menu.add_menu_item('burger',burger_2)

    # add drinks to the menu
    coke = Drinks('Coke',50,True)
    menu.add_menu_item('drinks',coke)
    coffee = Drinks('Mocha',300,False)
    menu.add_menu_item('drinks',coffee)

    # show menu
    menu.show_menu()
    restaurant = Restaurant('happy_me restaurant',2000,menu)

    # add employees
    manager = Manager('Arkan mia',5,'arkan@gmail.com','dinajpur',5000,'january 5,2020','core')
    restaurant.add_employee('manager',manager)
    chef = Chef('Islam',6,'islam@gmail.com','islamnogor',3500,'september 23,2002','chef','everything')
    restaurant.add_employee('chef',chef)
    server = Server('Arku',7,'arku@gmail.com','arkan society',2000,'march 5,2002','server')
    restaurant.add_employee('server',server)

    # show employees
    restaurant.show_employee()

    # customer_1 placing an order
    customer_1 = Customer('Mario',7,'mario@gmail.com','banani',100000)
    order_1 = Order(customer_1,[pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)
    # customer_1 paying for order_1
    restaurant.receive_payment(order_1,2000,customer_1)
    print('revenue and balance after first cutomer: ', restaurant.revenue,restaurant.balance)

    # customer_2 placing an order
    customer_2 = Customer('Mariana',7,'mariana@gmail.com','banani',200000)
    order_2 = Order(customer_2,[pizza_2,burger_1,pizza_1,coke])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)
    # customer_2 paying for order_2
    restaurant.receive_payment(order_2,5000,customer_2)
    print('revenue and balance after 2nd customer: ',restaurant.revenue,restaurant.balance)

    # pay rent
    restaurant.pay_expense(restaurant.rent, 'rent')
    print('After rent: ',restaurant.revenue,restaurant.balance,restaurant.expense)

    restaurant.pay_salary(chef)
    print('After salary of chef: ', restaurant.revenue,restaurant.balance,restaurant.expense)

# call the main
if __name__ == '__main__':
    main()