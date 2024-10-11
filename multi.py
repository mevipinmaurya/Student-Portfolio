def multiply_two_numbers(num1, num2):
    return num1 * num2

def main():
    # Input two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculate the product
        result = multiply_two_numbers(num1, num2)
        print(f"The product of {num1} and {num2} is: {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
