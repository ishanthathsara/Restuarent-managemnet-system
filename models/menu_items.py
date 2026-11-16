from dataclasses import dataclass

from RMS_2.utilitys.input_helps import RestuarentError


# from utils.input_helpers import Re

@dataclass
class MenuItem:

    item_id : str
    item_name : str
    category : str
    price : int
    quantity : int

    def is_available(self) -> bool:
        return self.quantity > 0

    def reduce_quantity(self,amount):

        if amount > self.quantity:
            raise RestuarentError(f"amount must be less than {self.quantity}")

        if amount < self.quantity:
            raise RestuarentError(f"amount must be greater than {self.quantity}")

        else:
            self.quantity -= amount

    def add_quantity(self,amount):

        if amount < 0:
            raise RestuarentError(f"amount must be greater than 0 ")

        else:
            self.quantity += amount
















