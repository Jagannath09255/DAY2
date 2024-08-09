def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    # Initialize an empty array
    numbers = []

    # Get the initial size of the array
    size = int(get_valid_number("Enter the initial size of the array: "))

    # Populate the array with initial elements
    print(f"\nEnter {size} numbers:")
    for i in range(size):
        num = get_valid_number(f"Number {i+1}: ")
        numbers.append(num)

    # Print the initial array
    print("\nInitial array:", numbers)

    # Allow the user to add more elements
    while True:
        choice = input("\nDo you want to add another number? (yes/no): ").lower()
        if choice != 'yes':
            break
        
        num = get_valid_number("Enter the number to add: ")
        numbers.append(num)
        print("Current array:", numbers)

    # Print the final array
    print("\nFinal array:", numbers)

if __name__ == "__main__":
    main()