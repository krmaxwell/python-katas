class ROS:
    def __init__(self):
        self.items = []
        self.total_income = 0
        self.categories = {}

    def add_item(self, name, _, price):
        # quantity is unused for now
        self.items.append((name, _, price))
        self.total_income += price

    def add_category(self, item, category):
        self.categories[item] = category

    def process_ros_file(self, data):
        for item in data.split("\n"):
            if item.strip():  # if item is not empty
                # items can have multiple commas so we just look for the last item in the list
                self.add_item(item, 0, int(item.split(",")[-1]))
