import re


class GroceryStore():
    def __init__(self):
        self._total_value = 0
        self._item_count = 0

    def total_value(self):
        return self._total_value

    def add_item(self, name, quantity, total_price):
        self._total_value += total_price
        self._item_count += quantity

    def read_ros_file(self, filedata):
        for line in filedata.splitlines():
            if len(line.strip()) > 0:
                line = re.sub(r'\(.*\)', '', line)
                name, quantity, price = line.strip().split(',')
                self.add_item(name, int(quantity), int(price))

    def item_count(self):
        return self._item_count
