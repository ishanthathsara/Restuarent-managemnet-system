from datetime import datetime
from dataclasses import dataclass, field
from typing import List
from RMS_2.models.order_status import OrderStatus

from RMS_2.models.menu_items import MenuItem

@dataclass
class OrderItems:

    item_id : str
    item_name : str
    user_quantity : int
    unit_price : int

    def sub_total_cal(self):
        return self.unit_price * self.user_quantity


@dataclass
class Order:

    order_id : str
    customer_id : str
    customer_name : str
    status : OrderStatus = field(default=OrderStatus.PENDING)
    create_at : datetime = field(default=datetime.now())
    order_list : List[OrderItems] = field(default_factory=list)

    def add_orderitem_to_order(self,item: OrderItems):

        self.order_list.append(item)

    def product_total(self):
        total = 0
        for item in self.order_list:
            total += item.sub_total_cal()

        return total

    def view_order_status(self):
        return self.status










