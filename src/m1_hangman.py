"""
Hangman.

Authors: PUT_YOUR_NAME_HERE and YOUR_PARTNERS_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
def main():
        #Global Variables:


        chosenword = random_word_generator()
        difficulty = difficulty_options()
        wrong = 0
        display = []
        for k in range(len(chosenword)):
            display.append("_ ")
            print(display[k],end='')
        print()

        while(True):
            foundletters = []
            output=input_letter(chosenword,difficulty,wrong,foundletters)
            if type(output) == str:
                display=display_word(chosenword, foundletters, output,display)
            else:
                wrong = number_of_remaining_guesses(difficulty,output)

            #LOSE CONDITION
            if wrong == difficulty:
                print("You have lost the game!")
                playagain=end_game()
                if playagain == 'Y':
                    main()
                else:
                    break

            #WIN CONDITION
            for i in range(len(display)):
                value = True
                if display[i]=='_':
                    value == False

            if value == True:
                print('You Win!')
                playagain=end_game()
                if playagain=='Y':
                    main()
                else:
                    break




    #FUNCTION DEFINITIONS:
def difficulty_options():
    difficulty=int(input('Choose The Number of Incorrect Attempts: '))
    return difficulty

def random_word_generator():
    import random
    with open('words.txt') as f:
        f.readline()
        string=f.read()
        words=string.split()
    randomindex = random.randint(0,len(words)-1)
    chosenword=words[randomindex]
    print(chosenword)
    return chosenword

def display_word(chosenword,foundletters,letter,display):
    for j in range(len(foundletters)):
        index = foundletters[j]
        display[index]=letter
    for i in range(len(display)):
        print(display[i],end='')
    print()
    return display





def input_letter(chosenword,difficulty,wrong,foundletters):
    letter=input('What Letter do You Want to Try?:')
    if checkletter(letter,chosenword,foundletters)==True:
        print('Good Guess! There is a ',letter,' In the word!')
        return letter
    else:
        print("Sorry! There are no ", letter," in the secret word!")
        wrong = wrong + 1
        return wrong






def number_of_remaining_guesses(difficulty,wrong):
    numbereremaining=difficulty-wrong
    print("You have ,",numbereremaining," guesses left until you lose the game!")
    return wrong

def end_game():
    play_again=input("Do you want to play again? (Y/N):")
    if play_again=='Y':
        return play_again
    else:
        print("Goodbye!")
        return play_again

def checkletter(letter,chosenword,foundletters):
    yes=0
    for k in range(len(chosenword)):
        if letter==chosenword[k]:
            foundletters.append(k)
            yes=1

    if yes==1:
        return True
    return False






















#Calling of Main
main()