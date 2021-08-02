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
def product():
    user_input = int(input('''
[0] Main Menu
[1] View Products
[2] Update Products
[3] List & Replace Product
[4] Delete Product
\nChoose Option: '''))
    if user_input == 0:
        main()
    elif user_input == 1:
        print('\nThis is the Drinks Menu: ', products_list)
    elif user_input == 2:
        print('\nThis is the Drinks Menu: ', products_list)
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