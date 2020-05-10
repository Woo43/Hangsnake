import random
print("Hangsnake!\n")
playercount = 0
while playercount != 1 and playercount != 2:
    try:
        playercount = int(input("Are you playing with 1 or 2 players? "))
    except ValueError:
        print("Error. Only enter 1 or 2.")
        playercount = int(input("Are you playing with 1 or 2 players? "))
if playercount == 2:
    secretword = input("Select a secret word. ")
    try:
        maxguesses = int(input("How manny errors do you want to give? "))
    except ValueError:
        print("Number, please.")
        maxguesses = int(input("How manny errors do you want to give? "))
    print(
        "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    )
elif playercount == 1:
    secretword = random.choice(the_list_to_end_all_lists)
    maxguesses = 5
secretlist = list(secretword.upper())
length = len(secretlist)
mismatch = 0
oofcount = 0
letters_correct = 0
dedupelist = list(dict.fromkeys(secretlist))
dedupelen = len(dedupelist)
winner = False
print("\n")
for x in secretlist:
    print("_", end =" ")
print("\n")
print("You have " + str(maxguesses) + " incorrect guesses remaining." "\n")
letters = []
while oofcount < maxguesses and winner == False:
    guess = input("What letter do you want to guess? ").upper()
    if guess in letters:
        print("You already guessed that!")
    elif len(guess) != 1:
        print("Stop trying to break the program!")
    else:
        if guess in secretlist:
            letters_correct = letters_correct + 1
        else:
            oofcount = oofcount + 1
            print("You have " + str(maxguesses-oofcount) + " incorrect guesses remaining.")
        letters.append(guess)
        for x in secretlist:
            if x in letters:
                print(x,end =" ")
            else:
                print("_",end =" ")
        if oofcount == maxguesses:
            print("Game over. The secret word was " + secretword + ".")
        elif letters_correct == dedupelen:
            winner = True
if winner == True:
    print("You won!")