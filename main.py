def chatbot():
    print("Hello! I am your Delivery Chatbox!")

    name = input("May I ask for your name?")
    print(name+ ", that's a lovely name!")

    dob = int(input("Enter your birth year: "))  
    age = (2025 - dob)
    print("This year you will be", age)  
    print("That's amazing! How may I help you today?")

    while True:
        print("You may ask for help in the following options:")
        print("1.When is my food arriving?")
        print("2.How do I contact my dasher?")
        print("3.I want a refund.")
        print("4.Exit conversation.")

        choice = input("Please enter the number that matches your issue:")

        if choice == "1":
            print("You have selected option 1.")
            time = input("How many mintues was it ago when you ordered your food?")
            
            break
        elif choice == "2":
            print("You have selected option 2.")
            print("In order to contact your dasher")

            break
        elif choice == "3":
            print("You have selected option 3.")
            
            break
        elif choice == "4":
            print("Have a nice day! Goodbye!")
            break
        else:
            print("Invalid choice. Please selected a number from the menu options.")
chatbot()         