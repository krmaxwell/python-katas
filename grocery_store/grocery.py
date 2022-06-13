class ROS:
    def __init__(self):
        self.items = []
        self.total_income = 0
        self.categories = {}
        self._category_sales = {}

    def add_item(self, name, _, price):
        # quantity is unused for now
        self.items.append((name, _, price))
        self.total_income += price
        for category in self.categories:
            if name in self.categories[category]:
                print("Found {} in {}".format(name, category))
                if category not in self._category_sales:
                    self._category_sales[category] = 0
                self._category_sales[category] += price

    def add_category(self, item, category):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(item)

    def process_ros_file(self, data):
        for item in data.split("\n"):
            if item.strip():  # if item is not empty
                # items can have multiple commas so we just look for the last item in the list
                self.add_item(item, 0, int(item.split(",")[-1]))

    def create_categories(self, data):
        for line in data.split("\n"):
            if line.strip():
                item = line.split(",")[0].strip()
                category = line.split(",")[1].strip()
                self.add_category(item, category)
                print("Added {} to {}".format(item, category))

    def get_category_sales(self, category):
        return self._category_sales.get(category, 0)
