#Calvin Leo Comstock-Fisher
#2/8/21
#Bowling Program

print("Welcome to the Bowling Program.")

def inputdata():
    dictionary = {}
    for i in range(0,2):
        name = input("What is the bowlers name?")
        numGames = input("How many games have you bowled?\n")
        if numGames < 2:
            print("You must have played at least 2 games")
        avg = input("What is your average?\n")
        scorePerGame = input("What score did you get for each of the games")
        list = [numGames, avg, ]
    print(dictionary)
        

def calculate():

def display():

def main():
    numGames, avg, scorePerGame = inputdata()

main()