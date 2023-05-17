def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    average = total / count
    return average

# Unused variable
x = 10

# Unused function argument
def multiply(a, b):
    return a * b

# Duplicate code
def add(a, b):
    return a + b

# Cyclomatic complexity
def check_grade(score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

# Long method
def long_method():
    result = 0
    for i in range(1000):
        result += i
    return result

# Inefficient code
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
