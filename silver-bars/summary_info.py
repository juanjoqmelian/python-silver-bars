class SummaryInfo:

    def __init__(self, *args) -> None:
        self.items = []
        for arg in args:
            self.items.append(str(arg))

    def __repr__(self) -> str:
        separator = "\n"
        return separator.join(self.items)

    def __str__(self) -> str:
        separator = "\n"
        return separator.join(self.items)

    def __eq__(self, other: object) -> bool:
        if type(other) is type(self):
            return self.items == other.items
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.items)

