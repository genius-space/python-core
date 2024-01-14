from abc import ABC, abstractclassmethod


class DiscountCalculator(ABC):

    @abstractclassmethod
    def get_discounted_product():
        pass


class DiscountCalculatorShirt(DiscountCalculator):

    def __init__(self, cost) -> None:
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.10)
    

class DiscountCalculatorTShirt(DiscountCalculator):

    def __init__(self, cost) -> None:
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.15)
    

class DiscountCalculatorPant(DiscountCalculator):

    def __init__(self, cost) -> None:
        self.cost = cost

    def get_discounted_product(self):
        return self.cost - (self.cost * 0.20)
    

ds_shirt = DiscountCalculatorShirt(100)
print(ds_shirt.get_discounted_product())
ds_tshirt = DiscountCalculatorTShirt(1000)
print(ds_tshirt.get_discounted_product())
ds_pant = DiscountCalculatorPant(500)
print(ds_pant.get_discounted_product())