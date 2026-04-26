
import logging

# 1. Configure logging
logging.basicConfig(
    filename="friend_error_logs.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    """Divide two numbers with error handling."""
    try:
        result = a / b
    except ZeroDivisionError as e:
        logging.error(f"ZeroDivisionError: Tried dividing {a} by zero.")
        print("Error: Cannot divide by zero!")
    except TypeError as e:
        logging.error(f"TypeError: Invalid types {a}, {b}")
        print("Error: Inputs must be numbers.")
    else:
        print(f"Division Result: {result}")
    finally:
        print("Finished divide_numbers execution.\n")

def access_list_element(lst, index):
    """Access a list element safely."""
    try:
        element = lst[index]
    except IndexError as e:
        logging.error(f"IndexError: Index {index} out of range for list.")
        print("Error: Index out of range!")
    else:
        print(f"Element at index {index}: {element}")
    finally:
        print("Finished access_list_element execution.\n")

def simulate_runtime_error():
    """Simulate a custom runtime error."""
    try:
        raise RuntimeError("Simulated runtime error for demo!")
    except RuntimeError as e:
        logging.error(f"RuntimeError: {e}")
        print(f"Caught runtime error: {e}")
    finally:
        print("Finished simulate_runtime_error execution.\n")

# ---------------- Testing the functions ----------------
if __name__ == "__main__":
    print("Task 9: Error Handling & Logging (Friend's Version)\n")

    # Divide numbers
    divide_numbers(15, 3)    # Normal
    divide_numbers(7, 0)     # ZeroDivisionError
    divide_numbers("x", 10)  # TypeError

    # Access list elements
    sample_list = [5, 10, 15]
    access_list_element(sample_list, 0)  # Normal
    access_list_element(sample_list, 10) # IndexError

    # Simulate runtime error
    simulate_runtime_error()

    print("Check 'friend_error_logs.log' for logged errors.")