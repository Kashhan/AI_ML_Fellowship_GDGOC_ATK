from modules.math_ops import area_of_circle, factorial
from modules.string_ops import reverse_string
from modules.games import number_guessing_game
from modules.records import student_menu, contact_menu
from modules.bank import demo_bank_accounts
from modules.generators_mod import demo_generators
from modules.decorators_mod import demo_decorator
from mypackage import add_numbers, print_details, square, uppercase


def run_math_demo():
    print("Math Operations")
    print("Area of circle with radius 5:", area_of_circle(5))
    print("Factorial of 5:", factorial(5))
    print()


def run_string_demo():
    print("String Operations")
    print("Reverse of Python:", reverse_string("Python"))
    print()


def run_bank_demo():
    print("Bank Account System")
    demo_bank_accounts()
    print()


def run_generators_demo():
    print("Generators")
    demo_generators()
    print()


def run_decorators_demo():
    print("Decorators")
    demo_decorator()
    print()


def main():
    while True:
        print("\nTask 4 Main Menu")
        print("1 Math operations")
        print("2 String operations")
        print("3 Number guessing game")
        print("4 Student records")
        print("5 Contact manager")
        print("6 Bank account system")
        print("7 Generators")
        print("8 Decorators")
        print("9 Custom package demo")
        print("10 Exit")


        choice = input("Enter your choice: ")

        if choice == "1":
            run_math_demo()

        elif choice == "2":
            run_string_demo()

        elif choice == "3":
            number_guessing_game()

        elif choice == "4":
            student_menu()

        elif choice == "5":
            contact_menu()

        elif choice == "6":
            run_bank_demo()

        elif choice == "7":
            run_generators_demo()

        elif choice == "8":
            run_decorators_demo()

        elif choice == "9":
            run_package_demo()

        elif choice == "10":
            break
        
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

def run_package_demo():
    print("Custom Package Demo")
    print(add_numbers(1, 2, 3, 4))
    print(square(5))
    print(uppercase("task four"))
    print_details(name="Ali", role="Student", task=4)
    print()
