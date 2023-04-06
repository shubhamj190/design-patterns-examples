# Solid design principles in python with example

class Order:

    items=[]
    quntaties=[]
    prices=[]
    statius="Open"

    def add_item(self, name: str, quantity: int, price: int):
        self.items.append(name)
        self.quntaties.append(quantity)
        self.prices.append(price)

    def total_price(self):

        for i in range(len(self.prices)):
            total=self.quntaties[i]*self.prices[i]
        return total
    
    def pay(self, payment_type, secutrity_code):

        if payment_type == "debit":
            print("processing debit payment type")
            print(f"verifying security_code: {secutrity_code}")
        elif payment_type == "credit":
            print("processing credit payment type")
            print(f"verifying security_code: {secutrity_code}")
        else:
            raise Exception("Unknowen paymenrt type")
        


order=Order()
order.add_item("shoes",2,1000)
print(order.total_price())
order.pay("debit",'4548sdf')
        




