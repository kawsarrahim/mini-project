products_list = []
with open('Product_list.txt') as load_p_file:
    for load_i in load_p_file:
        products_list.append(load_i.rstrip())
couriers_list = []
with open('Courier_list.txt') as load_c_file:
    for load_i in load_c_file:
        couriers_list.append(load_i.rstrip())
        
def main():
    option = int(input(''' Choose A Option:
[0] EXIT
[1] View Products
[2] View Couriers
Enter Your Option Here: '''))
    if option == 0:
        with open('Product_list.txt', 'w') as save_p_file:
            for save_i in products_list:
                save_p_file.write(save_i + '\n')
        with open('Courier_list.txt', 'w') as save_c_file:
            for save_w in couriers_list:
                save_c_file.write(save_w + '\n')
        print( "\n Goodbye!")
        print("")
        exit()
    elif option == 1:
        product()
    elif option == 2:
        courier()
    elif option == 3:
        order()
order_status = ['Preparing...', 'Courier Enroute', 'Delivered!']
order_list = [{
    "customer name": "Jane",
    "customer address": "103 Argyll Road, BIRMINGHAM, B91 2LB",
    "customer phone": "0798765432",
    "courier": [couriers_list[2]],
    "status": [order_status[0]]
},
    {
    "customer name": "Kawsar",
    "customer address": "2, Dummy Street, BRUMTOWN, B1 3AD",
    "customer phone": "07366459874",
    "courier": [couriers_list[0]],
    "status": [order_status[1]]
}
]
def listing_orders(order):
    for key, value in enumerate(order):
        print(f'\nOrder number: {key} - {value}')
def order():
    user_input = int(input('''
[0] Main Menu
[1] Print Order List
[2] Enter Order
[3] Update A Order Status
[4] Update Info within an order
[5] Delete a Courier for order
\nEnter Your Choice: '''))
    if user_input == 0:
        return main()
    elif user_input == 1:
        print(order_list)
    elif user_input == 2:
        entry = {}
        customer_name = input('Enter Customer Name: ')
        customer_address = input('Enter Customer Address: ')
        phone_number = int(
            input('Enter Customer Mobile Number: '))
        for key, value in enumerate(couriers_list):
            print(key, value)
        selected_courier = int(input('Choose Courier For Delivery: '))
        entry['Customer'] = customer_name
        entry['Customer address'] = customer_address
        entry['Customer phone'] = phone_number
        entry['courier'] = selected_courier
        entry['Status'] = order_status[0]
        order_list.append(entry)
    elif user_input == 3:
        listing_orders(order_list)
        order_index = int(input('\nChoose Order to Adjust:  '))
        print('')
        for key, value in enumerate(order_status):
                print(key, value) 
        status_input = int(
            input('\nChoose an order status to update on the order list: '))
        order_update = order_list[order_index]
        order_update['status'] = order_status[status_input]
    elif user_input == 4:
        for key, value in enumerate(order_list):
            print(key, value)
        order_index = int(
            input("\nSelect Order to Update: "))
        chosen_order = order_list[order_index]
        for key, value in chosen_order.items():
            chosen_value = input(
                f'\n{key} Has value of {value}. Enter new value for {key}: ')
            if chosen_value == '':
                chosen_order[key] = value
                print('\nNothing Changed')
            else:
                chosen_order[key] = chosen_value
        print(chosen_order)
    elif user_input == 5:
        listing_orders(order_list)
        delete_order = int(
            input('\nChoose order to delete: '))
        del order_list[delete_order]
        print(order_list)
def product():
    user_input = int(input('''
[0]: Main Menu
[1]: View Products Menu
[2]: Update Products Menu
[3]: List & Replace a Product
[4]: Delete a Product
\nEnter Option: '''))
    if user_input == 0:
        main()
    elif user_input == 1:
        print('\nThis is the Products Menu: ', products_list)
    elif user_input == 2:
        print('\nThis is the Pr Menu: ', products_list)
        new_product = input('\nAdd new product to menu')
        products_list.append(new_product)
        print('\nNew Drink Added: ', products_list)
    elif user_input == 3:
        print('\nThe Drink List is: ', '\n')
        for key, value in enumerate(products_list):
            print(key, value)
        number_input = int(
            input('\nEnter your option to replace: '))
        new_product = input('\nEnter your new product choice: ')
        products_list[number_input] = new_product
        print("\nHere's the new updated products menu: ", products_list)
    elif user_input == 4:
        print('\nLets delete a product')
        for key, value in enumerate(products_list):
            print(key, value)
        deleted_input = int(
            input('\nSelect a product to delete: '))
        del products_list[deleted_input]
        print('\nThis is the new products menu: ', products_list)
def courier():
    user_input = int(input('''
[0] Main Menu
[1] View Couriers
[2] Create New Couriers
[3] Update Couriers
[4] Delete Couriers
\nEnter Option: '''))
    if user_input == 0:
            main()
    elif user_input == 1:
        print('\n The Courier List: ', couriers_list)
    elif user_input == 2:
        print('\nThe Courier List: ', couriers_list)
        new_courier = input('\nEnter New Courier: ')
        couriers_list.append(new_courier)
        print("\nSuccessfully added a new courier!", couriers_list)
    elif user_input == 3:
        print("\nCouriers List is: ")
        for value, index in enumerate(couriers_list):
            print(value, index)
        number_input = int(input(
        '\n Select Courier Option To Replace:  '))
        new_courier = input('\nAdd a New Name: ')
        couriers_list[number_input] = new_courier
        print("\nThis is the New Courier List: ", couriers_list)
    elif user_input == 4:
        print('\nDelete Courier')
        for key, value in enumerate(couriers_list):
            print(key, value)
        deleted_input = int(input(
            '\nEnter Courier Option to Remove: '))
        del couriers_list[deleted_input]
        print('\nThis is the New Courier List: ', couriers_list)