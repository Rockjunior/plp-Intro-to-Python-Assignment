# Step 1: Define operation functions
DEFINE function add(a, b)
    RETURN a + b

DEFINE function subtract(a, b)
    RETURN a - b

DEFINE function multiply(a, b)
    RETURN a * b

DEFINE function divide(a, b)
    RETURN a / b  // Ensure that b is not zero when calling

# Step 2: Map operations to functions in a dictionary
SET operations = { "+": add, "-": subtract, "*": multiply, "/": divide }

# Step 3: Get user input
PRINT "Enter the first number:"
SET first_number = USER_INPUT

PRINT "Enter the second number:"
SET second_number = USER_INPUT

PRINT "Enter the operation (+, -, *, /):"
SET operation = USER_INPUT

# Step 4: Perform the operation using the dictionary
SET result = operations[operation](first_number, second_number)

# Step 5: Display the result
PRINT "The result of", first_number, operation, second_number, "is", result
