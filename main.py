from RMS_2.utilitys.input_helps import get_int_input,get_float_input,get_non_empty_str,RestuarentError
from RMS_2.services.menu_service import MenuService
from RMS_2.repositories.memory_menu_repository import InMemoryMenuRepository
from RMS_2.repositories.memory_customer_repository import InMemoryCustomerRepository
from RMS_2.repositories.memory_order_repository import InMemoryOrderRepository
from RMS_2.services.order_service import OrderService

menu_repository = InMemoryMenuRepository()
customer_repository = InMemoryCustomerRepository()
order_repository = InMemoryOrderRepository()

menuservice = MenuService(customer_repository=customer_repository,menu_repository=menu_repository)
orderservice = OrderService(order_repository=order_repository,customer_repository=customer_repository,menu_repository=menu_repository)

def show_main_menu():

    print("----- RESTAURANT MANAGEMENT SYSTEM -----")
    print("""1. View menu
2. Add menu item
3. Update menu item
4. Remove menu item
5. Create order
6. View order
7. List orders
8. Update order status
9. Add customer
10. View all customers
0. Exit""")

def view_menu():

    print("========== MENU ==========")
    menuservice.view_menu()

def add_menu_items():
    print("========== ADD MENU ITEMS ==========")

    item_id = get_non_empty_str("Enter item id : ")
    item_name = get_non_empty_str("Enter item name : ")
    category = get_non_empty_str("Enter category name : ")
    price = get_float_input("Enter unit price : ")
    quantity = get_int_input("Enter quantity of item : ")

    try:
        menuservice.add_menu_items(item_id=item_id,item_name=item_name,category=category,price=price,quantity=quantity)
        print("Item added successfully")
    except RestuarentError as e:
        print(f"Error : {str(e)}")

def update_menu_item():
    print("========== UPDATE MENU ITEMS ==========")

    item_id = get_non_empty_str("Enter item id : ")
    item_name = get_non_empty_str("Enter item name : ")
    category = get_non_empty_str("Enter category name : ")
    price = get_float_input("Enter unit price : ")
    quantity = get_int_input("Enter quantity of item : ")

    try:
        menuservice.update_menu_items(item_id=item_id,item_name=item_name,category=category,price=price,quantity=quantity)
        print("Item updated successfully")
    except RestuarentError as e:
        print(f"Error : {str(e)}")

def remove_menu_items():
    print("========== REMOVE MENU ITEMS ==========")
    item_id = get_non_empty_str("Enter item id : ")

    try:
        menuservice.remove_menu_item(item_id)
        print("Item removed successfully")
    except RestuarentError as e:
        print(f"Error : {e} ")

def create_order():
    new_order_id = get_non_empty_str("Enter order id : ")
    customer_id = get_non_empty_str("Enter customer id : ")

    try:
        orderservice.create_order(order_id=new_order_id,customer_id=customer_id)
        print("New order created successfully")

        while True:

            exit_order = False

            view_menu()
            item_id = get_non_empty_str("Enter item id : ")
            quantity = get_int_input("Enter quantity here : ", minimum=1)

            orderservice.add_order_item_to_order(item_id=item_id,quantity=quantity,order_id=new_order_id)
            print("Item added to order successfully")

            user_exit = get_int_input("Press 0 to exit | 1 to buy again : ",minimum=0,maximum=1)

            if user_exit == 0:
                exit_order = True
                break

        if exit_order == True:
            return

    except RestuarentError as e:
        print(f"Error : {str(e)}")

def add_customer():
    cust_id = get_non_empty_str("Enter customer id : ")
    cust_name = get_non_empty_str("Enter customer name : ")
    cust_no = get_int_input("Enter customer phone number : ")
    try:
        menuservice.add_customer(cust_id=cust_id,cust_name=cust_name,cust_no=cust_no)
        print("New customer added successfully")

    except RestuarentError as e:
        print(f"Error : {e}")

def view_customers():

    menuservice.view_customers()

def view_order():

    order_id = get_non_empty_str("Enter order id here : ")

    try:
        orderservice.view_order(order_id)
    except RestuarentError as e:
        print(f"Error : {str(e)}")

def update_order_status():

    user_order_id = get_non_empty_str("Enter order id here : ")

    print("""1. PREPARING
2. READY
3. COMPLETED
4. CANCELLED""")

    user_input = get_int_input("Enter your status choice : ", minimum=1,maximum=4)

    try:
        orderservice.update_order_status(order_id=user_order_id,status_no=user_input)

    except RestuarentError as e:
        print(f"Error : {str(e)}")


while True:

    show_main_menu()

    user_choice = get_int_input("Enter your choice here : ",minimum=0,maximum=10)

    match user_choice:
        case 1:
            view_menu()

        case 2:
            add_menu_items()

        case 3:
            update_menu_item()

        case 4:
            remove_menu_items()

        case 5:
            create_order()

        case 6:
            view_order()

        case 7:
            orderservice.list_orders()

        case 8:
            update_order_status()

        case 9:
            add_customer()

        case 10:
            view_customers()

        case 0:
            break

        case _:
            print("invalid answer. try again!")






