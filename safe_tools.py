def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"

def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"