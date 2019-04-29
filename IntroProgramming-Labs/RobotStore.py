class Product:
    
    def__init__(self, name, price, quantity):
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def inStock(self, count):
        return self.quantity >= count

    def totalCost(self, count):
        return count*self.price

    def decStock(self, count):
        self.quantity = self.quantity - count
        
products = [ Product("Ultrasonic range finder", 2.50, 4),
             Product("Servo motor", 14.99, 10),
             Product("Servo controller", 44.95, 5),
             Product("Microcontroller Board", 34.95, 7),
             Product("Laser range finder", 149.99, 2),
             Product("Lithium polymer battery", 8.99, 8)]


def printStock():
    print()
    print("Available Products")
    print("------------------")
    for i in range(0,len(productNames)):
        if productQuantities[i] > 0:
            print(str(i)+")",productNames[i], "$", productPrices[i])
    print()
def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()
        vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break
        prodId = int(vals[0])
        count = int(vals[1])
        if productQuantities[prodId] >= count:
            if cash >= productPrices[prodId]:
                productQuantities[prodId] -= count
                cash -= productPrices[prodId] * count
                print("You purchased", count, productNames[prodId]+".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", productNames[prodId])
main()
