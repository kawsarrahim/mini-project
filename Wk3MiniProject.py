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
    "customer name": "Rumaanah",
    "customer address": "2, worst Street, BUMTOWN, B1 1AD",
    "customer phone": "07366459874",
    "courier": [couriers_list[0]],
    "status": [order_status[1]]
}
]