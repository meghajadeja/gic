def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the difference between a and b."""
    return a - b
# Import the functions from the mymath module
from mymath import add, subtract

# Example usage of the imported functions
num1 = 10
num2 = 5

sum_result = add(num1, num2)
diff_result = subtract(num1, num2)

print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The difference between {num1} and {num2} is: {diff_result}")
