import re


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

    def process_ros_file(self, data):
        for item in data.split("\n"):
            if item.strip():
                self.add_item(item, 0, int(item.split(",")[-1]))