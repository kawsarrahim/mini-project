products_list = ["Water", "Coke", "Pepsi", "Mango", "Sprite"]

def main():
    app_option = int(input(''' 
        Input your option
        Press 0 -> To Exit App 
        Press 1 -> To Enter App
        Enter your option here: '''))
    if app_option == 0:
        print("\n Goodbye.")
        exit()
    elif app_option == 1:
        product()
def product():
    user_input = int(input('''
    Your menu options below:
    0: Main Menu
    1: View products menu
    2: Add a new product 
    3: Update products menu
    4: Delete a product
    \tEnter Option Here: '''))
    if user_input == 0:
        main()
    elif user_input == 1:
        print("\n The product list for this app: ", products_list)
    elif user_input == 2:
        print("\n The product list for this app: ", products_list)
        new_product = input("\n Enter New Product: ")
        products_list.append(new_product)
        print("\n Succesfully created a new product!")
        print(products_list)
    elif user_input == 3:
        for value, index in enumerate(products_list):
            print(value, index)
        product_index_name = int(
            input("\n Enter Product Index Value (Number) to UPDATE: "))
        new_product_name = input("\n Enter New Product Name: ")
        products_list[product_index_name] = new_product_name
        print(products_list)
    elif user_input == 4:
        print("\n", [list((i, products_list[i]))
            for i in range(len(products_list))])
        delete_product_index_value = int(
            input("\n Enter Product Index Value (Number) to DELETE: "))
        del products_list[delete_product_index_value]
        print("\n This is the updated Product List: ", products_list)
main()