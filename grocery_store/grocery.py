class ROS:
    def __init__(self):
        self.items = []
        self.total_income = 0
        self.categories = {}
        self._category_sales = {}

    def add_item(self, name, _, price):
        name = name.strip()
        # quantity is unused for now
        self.items.append((name, _, price))
        self.total_income += price
        for category in self.categories:
            for item in self.categories[category]:
                if item in name:
                    self._category_sales[category] = self._category_sales.get(category, 0) + price

    def add_category(self, item, category):
        if category not in self.categories:
            self.categories[category] = []
        self.categories[category].append(item)

    def process_ros_file(self, data):
        for item in data.split("\n"):
            if item.strip():  # if item is not empty
                name = item.split(",")[-3].strip()
                # items can have multiple commas so we just look for the last item in the list
                price = int(item.split(",")[-1].strip())
                name = item.strip().split(",")[0]
                self.add_item(name, 0, price)

    def create_categories(self, data):
        for line in data.split("\n"):
            if line.strip():
                item = line.split(",")[0].strip()
                category = line.split(",")[1].strip()
                self.add_category(item, category)

    def get_category_sales(self, category):
        return self._category_sales.get(category, 0)

    def similarity(self, other_ros):
        """
        Returns a similarity score between two ROS objects.
        """
        all_items = set(self.items) | set(other_ros.items)
        both_items = set(self.items) & set(other_ros.items)
        return len(both_items) / len(all_items)
