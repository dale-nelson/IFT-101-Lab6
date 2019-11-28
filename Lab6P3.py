def validCheck():
    try:
        return int(input("Give me a number: "))
    except ValueError:
        print("That is not a number. Please try again.")

def validLoop():
    checking = validCheck()
    while not checking:
        checking = validCheck()
    return checking

def isPos():
    posCheck = validLoop()
    while posCheck < 0:
        print("""
Natural numbers are all integers greater than 0. You entered
a negative number. Please try again.
        """)
        posCheck = validLoop()
    return posCheck

def factorial(a):
    if a <= 1:
        return a
    return a * factorial(a-1)

print("This program outputs the factorial of a natural number entered by a user.")
posVal = isPos()
print("{0}! or {0} factorial is {1}".format(posVal, factorial(posVal)))