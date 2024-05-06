#!python3
"""
Fix this program.
It should ask the user to enter in 10 numbers and see
if the number is positive or negative
"""
for n in range(10):
    x = input("enter in a number")
    x = int(x)
    if x > 0:
        print('that is a positive number')
    elif x < 0:
        print('that is a negative number')
