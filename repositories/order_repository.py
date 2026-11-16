from abc import ABC, abstractmethod
from typing import Optional, List

from RMS_2.models.order import Order


class OrderRepository(ABC):

    @abstractmethod
    def add_order(self, order : Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id : str) -> Optional[Order]:
        pass

    @abstractmethod
    def update_orders(self, order : Order) -> None:
        pass

    @abstractmethod
    def list_all_orders(self) -> List[Order]:
        pass
