products_list = ["Water", "Coke", "Pepsi", "Mango", "Sprite"]


app_option = int(input(''' Input your option
                    Press 0 -> To Exit App 
                    Press 1 -> To Enter App
                    Enter your option here: '''))
if app_option == 0:
    print("Goodbye.")
    exit()

elif app_option == 1:
    user_input = int(input(''' Your menu options below:
    0: Main Menu
    1: View products menu
    2: Add a new product 
    3: Update products menu
    4: Delete a product
    \tEnter Option Here: '''))

if user_input == 0:

    pypy