#Input Validation + Rhombus Pattern
#prompts for an integer n where n must be an odd integer  and not more than 5

import math


while True:
    n= input("Enter an odd integer >=5: ")
    if not n.isdigit():
        print("Invalid input. Please enter a valid input.")
        continue
    n = int(n)
    if n < 5:
        print("number has to be bellow or equal to 5")
        continue
    if n % 2 == 0:
        print("number should be an odd number")
        continue
    break

#printing 9*9rhombus pattern

print("\nfixed 9x9 rombus:\n")

size = 9
mid = size // 2

for i in range(size):
    spaces = abs(mid - i)
    stars = size - 2 * spaces

    print(" " * spaces, end="")
    print("*" * stars)

#printing rhombus with any valid n value
import math
print("\nGeneral Rhombus:\n")

mid = math.ceil(n / 2) - 1

for i in range(n):
    spaces = abs(mid - i)
    stars = n - 2 * spaces

    print(" " * spaces, end="")
    print("*" * stars)