import random       #random modeule for using randint

def game():
    print("You are playing a game...")
    
    score = random.randint(1, 100)          # Random score between 1 and 100

    # Fetch the hiscore
    with open("ch9_02_Hi-Score.txt") as f:  # Open file in read mode
        hiscore = f.read()                  # Read existing content from file

        if hiscore != "":                   # If file is not empty
            hiscore = int(hiscore)          # Convert to integer
        else:
            hiscore = 0                     # If empty, assume high score is 0 as default

    print(f"Your score: {score}")          #show the score u got

    if score > hiscore:
        # Write new high score to the file
        with open("ch9_02_Hi-Score.txt", "w") as f:  # Open file in write mode
            f.write(str(score))                      # Write the new high score as string

    return score                                 

game()

#here new high score will be replaced in text file instead of append
