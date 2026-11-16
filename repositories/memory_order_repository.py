from typing import List, Optional, Dict

from RMS_2.models.order import Order
from RMS_2.repositories.order_repository import OrderRepository
from RMS_2.utilitys.input_helps import RestuarentError


class InMemoryOrderRepository(OrderRepository):

    def __init__(self):
        self.__order_dict : Dict[str,Order] = {}

    def add_order(self, order: Order) -> None:
        self.__order_dict[order.order_id] = order

    def get_by_id(self, order_id: str) -> Optional[Order]:

        return self.__order_dict.get(order_id)

    def update_orders(self, order: Order) -> None:

        if self.__order_dict.get(order.order_id) is None:
            raise RestuarentError("Order id is does not exist")

        self.__order_dict[order.order_id] = order


    def list_all_orders(self) -> List[Order]:

        return list(self.__order_dict.values())