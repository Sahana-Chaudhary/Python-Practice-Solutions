'''
print pattern

    *      *
   * *    * *
  * * *  * * *
 * * * * * * * *
* * * * * * * * *
'''
r = int(input("Enter number of rows: "))

for i in range(1, r + 1):
    # Leading spaces
    for space in range(r - i):
        print(" ", end="")

    # Left hill (i stars)
    for star in range(i):
        print("* ", end="")

    # Middle gap (shrinks each row)
    for gap in range(2 * (r - i)):
        print(" ", end="")

    # Right hill (i - 1 stars)
    for star in range(i - 1):
        print("* ", end="")

    print()
