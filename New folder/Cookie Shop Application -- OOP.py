# Name: Van Bohn
# Assignment Number:7
# Date: 11/17/2018
# Section: 11:00-12:30
# Description: Program to teach me abnout classes and combine past knowlege of funcitons

import cookie

def main():

    # instatiates c1,c2,c3 as objects from the Cookie class
    c1 = cookie.Cookie("chocolate chip", 10, 4.50)
    c2 = cookie.Cookie("strawberry", 30, 3.00)
    c3 = cookie.Cookie("sugar", 15, 2.50)

    # creates an empty list
    clist = []
    
    #adds c1, c2, c3 to the empty clist
    clist.append(c1)
    clist.append(c2)
    clist.append(c3)

    def displayChoice():
    
        def printAllCookies(cList):
            for i in cList:
                example = cookie.Cookie.__str__(i)
                print(example)
                print()
                
        def changePrice(cList, cookieType, pRice):
            flag = 0 
            for i in cList:
                if i.get_cType() == cookieType:
                    flag = 1
                    i.set_price = pRice
                    break
            return flag

        def outputCookieInventory(cList, cookieType):
            for i in cList:
                flag1 = 0
                if i.get_cType() == cookieType:
                    flag1 = 1
                    break
            return i.get_inventory()

                


        # the following block of code is the menu
        print("Welcome to Best Cookies")
        print("===========================")
        print("a: Output information for all cookies")
        print("b: Set a new price for one cookie")
        print("c: Output inventory for a specific cookie")
        print("e: Exit the program \n")

        choice = 'zar'
        while choice != 'e':
            # the initial prompt for menu choice
            choice = input("Please enter your choice: ").lower()
            print("\n")
            #the following decision tree processees the choice
            choicelist = ['a','b','c','e']
                   
            if choice == 'a':
                printAllCookies(clist)

            elif choice == 'b':
                cookietype = input("What cookietype you want to change the price of?").lower()
                price = float(input("What do you want to change the cookie price to?"))
                flag = changePrice(clist, cookietype, price)
                if flag  == 0:
                    print("COOKIE TYPE NOT FOUND")       

            elif choice == 'c':
                cookietype = input("What cookie type do you want?")
                number = outputCookieInventory(clist, cookietype)
                print("The inventory for", cookietype, "is", number)

            elif choice == 'e':
                print("You just chose to exit the program")
            else:
                print("you just made an invalid input, you will be prompted again in a moment")
                


    displayChoice()
        

main()

