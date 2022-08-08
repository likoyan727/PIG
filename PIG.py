import random

human_score = 0
comp_score = 0

#gets user's input for holding or rolling
def roll_hold():
    player_choice = raw_input("would you like to roll ('r') or hold ('h')? ")
    while (player_choice != "r") and (player_choice != "h"):
        player_choice = raw_input("Enter a valid input. \n would you like to roll ('r') or hold ('h')? ")
    return player_choice

#rolls a die and returns the result
def roll():
    roll = random.randint(1,6)
    return roll

#checks both total scores to see if someone won
def check_score():
    global human_score
    global comp_score
    if human_score >= 50:
        print("Human earned " + str(human_score) + " point")
        print("HUMAN WINS!")
        return "Game over"
    elif comp_score >= 50:
        print("Computer earned " + str(comp_score) + " points")
        print("COMPUTER WINS!")
        return "Game over"
    else:
        return "Game not over"

#Runs when it's the human's turn
def human_turn():
    global human_score
    global comp_score
    #checks if game is over or not
    check_score()
    if check_score() != "Game over":
        print("HUMAN'S TURN-----------------------------------------")
        print("CURRENT SCORES: Human: " + str(human_score) + " Computer: " + str(comp_score))
        player_choice = roll_hold()
        temp_score = 0
    #When the player chooses r, it rolls the die to determine points earned for that round
        while player_choice == "r":
            num = roll()
            print("You rolled a " + str(num))
            if num == 1:
                print("OOF you lost all your points")
                temp_score = 0
                break
            else:
                temp_score += num
            player_choice = roll_hold()
        human_score += temp_score
    else:
        return "Game over"

#Runs when it's the computer's turn
def comp_turn():
    global human_score
    global comp_score
    #checks if game is over or not
    if check_score() != "Game over":
        print("COMPUTER'S TURN-----------------------------------------")
        print("CURRENT SCORES: Human: " + str(human_score) + " Computer: " + str(comp_score))
        temp_score = 0
    #Computer rolls die until score for that round reaches 20 or until it rolls 1
        while temp_score < 20:
            num = roll()
            print("You rolled a " + str(num))
            if num == 1:
                print("OOF you lost all your points")
                temp_score = 0
                break
            else:
                temp_score += num

        comp_score += temp_score
    else:
        return "Game over"

#loops through a round of the game until one of the players wins
while check_score() == "Game not over":
    human_turn()
    if check_score() == "Game over":
        break
    comp_turn()
    if check_score() == "Game over":
        break
