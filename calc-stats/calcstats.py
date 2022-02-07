class Stats:
    def __init__(self, data: list) -> None:
        self.data = data

    def min(self) -> int:
        return min(self.data)

    def max(self) -> int:
        return max(self.data)

    def length(self) -> int:
        return len(self.data)

    def mean(self) -> float:
        return sum(self.data) / len(self.data)
