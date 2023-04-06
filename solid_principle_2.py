# Solid design principles in python with example

# add open/closed principle

from abc import ABC, abstractmethod


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


class PaymentProceser(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass


class CreditPaymentProcessor(PaymentProceser):
    def pay(self, order, secutrity_code):
        print("processing credit payment type")
        print(f"verifying security_code: {secutrity_code}")
        order.status = "paid"


class DebitPaymentProcessor(PaymentProceser):
    def pay(self, order, secutrity_code):

        print("processing debit payment type")
        print(f"verifying security_code: {secutrity_code}")
        order.status = "paid"


order = Order()
order.add_item("shoes", 2, 1000)
pay = CreditPaymentProcessor()
pay.pay(order, "asfsadf4564")
