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
