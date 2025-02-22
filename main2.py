try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("Result:", result)
    
    def tell(msg: str) -> str:
        print(msg)
        
except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    tell("Carol ma'am is a proooo")