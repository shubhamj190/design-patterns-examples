# Solid design principles in python with example

# add Liskov substitutation principle principle

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
    def pay(self, order):
        pass


class CreditPaymentProcessor(PaymentProceser):

    def __init__(self, security_code):
        self.security_code=security_code

    def pay(self, order):
        print("processing credit payment type")
        print(f"verifying security_code: {self.security_code}")
        order.status = "paid"


class DebitPaymentProcessor(PaymentProceser):

    def __init__(self, security_code):
        self.security_code=security_code

    def pay(self, order):

        print("processing debit payment type")
        print(f"verifying security_code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProceser):
    def __init__(self, email):
        self.email=email

    def pay(self, order):

        print("processing paypal payment type")
        print(f"verifying security_code with email: {self.email}")
        order.status = "paid"

order = Order()
order.add_item("shoes", 2, 1000)
pay = PaypalPaymentProcessor("shubham.jadhav@ufaber.com")
pay.pay(order)
