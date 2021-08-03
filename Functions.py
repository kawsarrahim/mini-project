#Functions
import csv

def read_csv_file(file_name, csv_to_read):
    with open(file_name, 'r') as csv_file:
        csv_to_read = csv.DictReader(csv_file)
        csv_list = []
        for row in csv_to_read:
            csv_list.append(row)
        return csv_list
def save_list(file_name, list_name):
    with open(file_name, "w", newline='') as updated:
        if list_name:
            writer = csv.DictWriter(updated, fieldnames=list_name[0].keys())
            writer.writeheader()
            writer.writerows(list_name)
def print_csv_file(file_name, csv_file):
    with open(file_name, 'r') as csv_print:
        csv_file = csv.DictReader(csv_print)
        for row in csv_file:
            print(dict(row))
def append_dict(file_name, dict_of_elem, field_names):
    with open(file_name, 'a+', newline='') as write_obj:
        dict_writer = csv.DictWriter(write_obj, fieldnames=field_names)
        dict_writer.writerow(dict_of_elem)
def update_dict(chosen_item):
    for key, value in chosen_item.items():
        chosen_value = input(
            f'\nThe {key} Value is {value}. Enter New Value For {key}: ')
        if chosen_value == '':
            chosen_item[key] = value
            print('\nNothing has been changed')
        else:
            chosen_item[key] = chosen_value
def delete_index(list_name, deleted_input):
    del list_name[deleted_input]
def enumerate_orders(order_goes_here):
    for key, value in enumerate(order_goes_here):
        print(key, value)
        
def whitespace():
    print('\n')