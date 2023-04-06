# Solid design principles in python with example

# add singleton principle


class Order:

    items = []
    quntaties = []
    prices = []
    status = "Open"

    def add_item(self, name: str, quantity: int, price: int):
        self.items.append(name)
        self.quntaties.append(quantity)
        self.prices.append(price)

    def total_price(self):

        for i in range(len(self.prices)):
            total = self.quntaties[i] * self.prices[i]
        return total


class PaymentProceser:
    def pay_debit(self, order, secutrity_code):

        print("processing debit payment type")
        print(f"verifying security_code: {secutrity_code}")
        order.status = "paid"

    def pay_credit(self, order, secutrity_code):
        print("processing credit payment type")
        print(f"verifying security_code: {secutrity_code}")
        order.status = "paid"


order = Order()
order.add_item("shoes", 2, 1000)
pay=PaymentProceser()
pay.pay_credit(order, "asfsadf4564")
