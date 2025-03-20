def find_NOK(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = 56
num2 = 98
result = find_NOK(num1, num2)
print(f"The NOK of {num1} and {num2} is: {result}")

