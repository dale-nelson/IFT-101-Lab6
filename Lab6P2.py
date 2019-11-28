def fib(a):
    if a <= 1:
        return a
    return fib(a - 1) + fib(a - 2)

def valid_check():
    try:
        return int(input("Give me a number: "))
    except ValueError:
        print("That is not a number. Please try again.")

def valid_loop():
    checkVal = valid_check()
    while not checkVal:
        checkVal = valid_check()
    return checkVal

def is_Pos():
    posCheck = valid_loop()
    while posCheck < 0:
        print("Fibonacci sequences use only positive numbers. Please try again.")
        posCheck = valid_loop()
    return posCheck

print(
"""This program will compute the value of the n-th value of the Fibonacci Sequence.
What n-th term would you like to generate?"""
)

posCheck = is_Pos()
print("Term {0} of the Fibonacci sequence is {1}"\
    .format(posCheck, fib(posCheck)))