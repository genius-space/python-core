class BaseInterface:
    """Base class"""
    def __init__(self) -> None:
        pass

    def get_attrs(self) -> None:
        pass
    
    def print_model(self) -> None:
        pass

    def count_of_price(self) -> None:
        pass

    def call_to_support(self) -> None:
        pass


class SiteInterface(BaseInterface):
    """Interface of our site"""

    def __init__(self, number, model, price) -> None:
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self):
        print(f"Model of site: {self.model}")

    def count_of_price(self):
        print(f"Count of site price: {self.price ** 2}")

    def call_to_support(self) -> None:
        print(f"Number of support is {self.number}")
        print(f"Your can call from 8am to 19pm")


class AppInterface(BaseInterface):
    """Interface of our application"""

    def __init__(self, number, model, price) -> None:
        super().__init__()
        self.number = number
        self.model = model
        self.price = price

    def print_model(self):
        print(f"Model of application: {self.model}")

    def count_of_price(self):
        print(f"Count of application price: {self.price ** 2}")

    def call_to_support(self) -> None:
        print(f"Number of support is {self.number}")
        print(f"Your can call from 8am to 19pm")


site_user = SiteInterface(12345, "shop", 1000)
app_user = AppInterface(322324, "android", 5000)

for user in (site_user, app_user):
    user.print_model()
    user.count_of_price()
    user.call_to_support()
    print("---------------")


