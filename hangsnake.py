print("Hangsnake!\n")
# enter secret here
secretword = input("Select a secret word. ")
maxguesses = int(input('How manny errors do you want to give? '))
print(
    "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
)
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
    print("_")
print("\n")
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
        letters.append(guess)
        for x in secretlist:
            if x in letters:
                print(x)
#                mismatch = 0
            else:
                print("_")
#                mismatch = mismatch + 1
#                if mismatch == dedupelen:
#                    oofcount = oofcount + 1
#                    mismatch = 0
        if oofcount == maxguesses:
            print("Game over.")
        elif letters_correct == dedupelen:
            winner = True
if winner == True:
    print("You won!")
