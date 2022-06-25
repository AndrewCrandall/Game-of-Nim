"""
Andrew Crandall
07/16/2021
CSC 119 802
Title: Game of Nim
Summary: The game of nim, however the difficulty, and number of balls are randomized each game
"""


from random import seed, randint

def main():                     # definition of main program
    #seed()                      # initialize the random number generator for the game play

    # -------------------------------------------------------
    # INPUT - to randomlize the game play
    # -------------------------------------------------------

    ballCount = randint(10, 100)# randomly generate the amount of balls to play
    turn = randint(0,1)         # randomly generate who goes first (0) player (1) computer
    mode = randint(0,1)         # randomly generate mode of computer (0) smart (1) stupid

    # -------------------------------------------------------
    # PROCESS - play the game of NIM taking turns
    # -------------------------------------------------------

    print("About the Game: ")

    print("The number of marbles and difficulty of the game is randomly determined each time you play! ")
    print("")
    print("Who ever has 0 marbles at the end, loses. ")
    print("")
    print("Keep in mind, you need to take atleast one marble a turn, and at most you can only take half of the total marbles. ")
    print("")
    print("If the number of marbles are odd, you can take half plus one, for example if you had 15 marbles, you can take 8. ")
    print("")
    print("If the number of marlbes are even, you can only take exactly half of them")
    print("")
    print("If the total number of marbles are '21', you cannot take '10.5' marbles, please keep the numbers whole such as '10'. ")
    print("")
    print("Good luck! ")
    print("")
    
    print("***** Game of NIM Starts *****")
    while ballCount > 0:        # if there are still balls left, then keep playing
        print("\t\tBall count:", ballCount)
        if turn == 0:           # player turn
            print("\n\tPLAYER TURN")
            ballCount = ballCount = playerTurn(ballCount)
            # TODO: call the playerTurn function 
            turn = 1            # switch the turn 1 - for computer turn next
        else:                   # computer turn
            if mode == 0:       # computer smart mode
                print("\n\tCOMPUTER TURN - Mode: Smart")
                ballCount = computerSmart(ballCount)
                
                # TODO: call the computerSmart function
            else:               # computer hard mode
                print("\n\tCOMPUTER TURN - Mode: Stupid")
                ballCount = computerStupid(ballCount)
                # TODO: call the computerStupid function
            turn = 0            # switch the turn 0 - for player turn next
        # TODO: ballCount needs to be updated for each turn
                
    # -------------------------------------------------------
    # OUTPUT - The player who takes the last ball loses.
    # once the ballCount goes to 0, the turn switches, so it is the other
    # player then that wins
    # -------------------------------------------------------
    print("\t\tBall count:", ballCount)
    if turn == 0 and ballCount == 0:
        print("\n***** GAME of NIM Winner! PLAYER *****\n\n")
    else:
        print("\n***** Game of NIM Winner! COMPUTER *****\n\n")

        # execution of main program





def computerStupid(ballCount):
    ## Stupid Computer Turn
    # make sure the ballcount is greater than 0
    # if it is, ballcount is // 2 and randomly selected
    # difference is random number subtracted by ballcount
    # if ballcount is equal to one, difference is ballcount - 1
    # return difference, (ballcount - choice)
    
    while ballCount > 0:
        if ballCount == 1:
            difference = ballCount - 1
            return difference
            
        else:
            total = randint(1,ballCount // 2) #"Stupid effect" of taking a random number of ballcount //2
            difference = ballCount - total
            return difference
   
        




def computerSmart(ballCount):

    ## Smart Computer Turn
    # If it is still the computers turn, decide between the choices of [3, 7, 15, 31, 63]
    # based off of the number of ballcount, set the difference to the highest possible power of two minus 1
    # If the ballcount is less than or  equal to three, difference is ballCount minus 1
    # return difference (ballcount - choice)


    cTurn = 0

    while cTurn == 0: #Computer turn = 0, end of turn = 1

        choices = [3, 7, 15, 31, 63]
 

        if ballCount > 63:
            difference = choices[4] #makes it equal 63
            cTurn = 1
                
        elif ballCount > 31 and ballCount < 63 :
            difference = choices[3] #makes decision equal 31
            cTurn = 1
                
        elif ballCount > 15 and ballCount < 31:
            difference = choices[2] #makes decision equal 15
            cTurn = 1
                
        elif ballCount > 7 and ballCount < 15:
            difference = choices[1]#makes decision equal 7
            cTurn = 1
            
        elif ballCount > 3 and ballCount < 7:
            difference = choices[0]#makes decision equal 3
            cTurn = 1

        if ballCount == 3 or ballCount ==  7 or ballCount == 15 or ballCount == 31 or ballCount == 63: 
            total = randint(1,ballCount // 2) #adds the "stupid" effect, where if the ballCount equals a power of two minus one, it will have a random act
            difference = ballCount - total
            cTurn = 1

        if ballCount <= 3: # allows for decisions to be made while ballCount is less than three
            difference = ballCount - 1
            cTurn = 1
                
            
    return difference #returns the remaining number of balls




def playerTurn(ballCount):
