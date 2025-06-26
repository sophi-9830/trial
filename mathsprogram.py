def option_one_action():
    """Function to execute when Option 1 is chosen yay."""
    print("You selected Option 1:")
    num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())
    num_result = num1 + num2
    print(f"Your result is {num_result}")

def option_two_action():
    """Function to execute when Option 2 is chosen."""
    print("You selected Option 2:")
    num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())
    num_result = num1 - num2
    print(f"Your result is {num_result}")

def option_three_action():
    """Function to execute when Option 3 is chosen."""
    print("You selected Option 3:")
    num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())
    num_result = num1*num2
    print(f"Your result is {num_result}")

def option_four_action():
    """Function to execute when Option 3 is chosen."""
    print("You selected Option 4:")
    num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())
    num_result = int(num1/num2)
    remainder =  num1%num2
    if remainder == 0:
      print(f"Your result is {num_result}")
    else:
      print(f"Your result is {num_result} with a remainder of {remainder}")

def display_menu():
    """Displays the menu options to the user."""
    print("\n--- Main Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("0. Exit")
    print("-----------------")

def main_menu():
    """Manages the main menu loop and user interaction."""
    while True:
        display_menu()
        choice = input("Enter your choice (0-3): ")

        if choice == '1':
            option_one_action()
        elif choice == '2':
            option_two_action()
        elif choice == '3':
            option_three_action()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

# Call the main menu function to start the program
if __name__ == "__main__":
    main_menu()
