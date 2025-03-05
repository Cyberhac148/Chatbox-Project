def chatbot():
    name = input("May I ask for your name?")
    print("Hello! "+name+" I am your Delivery Chatbox!")
    print("***************************************")

    dob = int(input("Enter your birth year: "))  
    age = (2025 - dob)
    print("                                         ")
    print("This year you will be",age)  
    print("That's amazing! How may I help you today?")
    print("                                         ")

    while True:
        print("You may ask for help in the following options:")
        print("-------------------------------")
        print("1.When is my food arriving?")
        print("2.How do I contact my dasher?")
        print("3.I want a refund.")
        print("4.Exit conversation.")

        choice = input("Please enter the number that matches your issue:")

        if choice == "1":
            print("                                         ")
            print("You have selected option 1. When is my food arriving?")
            print("-------------------------------")
            time = int(input("How many mintues was it ago when you ordered your food?"))

            if time < 30:
                print("Your order will arrive soon!")
                
            else:
                print("Your order seems to be delayed. Attempt to check your order status by selecting 'Order History' in the app.")
            break
            
        elif choice == "2":
            print("                                         ")
            print("You have selected option 2. How do I contact my dasher?")
            print("-------------------------------")
            print("In order to contact your dasher, you must go through your order detials and select 'Contact Dasher'!")

            break
        elif choice == "3":
            print("                                         ")
            print("You have selected option 3. I want a refund.")
            print("-------------------------------")
            reason = input("May you explain the issue that has occured? For example: wrong order, missing item, damange order etc...")
            print("Thanks for the feedback! You can issue a refund by clicking 'Report issue' under the ChatBot option. Your reason: "+ reason)
            
            break
        elif choice == "4":
            print("                                         ")
            print("Have a nice day! Goodbye!")
            break
        else:
            print("                                         ")
            print("Invalid choice. Please selected a number from the menu options.")
chatbot()         