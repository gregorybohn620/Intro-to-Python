class Dress:

    #initializes the dress_id, dress_type, size, price
    def __init__(self, dress_id, dress_type, designer, size, price):
        self.__dress_id = dress_id
        self.__dress_type = dress_type
        self.__designer = designer
        self.__size = size
        self.__price = price

    
    
    #defines all of methods to change all of the already set functions
    def set_dress_id(self, dress_id):
        self.__dress_id = dress_id

    def set_dress_type(self, dress_type):
        self.__dress_type = dress_type

    def set_designer(self, designer):
        self.__designer = designer
        
    def set_size(self, size):
        self.__size = size

    def set_price(self, price):
        self.__price = price

    #defines all of the methods to return values
    def get_dress_id(self):
        return self.__dress_id

    def get_dress_type(self):
        return self.__dress_type

    def get_designer(self):
        return self.__designer

    def get_size(self):
        return self.__size


    def get_price(self):
        return self.__price

    #defines the __str__ the method

    def __str__(self):
        stringprice = str(self.__price)
        return 'Dress ID: ' + self.__dress_id + \
               '\nDress type: ' + self.__dress_type + \
               '\nDesigner: ' + self.__designer + \
               '\nSize: ' + self.__size + \
               '\nPrice: ' + stringprice

#creates the subclass PreOwnedDress
class PreOwnedDress(Dress):

    def __init__(self, dress_id, dress_type, designer, size, price, year):
        Dress.__init__(self, dress_id, dress_type, designer, size, price)
        self.__year = year

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def __str__(self):
        yr = str(self.__year)
        return Dress.__str__(self) + "\nYear: " + yr
