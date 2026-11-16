from typing import List, Optional, Dict

from RMS_2.models.customer import Customer
from RMS_2.repositories.customer_repository import CustomerRepository
from RMS_2.utilitys.input_helps import RestuarentError


class InMemoryCustomerRepository(CustomerRepository):

    def __init__(self):
        self.__customers : Dict[str,Customer] = {}

    def add_customer(self, customer: Customer) -> None:

        self.__customers[customer.cust_id] = customer

    def get_by_id(self, cust_id: str) -> Optional[Customer]:

        return self.__customers.get(cust_id)

    def update_customer(self, customer: Customer) -> None:

        if self.__customers.get(customer.cust_id) is None:
            raise RestuarentError("Customer is does not exist")

        self.__customers[customer.cust_id] = customer

    def list_all_customer(self) -> List[Customer]:

        return list(self.__customers.values())