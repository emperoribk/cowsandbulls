import random
print('Welcome to cow and bulls game') 
print("Type exit at any place to exit.")


players_character = input('Enter your name: ')

def compare_numbers(number, user_guess):
    cowbull = [0,0] 
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__=="__main__":
    playing = True 
    number = str(random.randint(0,9999)) 
    guesses = 0

    while playing:
        user_guess = input("Give me your prediction: ")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1

        print((players_character) +" You have "+ str(cowbullcount[1]) + " cows, and " + str(cowbullcount[0]) + " bulls." )

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "trial(s)" + "! The suggested digits were "+str(number))
            break 
        else:
            print("Your guess was not right, Try again.")