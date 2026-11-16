from dataclasses import dataclass
from RMS_2.models.menu_items import MenuItem
from RMS_2.repositories.customer_repository import CustomerRepository
from RMS_2.repositories.menu_repository import MenuRepository
from RMS_2.utilitys.input_helps import RestuarentError
from RMS_2.models.customer import Customer

@dataclass
class MenuService:

    customer_repository : CustomerRepository
    menu_repository : MenuRepository

    def view_menu(self):
        for menu_item in self.menu_repository.list_all_items():
            print(f"item id {menu_item.item_id} | item name {menu_item.item_name} | category {menu_item.category} | "
                  f"price {menu_item.price} | available quantity {menu_item.quantity} ")

    def add_menu_items(self,item_id:str,item_name:str,category:str,price:int,quantity:int):

        if self.menu_repository.get_by_id(item_id=item_id) is not None:
            raise RestuarentError("This item id already taken")

        if quantity < 0:
            raise RestuarentError("quantity must be greate than 0")

        if price < 0:
            raise RestuarentError("price must be greate than 0")

        menu_item = MenuItem(item_id=item_id,item_name=item_name,category=category,price=price,quantity=quantity)
        self.menu_repository.add_menu_item(menu_item)

        return menu_item

    def update_menu_items(self,item_id:str,item_name:str,category:str,price:int,quantity:int):

        if self.menu_repository.get_by_id(item_id=item_id) is None:

            raise RestuarentError("This item id already taken")

        if quantity < 0:
            raise RestuarentError("quantity must be greate than 0")

        if price < 0:
            raise RestuarentError("price must be greate than 0")

        menu_item = MenuItem(item_id=item_id,item_name=item_name,category=category,price=price,quantity=quantity)

        self.menu_repository.update_item(menu_item)

    def remove_menu_item(self,item_id : str):

        item = self.menu_repository.get_by_id(item_id)

        if self.menu_repository.get_by_id(item_id) is None:
            raise RestuarentError("Item is does not exist")

        self.menu_repository.remove_menu_items(item)

    def add_customer(self,cust_id:str,cust_name:str,cust_no:int):

        if self.customer_repository.get_by_id(cust_id=cust_id) is not None:
            raise RestuarentError("This customer id is already taken")

        customer = Customer(cust_id=cust_id,cust_name=cust_name,cust_no=cust_no)

        self.customer_repository.add_customer(customer)

    def view_customers(self):

        for customer in self.customer_repository.list_all_customer():
            print(f"customer name {customer.cust_name} | customer id {customer.cust_id} | customer no {customer.cust_no}")







