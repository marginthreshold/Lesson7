
def view_data(data, title):
    print(f'{title} = {data}')

def get_contact_info():
    return input()

def ask_to_fill(text):
    print(f"\nВведите {text} :")

def print_list(printed_list):
    for i in printed_list:
        print(",".join(map(str,i)))