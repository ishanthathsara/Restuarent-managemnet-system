from abc import ABC, abstractmethod
from typing import Optional, List

from RMS_2.models.customer import Customer

class CustomerRepository(ABC):

    @abstractmethod
    def add_customer(self,customer : Customer) -> None:
        pass

    @abstractmethod
    def get_by_id(self,cust_id : str) -> Optional[Customer]:
        pass

    @abstractmethod
    def update_customer(self, customer : Customer) -> None:
        pass

    @abstractmethod
    def list_all_customer(self) -> List[Customer]:
        pass
