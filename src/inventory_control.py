class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.data = list()

    def add_new_order(self, customer, order, day):
        check = self.check_ingredient_availability(order)
        if check is False:
            return False
        else:
            self.data.append({
                "id": len(self.data),
                "customer": customer,
                "order": order,
                "day": day
            })

    def get_quantities_to_buy(self):
        buy_list = self.MINIMUM_INVENTORY.copy()
        for key in buy_list.keys():
            buy_list[key] = 0
        for order in self.data:
            buy_list[self.INGREDIENTS[order["order"]][0]] += 1
            buy_list[self.INGREDIENTS[order["order"]][1]] += 1
            if len(self.INGREDIENTS[order["order"]]) == 3:
                buy_list[self.INGREDIENTS[order["order"]][2]] += 1
        return buy_list

    def check_ingredient_availability(self, order):
        quantities = self.get_quantities_to_buy()
        for ing in self.INGREDIENTS[order]:
            if quantities[ing] >= self.MINIMUM_INVENTORY[ing]:
                return False
