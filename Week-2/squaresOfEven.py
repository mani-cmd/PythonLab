# Instructor at a math program
# concept of using the control statements to manipulate loops
# Create a program that takes an interger N as input and print the squares of even numbers from 1 to n
# Skipping odd numbers

N = int(input())

for i in range(1, N+1):
    if(i%2 == 0):
        print(f"{i**2}")
