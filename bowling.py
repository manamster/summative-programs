#Calvin Leo Comstock-Fisher
#2/8/21
#Bowling Program

print("Welcome to the Bowling Program.")

def inputdata():
    """The input funtion that makes sure that the player has played 2/3 games and then gets the information from them about their scores"""
    g1 = input("What was the score of your first game?\n")
    g2 = input("What was the score of your second game?\n")
    flag = input("Did you play a 3rd game? (y/n)\n")
    if flag == "y":
        numGames = 3
    else:
        numGames = 2
    if numGames > 2:
        g3 = input("What was the score of your third game?\n")
        return(g1, g2, g3,numGames)
    else:
        #This will be the average based on the flag
        g3 = input("What is your average?\n")
        return(g1, g2, g3, numGames)

def calculate(g1, g2, g3, numGames):
    """Calculates the average based on wether it was 2 or 3 games"""
    if numGames == 2:
        total = g1 + g2 + g3 #g3 if it is 2 games is the average
        avg = total / 3
        return(total, avg)
    elif numGames > 2:
        total = g1 + g2 + g3
        avg = total / 3
        return(total, avg)

def display(g1,g2,g3,numGames,total,avg):
    """The display function that prints the users games and their total and average"""
    print("First Game:", g1)
    print("Second Game:",g2)
    if numGames == 2:
        print("Their personal average:", g3)
    else:
        print("Third Game:",g3)
    print("Total:", total)
    print("Calculated Average:",avg)

def main():
    """The main function that calls everything"""
    g1, g2, g3, numGames= inputdata()
    total, avg= calculate(g1, g2, g3, numGames)
    display(g1,g2,g3,numGames,total,avg)
    input("Press enter to exit.")

main()