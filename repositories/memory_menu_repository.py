from typing import List, Optional, Dict

from RMS_2.models.menu_items import MenuItem
from RMS_2.repositories.menu_repository import MenuRepository
from RMS_2.utilitys.input_helps import RestuarentError


class InMemoryMenuRepository(MenuRepository):

    def __init__(self):
        self.__menu_dict : Dict[str,MenuItem] = {}

    def add_menu_item(self, item: MenuItem) -> None:
        self.__menu_dict[item.item_id] = item

    def get_by_id(self, item_id: str) -> Optional[MenuItem]:

        return self.__menu_dict.get(item_id)

    def update_item(self, item: MenuItem) -> None:

        if self.__menu_dict.get(item.item_id) is None:
            raise RestuarentError("Menu item does not exist")

        self.__menu_dict[item.item_id] = item

    def list_all_items(self) -> List[MenuItem]:

        return list(self.__menu_dict.values())

    def remove_menu_items(self, item : MenuItem) -> None:

        del item


