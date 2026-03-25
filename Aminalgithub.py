"""
Advanced Programming — TA Practice Session (Week 4)
STUDENT VERSION (TODOs only)

Topic: Control statements — for/while loops, break, continue, nested loops
Reference: Week 4 slides (for, while, break, continue, input validation, nested loops). 

How to use:
- Open in VS Code.
- Complete each TODO.
- Run this file and test each practice from the menu.

Rules:
- Keep your code readable.
- Use the loop type requested (for vs while).
"""

# ============================================================
# Practice 1 — Average of a Series (FOR loop)
# Goal: definite loops with range(n)
# ============================================================

def practice_1():
    """
    TODO:
    Write a program that:
    1) Asks the user: "How many numbers do you have?"
    2) Uses a for loop to read n numbers.
    3) Computes and prints the average.

    Notes:
    - Use float for sum.
    - Assume n is an integer >= 1 (no validation needed in this practice).
    """
    # TODO: read n
    # TODO: initialize total sum
    # TODO: loop n times, read x each time, add to sum
    # TODO: print average (sum / n)
    pass

num_count_str = input("How many numbers do you have? ")
try:
    num_count = int(num_count_str)
    if num_count <= 0:
        print("Please enter a positive number.")
        exit()
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

total_sum = 0.0
for i in range(num_count):
    # Prompt the user for each number
    num_str = input(f"Enter number {i + 1}: ")
    # Basic error handling for each number input
    try:
        current_number = float(num_str)
        total_sum += current_number
    except ValueError:
        print(f"Invalid input for number {i + 1}. Skipping this entry.")
    if num_count > 0:
        average: float = total_sum / num_count
    print(f"\nThe average of the {num_count} numbers is: {average}")




# ============================================================
# Practice 2 — Odd Numbers in Range (FOR loop + range start/end)
# Goal: range(start, end+1) and modulo
# ============================================================

def practice_2():
    """
    TODO:
    Ask the user for:
      - start number (s)
      - end number (e)

    Then print all odd numbers from s to e (inclusive) on ONE line.

    Constraints:
    - Use a for loop.
    - Use: if i % 2 == 1
    - Print with spaces (e.g., end=" ").
    """
    # TODO: read s and e
    # TODO: for loop from s to e inclusive
    # TODO: if odd -> print
    pass

start_num = int(input("Enter the start number (s): "))
end_num = int(input("Enter the end number (e): "))


print(f"Odd numbers from {start_num} to {end_num} (inclusive): ", end="")
for i in range(start_num, end_num + 1):
    if i % 2 == 1:
        print(i, end=" ")

# ============================================================
# Practice 3 — Fibonacci Sequence (FOR loop)
# Goal: iterative update (f_i, f_j)
# ============================================================

def practice_3():
    """
    TODO:
    Ask the user to enter n (integer).
    If n < 2:
      print a message that n must be >= 2 (or "larger than 1").
    Else:
      print Fibonacci sequence from F0 up to Fn on ONE line.

    Example for n=7:
      0 1 1 2 3 5 8 13

    Requirements:
    - Use a for loop.
    - Use two variables that keep the previous two Fibonacci numbers.
    """
    # TODO: read n
    # TODO: validate n
    # TODO: initialize f_i, f_j
    # TODO: print starting values
    # TODO: loop to compute next values and print
    pass

def print_fibonacci_sequence():
    """
    Asks the user for an integer n >= 2 and prints the Fibonacci sequence 
    from F0 up to Fn using a for loop and two variables.
    """
    
    # 1. Read n from user input
    try:
        n = int(input("Enter an integer n (n >= 2): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # 2. Validate n
    if n < 2:
        print("n must be >= 2 (or larger than 1).")
        return

    # 3. Initialize the first two Fibonacci numbers
    f_prev = 0  # Represents F_{i-2}
    f_curr = 1  # Represents F_{i-1}

    # 4. Print starting values without a newline at the end
    print(f_prev, f_curr, end=" ")

    # 5. Loop to compute the next values and print them
    # The loop runs from the 3rd number (i=2) up to and including the nth number (i=n)
    for i in range(2, n + 1):
        f_next = f_prev + f_curr
        print(f_next, end=" ")
        
        # Update the variables for the next iteration
        f_prev = f_curr
        f_curr = f_next

    # Print a final newline character for clean output after the sequence
    print()

# Call the function to run the program
print_fibonacci_sequence()



# ============================================================
# Practice 4 — Input Validation + continue (WHILE True + break)
# Goal: validate start/end are positive and end > start,
#       then print odd numbers (skip evens using continue)
# ============================================================

def practice_4():
    """
    TODO:
    1) Keep asking for start and end until the user enters:
         - start >= 0
         - end >= 0
         - end > start
       Use: while True: ... if valid: break else: print error message
    2) After valid input:
       Print all odd numbers from start to end (inclusive).
       Use 'continue' to skip even numbers.

    Requirements:
    - Use while True + break for validation.
    - Use continue inside the for loop.
    """
    # TODO: input validation loop
    # TODO: printing loop using for + continue
    pass

"""
This script asks the user for a start and end number, validates the input
to ensure both numbers are non-negative and the end number is greater than
the start number. If valid, it then prints all odd numbers within that range
(inclusive), using 'continue' to skip even numbers.
"""

while True:
    try:
        # Get user input and convert to integers
        start = int(input("Enter the start number (>= 0): "))
        end = int(input("Enter the end number (>= 0 and > start): "))

        # Check the validation criteria
        if start >= 0 and end >= 0 and end > start:
            # If valid, break the loop
            break
        else:
            # If invalid, print an error message
            print("Error: Input must be >= 0 for both numbers, and the end number must be greater than the start number. Please try again.")
    except ValueError:
        # Handle cases where the user enters non-integer values
        print("Error: Please enter valid integers for both numbers. Please try again.")

# After valid input, print all odd numbers in the range
print(f"\nOdd numbers from {start} to {end} (inclusive):")
for number in range(start, end + 1):
    # Check if the number is even
    if number % 2 == 0:
        # If even, skip the rest of the loop body and continue to the next iteration
        continue
    # If the code reaches here, the number is odd, so print it
    print(number)




# ============================================================
# Practice 5 — break vs continue (STRING scan)
# Goal: loop through characters, demonstrate break/continue
# ============================================================

def practice_5():
    """
    TODO:
    Ask the user to enter a string.

    Part A (break):
      Print characters one per line UNTIL a space ' ' is found.
      When you see a space, break the loop.
      After the loop, print: "end of loop"

    Part B (continue):
      Print ALL characters one per line, BUT skip spaces.
      Use continue when char == ' '.
      After the loop, print: "end of loop"
    """
    # TODO: read text
    # TODO: Part A break version
    # TODO: Part B continue version
    pass

# Read text from the user
text = input("Please enter a string: ")
print()

# Part A (break): Print characters until a space is found
print("--- Part A (break version) ---")
for char in text:
    if char == ' ':
        break
    print(char)
else:
    # This 'else' block will only execute if the loop finishes without hitting a break
    # For this specific problem where break is guaranteed if there's a space, 
    # it primarily handles the edge case of input with no spaces.
    pass 
print("end of loop")
print()

# Part B (continue): Print all characters except spaces
print("--- Part B (continue version) ---")
for char in text:
    if char == ' ':
        continue
    print(char)
print("end of loop")

# ============================================================
# Bonus (Optional) — Nested Loops: Rectangle Border of Stars
# Goal: one loop + if/else OR nested loops (your choice)
# ============================================================

def bonus():
    """
    OPTIONAL TODO:
    Print a rectangle border using stars '*'.

    Version A (simple, like slides):
      Print 9 rows and 9 columns where:
      - first and last rows are "*********"
      - middle rows are "*       *"  (a star, spaces, star)

    Version B (general):
      Ask user for rows and columns (>= 2), then print a border.

    You can do either A or B.
    """
    # TODO: implement if you want extra practice
    pass


# ============================================================
# Main runner
# ============================================================

def main():
    print("\n=== Advanced Programming: TA Practice Session (Week 4) — Student ===\n")
    print("Choose a practice to run:")
    print("1) Average of a series (for loop)")
    print("2) Print odd numbers in a range (for loop)")
    print("3) Fibonacci sequence up to n (for loop)")
    print("4) Input validation + continue (while + for)")
    print("5) break vs continue (string scan)")
    print("6) Bonus: stars rectangle (optional)")
    print("0) Exit")

    choice = input("\nEnter choice (0-6): ").strip()

    if choice == "1":
        practice_1()
    elif choice == "2":
        practice_2()
    elif choice == "3":
        practice_3()
    elif choice == "4":
        practice_4()
    elif choice == "5":
        practice_5()
    elif choice == "6":
        bonus()
    else:
        print("Goodbye.")

if __name__ == "__main__":
    main()


