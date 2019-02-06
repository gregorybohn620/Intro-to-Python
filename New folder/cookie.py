# Name: Van Bohn
# Assignment Number:7
# Date: 11/17/2018
# Section: 11:00-12:30
# Description: the Cookie Class for homework 7
class Cookie:
    # the preceeding statement creates the Cookie class,
    # from which objects can be created
    def __init__(self,cType, inventory, price):
        self.__cType = str(cType)
        self.__inventory = int(inventory)
        self.__price = float(price)

    def set_cType(self, cType):
        self.cType = cType

    def set_inventory(self, inventory):
        self.__inventory = inventory
        if inventory <= 0:
            print("The inventory cannot be zero or negative!")

    def set_price(self,price):
        self.price = price
        if price <= 0:
            print("price must be posative")
        elif price > 4.50:
            print("price cannot exceed $4.50")

    # the above defined methods set the values for cType, inventory and price
    # the "__" makes each of the methods private

    def get_cType(self):
        return self.cType

    def get_inventory(self):
        return self.__inventory
        

    def get_price(self):
        return self.price

    # the above defined methods retuen the values for each of the varibales
    # defined in the beginning of the program

    def __str__(self):
        inv = str(self.__inventory)
        pri = str(self.__price)
        return "Cookie type is " + self.__cType + \
               "\nThe inventory is " + inv + \
               "\nThe price is " + pri


'''
def main():
# the code in main creates and uses objects bases on the class Cookie


    
main()
#calls main to run the program

'''
