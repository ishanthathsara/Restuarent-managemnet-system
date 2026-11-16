from dataclasses import dataclass
from RMS_2.models.order_status import OrderStatus
from RMS_2.models.order import OrderItems, Order
from RMS_2.repositories.customer_repository import CustomerRepository
from RMS_2.repositories.menu_repository import MenuRepository
from RMS_2.repositories.order_repository import OrderRepository
from RMS_2.utilitys.input_helps import RestuarentError


@dataclass
class OrderService:

    order_repository : OrderRepository
    customer_repository : CustomerRepository
    menu_repository : MenuRepository

    def add_order_item_to_order(self,item_id,quantity,order_id):

        item = self.menu_repository.get_by_id(item_id)
        order = self.order_repository.get_by_id(order_id)

        if self.menu_repository.get_by_id(item_id) is None:
            raise RestuarentError("Order is does not exist")

        if self.order_repository.get_by_id(order_id) is None:
            raise RestuarentError("Order is does not exist")

        order_item = OrderItems(item_id=item_id,item_name=item.item_name,user_quantity=quantity,unit_price=item.price)

        order.add_orderitem_to_order(order_item)

    def create_order(self,order_id,customer_id):

        customer = self.customer_repository.get_by_id(customer_id)

        if self.order_repository.get_by_id(order_id) is not None:
            raise RestuarentError("This order id is already taken")

        if self.customer_repository.get_by_id(customer_id) is None:
            raise RestuarentError("Customer is does not exist")

        order = Order(order_id=order_id,customer_id=customer_id,customer_name=customer.cust_name)

        self.order_repository.add_order(order)

    def list_orders(self):

        for order in self.order_repository.list_all_orders():
            print(f"order id {order.order_id} | customer is {order.customer_name} ")
            print("------------------------------------------------------------------")
            for order_item in order.order_list:
                print(f"{order_item.item_name}__________x{order_item.user_quantity}__________{order_item.sub_total_cal()}")

    def view_order(self,order_id):

        if self.order_repository.get_by_id(order_id) is None:
            raise RestuarentError("Order is does not exist")

        order = self.order_repository.get_by_id(order_id)

        print(f"order id {order.order_id} | customer is {order.customer_name} ")
        print("------------------------------------------------------------------")
        for order_item in order.order_list:
            print(f"{order_item.item_name}__________x{order_item.user_quantity}__________{order_item.sub_total_cal()}")

    def update_order_status(self,order_id,status_no):

        order = self.order_repository.get_by_id(order_id)

        if self.order_repository.get_by_id(order_id) is None:
            raise RestuarentError("Order does not exist")

        match status_no:
            case 1:
                order.status = OrderStatus.PREPARING

            case 2:
                order.status = OrderStatus.READY

            case 3:
                order.status = OrderStatus.COMPLETED

            case 4:
                order.status = OrderStatus.CANCELLED

            case _:
                raise RestuarentError("Enter valid choice")













        