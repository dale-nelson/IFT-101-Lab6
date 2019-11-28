def sumN(a):
    if a <= 1:
        return a
    if a:
        return a + sumN(a - 1)

def cubeIt(a):
    list_of_cubes = []
    if a <= 1:
        return a
    while a:
        list_of_cubes.append(a**3)
        a -= 1
    return list_of_cubes

def sumNCubes(a):
    return sum(a)

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

print(
"""This program takes a positive integer given by the user and does 2 things:
1) Calculates the sum of all integers in the range of 1:n
2) Calculates the sum of all cubes of integers in the range of 1:n"""
)

posval_needed = isPos()
print("The sum of all natural numbers up in the range of 1:{0} is {1}"\
    .format(posval_needed, sumN(posval_needed)))

cubed_list = cubeIt(posval_needed)
print("The sum of all cubes of the natural numbers in the range of 1:{0} is {1}"\
    .format(posval_needed, sumNCubes(cubed_list)))