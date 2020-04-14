print("Hangsnake!\n")
# enter secret here
secretword = input("Select a secret word. ")
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
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
while oofcount < 5 and winner == False:
    guess = input("What letter do you want to guess? ").upper()
    truel = length - letters_correct
    if guess in letters:
        print('You already guessed that!')
    else:
        if guess in secretlist:
            letters_correct=letters_correct+1
        letters.append(guess)
        if len(guess) == 1:
            for x in secretlist:
                if x in letters:
                    print(x)
                    mismatch = 0
                else:
                    print("_")
                    mismatch = mismatch + 1
                    if mismatch == truel:
                        oofcount = oofcount + 1
                        mismatch = 0
            if oofcount == 5:
                print("Game over.")
            elif letters_correct == dedupelen:
                winner = True

        else:
            print("Stop trying to break the progam.")
if winner == True:
    print("You won!")
