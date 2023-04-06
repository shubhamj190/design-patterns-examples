# Solid design principles in python with example

# Dependency inversion

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


class SMSAuthorizer:
    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProceser(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class PaymentProcessorWithAuth(PaymentProceser):
    @abstractmethod
    def auth(self):
        pass


class CreditPaymentProcessor(PaymentProceser):
    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("processing credit payment type")
        print(f"verifying security_code: {self.security_code}")
        order.status = "paid"


class DebitPaymentProcessor(PaymentProceser):
    def __init__(self, security_code, authorizer: SMSAuthorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer:
            raise Exception("Not authorized")
        print("processing debit payment type")
        print(f"verifying security_code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProceser):
    def __init__(self, email, authorizer: SMSAuthorizer):
        self.email = email
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer:
            raise Exception("Not authorized")
        print("processing paypal payment type")
        print(f"verifying security_code with email: {self.email}")
        order.status = "paid"


order = Order()
order.add_item("shoes", 2, 1000)
authorizer=SMSAuthorizer()
pay = PaypalPaymentProcessor("shubham.jadhav@ufaber.com", authorizer)
pay.pay(order)
