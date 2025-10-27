class Inventory:
    def __init__(self, id: int, item: str) -> None:
        self.id = id
        self.item = item

    def get_info(self) -> str:
        return f"Это инвентарь. Содержимое инвентаря: {self.item}."