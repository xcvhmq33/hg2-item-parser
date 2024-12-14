from pathlib import Path

from tqdm import tqdm

from .data_loader import DataLoader
from .enums import ItemCategory, ItemData
from .exceptions import ItemNotFoundError
from .info_parser import InfoParser
from .models import Item, ItemInfo, ItemProperties, ItemSkill
from .property_parser import PropertyParser
from .skill_parser import SkillParser
from .tsvreader import TSVReader


class ItemParser:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.main_data = self._load_main_data()

    def parse_and_write_items_from_to(
        self,
        first_item_id: int,
        last_item_id: int,
        output: Path,
        *,
        progressbar: bool = False,
    ) -> None:
        output.parent.mkdir(parents=True, exist_ok=True)
        items = self.parse_items_from_to(
            first_item_id, last_item_id, progressbar=progressbar
        )
        with output.open("w", encoding="utf-8") as file:
            for item in items:
                file.write(f"{item}\n\n")

    def parse_and_write_item(self, item_id: int, output: Path) -> None:
        output.parent.mkdir(parents=True, exist_ok=True)
        item = self.parse_item(item_id)
        with output.open("w", encoding="utf-8") as file:
            file.write(str(item))

    def parse_items_from_to(
        self, first_item_id: int, last_item_id: int, *, progressbar: bool = False
    ) -> list[Item]:
        items = []
        for item_id in tqdm(
            range(first_item_id, last_item_id + 1),
            desc="Parsing...",
            disable=(not progressbar),
        ):
            try:
                item = self.parse_item(item_id)
            except ItemNotFoundError:
                continue
            items.append(item)

        return items

    def parse_item(self, item_id: int) -> Item:
        info = self.parse_item_info(item_id)
        property = self.parse_item_property(item_id)
        skills = self.parse_item_skills(item_id)

        item = Item(
            info,
            property,
            skills,
        )

        return item

    def parse_item_info(self, item_id: int) -> ItemInfo:
        item_main_data = self.search_item_main_data(item_id)
        item_info = InfoParser.parse_info(item_main_data)

        return item_info

    def parse_item_property(self, item_id: int) -> ItemProperties:
        item_main_data = self.search_item_main_data(item_id)
        item_property = PropertyParser.parse_properties(item_main_data)

        return item_property

    def parse_item_skills(self, item_id: int) -> list[ItemSkill]:
        item_main_data = self.search_item_main_data(item_id)
        skill_parser = SkillParser(self.data_dir)
        item_skills = skill_parser.parse_skills(item_main_data)

        return item_skills

    def search_item_main_data(self, item_id: int) -> dict[str, str]:
        for item_category in ItemCategory:
            item_main_data = self.get_item_main_data(item_id, item_category)

            if item_main_data is not None:
                return item_main_data

        msg = f"Item not found: {item_id}"
        raise ItemNotFoundError(msg, item_id=item_id)

    def get_item_main_data(
        self, item_id: int | str, item_category: ItemCategory
    ) -> dict[str, str] | None:
        category_main_data = self.main_data[item_category]
        item_main_data = category_main_data.get_row_by_column_value(
            "DisplayNumber", item_id
        )
        if item_main_data is not None:
            item_main_data["Category"] = item_category.value
            return item_main_data

        return None

    def _load_main_data(self) -> dict[ItemCategory, TSVReader]:
        data = DataLoader.load_data(
            self.data_dir,
            list(ItemCategory),
            (f"{data.value}.tsv" for data in ItemData),
        )

        return data  # type: ignore
