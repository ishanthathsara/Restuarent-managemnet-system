from abc import ABC,abstractmethod
from typing import Optional, List

from RMS_2.models.menu_items import MenuItem

class MenuRepository(ABC):

    @abstractmethod
    def add_menu_item(self,item : MenuItem ) -> None:
        pass

    @abstractmethod
    def get_by_id(self,item_id : str) -> Optional[MenuItem]:
        pass

    @abstractmethod
    def update_item(self, item : MenuItem) -> None:
        pass

    @abstractmethod
    def list_all_items(self) -> List[MenuItem]:
        pass

    @abstractmethod
    def remove_menu_items(self, item : MenuItem) -> None:
        pass

