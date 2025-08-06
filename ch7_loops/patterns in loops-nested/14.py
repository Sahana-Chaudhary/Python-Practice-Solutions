'''
print pattern

* * * 
*   * 
* * * 
'''

r = int(input("Enter number: "))     # Step 1: Take number of rows/columns (since it's a square)

for i in range(1, r + 1):            # Step 2: Loop through each row from 1 to r
    if(i == 1 or i == r):            # Step 3: First or last row
        print("* " * r, end="")      #     => Print full row of stars
    else:                            # Step 4: Middle rows
        print("* ", end="")          #     => Left star
        print("  " * (r - 2), end="")#     => (r-2) spaces between (each "  " is two spaces to align with "* ")
        print("* ", end="")          #     => Right star
    print()                          # Step 5: Move to the next line
