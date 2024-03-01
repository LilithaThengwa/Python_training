def math_divide(n1, n2):
    try:
        result = n1 / n2
        print("the answer is ", result)
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    else:
        print("Division was successful.")
    finally:
        print("Operation done.")

# Try block: Lets you test a block of code for errors. Executes the division operation. In n2 != 0, prints result.
# Except block: Lets you handle the error. Catches the error and prints an error message instead of crashing the program.
# Else executes if there is no error.
# Finally block: Executes no matter what. Ensures some code runs regardless of an error occuring. Useful for cleaning up resources, like closing files.
         
      