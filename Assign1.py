#!python3
# Write a program that uses a for loop to ask the user to enter
# in 5 numbers.  The program will determine the sum of the 5 numbers
# and calculate the average
# You must use only 1 input statement in your program

total = 0
for i in range(5):
    x = input(f"Enter in a number")
    x = int(x)
    total = total + x
print(f"The total of your numbers is {total}")