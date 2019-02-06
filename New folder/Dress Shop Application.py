# Name: Van Bohn
# Assignment Number:8
# Date: 11/17/2018
# Section: 11:00-12:30
# Description: the program imports the dress program which contains both the dress and PreOwnedDresss
    #this program instatiates 4 objects
    #the program defines 2 functions which can be perfomed upon any of the objects
    #the program uses these functions to be a business program dealing with
    #changing the values of prices and displaying product information



import dress

def main():
    import dress
    
    #instatiates 2 Dress objects
    d1 = dress.Dress("D111","Floral", "Jenny Flower", "medium", 695.98)
    d2 = dress.Dress("D112","Maxi", "John Dalsey", "small", 199.98)
    #instatiates 2 PreOwneDress objects
    pod1 = dress.PreOwnedDress("D113","Wrap", "Jason Georges", "medium" , 111.88, 2016)
    pod2 = dress.PreOwnedDress("D114","Floral", "Jenny Flower", "large", 100.85, 2015)

    #creates and empty dress list
    dress_list = []
    #adds the 4 objects created earlier to the dress list
    dress_list.append(d1)
    dress_list.append(d2)
    dress_list.append(pod1)
    dress_list.append(pod2)


    #defines function to display the info of each designer dress
    def designerdress(dressList, desig):
        flag = 0
        for dress in dressList:
            if dress.get_designer().upper() == desig.upper():
                print(dress.__str__())
                flag = 1
                print("")
        if flag == 0:
            print("This is not a valid choice for a designer")

    def newPrice(dresslist):
        
        dressID = input("Please enter the dress ID: ").upper()
        np = float(input("Please enter the new price: "))
        #validation loop to make sure that the values of np are between 
        while np <= 0 or np >= 2000:
            print("The price must be between 0 and $2000.00")
            np = float(input("Please re-enter the new price: "))
            
        print("\n")
        #sets a flag which will notify the user if the price has been changed or not
        #which hinges on if the the dressID chosen is in dressList
        flag1 = 0
        for dress in dresslist:
            if dress.get_dress_id() == dressID:
                 dress.set_price(np)
                 #flag changes if the dress ID is found
                 flag1 = 1
        if flag1 == 1:
            print("The price has been updated! \n")
        else:
            print("The ID was not located! The price has not been updated! \n")


    #user input assigns value to start
    start = input("Do you want to begin the program?(yes or Yes to begin): ").upper()
    print("")
    
    while start == "YES":
        #prints a menu
        print("Welcome to the dress program!" + 
              "\n===============================" + 
              "\nA - Print dress information of a designer" + 
              "\nB - Change the price of a dress\n")
        
        #validation loop to make sure that the user chooses an valid choice from the menu
        flag2 = 0
        choice = input("Please enter menu choice (A or B): ").upper()
        while flag2 == 0:
            #
            if choice == "A":
                whatdesigner = input("Please enter the designer's name: ")
                designerdress(dress_list, whatdesigner)
                flag2 = 1
                
            elif choice == "B":
                newPrice(dress_list)
                flag2 = 1

            else:
                print("")
        
        #gives the user the option to chose another choice or exit the program
        start = input("Do you want to continue with the program?(yes or YES to continue) ").upper()
 
main()


