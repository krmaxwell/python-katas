class ROS:
    def __init__(self):
        self.items = []
        self.total_income = 0
        self.categories = {}

    def add_item(self, name, quantity, price):
        self.items.append((name, quantity, price))
        self.total_income += price

    def add_category(self, item, category):
        self.categories[item] = category