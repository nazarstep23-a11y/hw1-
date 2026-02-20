class Product:
    def __init__(self, name, price, available=True):
        self.name = name
        self.price = price
        self.available = available


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product.available:
            self.products.append(product)
            print(product.name, "added to cart")
        else:
            print(product.name, "is not available")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(product.name, "removed from cart")
        else:
            print("Product not found in cart")

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
        if len(self.products) == 0:
            print("Cart is empty")
        else:
            print("Products in cart:")
            for product in self.products:
                print(product.name, "-", product.price, "UAH")
            print("Total price:", self.total_price(), "UAH")


p1 = Product("Phone", 10000)
p2 = Product("Headphones", 2000)
p3 = Product("Laptop", 30000, available=False)

cart = Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.show_cart()

cart.remove_product(p2)
cart.show_cart()