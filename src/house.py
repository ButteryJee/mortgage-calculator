class House:
    def __init__(self, price) -> None:
        self.price = price
    
    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price

    def print(self):
        print("House Price: ${}".format(self.price))