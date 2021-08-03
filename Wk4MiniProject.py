from Functions import read_csv_file, save_list, append_dict, update_dict, delete_index, enumerate_orders, whitespace
import csv
from pprint import pprint
order_list = []
product_list = []
courier_list = []
order_status = ['Preparing...', 'Quality Review',
                'Driver Enroute :)', 'Delivered!']
order_list = read_csv_file('Order_list.csv', order_list)
product_list = read_csv_file('Product_list.csv', product_list)
courier_list = read_csv_file('Courier_list.csv', courier_list)
def main():
    print("\n\tMain Menu")
    print("""
        [0] - Save/Exit
        [1] - Product Options
        [2] - Courier Options
        [3] - Order Options""")
    option = int(input("""\n\tEnter Your Option: """))
    if option == 0:
        save_list('Order_list.csv', order_list)
        save_list('Product_list.csv', product_list)
        save_list('Courier_list.csv', courier_list)
        print('\n\tGoodbye')
        exit()
    elif option == 1:
        product()
    elif option == 2:
        courier()
    elif option == 3:
        order()
    else:
        print('USER: Enter a valid input')
        main()
def product():
    print('\n\tProduct List Options')
    print('''
        [0]: Main Menu
        [1]: View products menu
        [2]: Add a new product
        [3]: Update Products
        [4]: Delete Product''')
    user_input = int(input('\n\tSelect from the options above: '))
    if user_input == 0:
        main()
    elif user_input == 1:
        print("\n\tHere's The Product List\n\t")
        pprint(product_list)
        product()
    elif user_input == 2:
        print('\n\tHere Ts The Product List\n\t')
        pprint(product_list)
        new_product = input('\n\tAdd New Product : ')
        new_price = float(input('\n\tEnter New Price: '))
        new_dict = {}
        new_dict['Name'] = new_product
        new_dict['Price'] = new_price
        headers = ['Name', 'Price']
        append_dict('Product_list.csv', new_dict, headers)
        print("\n\tProduct Added:", new_dict)
        product()
    elif user_input == 3:  # Check is \n still needs to be here
        print('\n\tThe Product List: \n\t')
        enumerate_orders(product_list)
        number_input = int(
            input('\n\tChoose Number To Replace Product: '))
        new_variable = product_list[number_input]
        update_dict(new_variable)
        print("\n\tUpdated Product List:\t\n")
        pprint(product_list)
        product()
    elif user_input == 4:
        print('\n\tDelete A Product\n\t')
        enumerate_orders(product_list)
        deleted_input = int(
            input('\n\tSelect the product (number) to delete: '))
        whitespace()
        delete_index(product_list, deleted_input)
        print("\n\tProduct Has Been Deleted\n\t")
        enumerate_orders(product_list)
        product()
    else:
        print('Invalid Option')
        product()
def courier():
    print('\n\tCourier Menu')
    print('''
        [0] Main Menu
        [1] View Couriers
        [2] Create New Couriers
        [3] Update Couriers
        [4] Delete Couriers''')
    user_input = int(input('\n\tEnter Option: '))
    if user_input == 0:
        main()
    elif user_input == 1:
        print("\n\tCouriers List\n\t")
        pprint(courier_list)
        courier()
    elif user_input == 2:
        print("\n\tCouriers List\n\t")
        pprint(courier_list)
        courier_name = input('\n\tAdd Courier: ')
        courier_phone = int(input('\n\tEnter A Phone Number: '))
        new_dict = {}
        new_dict['Name'] = courier_name
        new_dict['Phone Number'] = courier_phone
        headers = ['Name', 'Phone Number']
        append_dict('Courier_list.csv', new_dict, headers)
        print("\n\tNew Courier Added!\n\t")
        pprint(new_dict)
        courier()
    elif user_input == 3:  # Check is\n still needs to be here
        print('\n\tThe Courier List: ', '\n')
        enumerate_orders(courier_list)
        number_input = int(
            input('\n\tChoose A Courier (number) To Replace: '))
        new_variable = courier_list[number_input]
        update_dict(new_variable)
        print("\n\tCourier's List Updated:\n\t")
        pprint(courier_list)
        courier()
    elif user_input == 4:
            print('\n\tDelete Courier')
            enumerate_orders(courier_list)
            deleted_input = int(
            input('\n\tChoose Courier to Delete: '))
            delete_index(courier_list, deleted_input)
            print("\n\tYou've deleted a Courier:\n\t")
            pprint(courier_list)
            courier()
    else:
        print('\n\tInvalid Option')
        courier()

def order():
    print('\n\tOrder Menu')
    print('''
        [0]: Main Menu
        [1]: View The Order List
        [2]: Add An Order
        [3]: Update Order Status
        [4]: Update Existing Order
        [5]: Delete An Order''')
    user_input = int(input('\n\tEnter Option: '))
    if user_input == 0:
        main()
    elif user_input == 1:
        print("\n\tHere's The Order's List:")
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')
        order()
    elif user_input == 2:
        customer_name = input('\n\tEnter Customer Name : ')
        customer_address = input('\n\tEnter Customer Address: ')
        customer_phone_number = int(
            input('\n\tEnter Phone Number: \n\t'))
        enumerate_orders(product_list)
        product_choice = input(
            '\n\tWhich Product Do You Want Added To Your Order: ')
        enumerate_orders(courier_list)
        courier_choice = int(
            input('\n\tChoose A Courier To Deliver Your Order: '))
        new_dict = {}
        new_dict['Customer Name'] = customer_name
        new_dict['Customer Address'] = customer_address
        new_dict['Customer Phone'] = customer_phone_number
        new_dict['Courier'] = courier_choice
        new_dict['Status'] = order_status[0]
        new_dict['Items'] = product_choice
        headers = ['Customer Name', 'Customer Address',
                'Customer Phone', 'Courier', 'Status', 'Items']
        append_dict('Order_list.csv', new_dict, headers)
        print("\nYou've Added You're Order: ", new_dict)
        order()
    elif user_input == 3:
        print('\nThe Orders List: ', '\n')
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')
        order_input = int(
            input('\n\tOrder To Update: '))
        whitespace()
        enumerate_orders(order_status)
        status_input = int(input('\n\tStatus To Update: '))
        new_variable = order_list[order_input]
        new_variable['Status'] = order_status[status_input]
        print("\nNew updated product menu: ", new_variable)
        order()
    elif user_input == 4:
        print('\n\tUpdate Existing Order\n\t')
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')
        select_order = int(input('\n\tChoose Order: '))
        chosen_order = order_list[select_order]
        update_dict(chosen_order)
        print("\n\tOrder Updated\n\t")
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')
        order()
    elif user_input == 5:
        print('\n Delete An Order')
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')
        deleted_input = int(
            input('\nEnter Order To Delete: '))
        delete_index(order_list, deleted_input)
        print("You're Order No Longer Exists:\n\t")
        for key, value in enumerate(order_list):
            print(f'\n\tOrder Number - {key}{value}')
        order()
    else:
        print('Invalid Option')
        whitespace()
        order()
main()