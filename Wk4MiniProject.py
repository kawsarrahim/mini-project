from Functions import read_csv_file, save_list, append_dict, update_dict, delete_index, enumerate_orders, whitespace
from pprint import pprint
order_list = []
product_list = []
courier_list = []
order_status = ['Preparing', 'Quality checks',
                'Driver on the way', 'Delivered']
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
        number_input = float(
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
    