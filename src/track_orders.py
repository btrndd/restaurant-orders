class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({
            "id": self.__len__(),
            "customer": customer,
            "order": order,
            "day": day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        orders_per_customer = self.orders_per_customer(customer)
        return max(orders_per_customer, key=orders_per_customer.get)

    def get_never_ordered_per_customer(self, customer):
        orders_per_customer = self.orders_per_customer(customer)
        never_ordered = set()
        for order in orders_per_customer.keys():
            if orders_per_customer[order] == 0:
                never_ordered.add(order)
        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        days_per_customer = self.days_per_customer(customer)
        never_visited = set()
        for day in days_per_customer.keys():
            if days_per_customer[day] == 0:
                never_visited.add(day)
        return never_visited

    def get_busiest_day(self):
        days = self.total_per_days()
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = self.total_per_days()
        return min(days, key=days.get)

    def orders_per_customer(self, customer):
        orders_per_customer = {}
        for order in self.orders:
            if order["order"] not in orders_per_customer.keys():
                orders_per_customer[order["order"]] = 0
            if order["customer"] == customer:
                orders_per_customer[order["order"]] += 1
        return orders_per_customer

    def days_per_customer(self, customer):
        days_per_customer = {}
        for order in self.orders:
            if order["day"] not in days_per_customer.keys():
                days_per_customer[order["day"]] = 0
            if order["customer"] == customer:
                days_per_customer[order["day"]] += 1
        return days_per_customer

    def total_per_days(self):
        days = {}
        for order in self.orders:
            if order["day"] in days.keys():
                days[order["day"]] += 1
            else:
                days[order["day"]] = 0
                days[order["day"]] += 1
        return days
