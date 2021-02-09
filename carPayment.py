#Calvin Leo Comstock-Fisher
#2/8/21
#Car Payment Program

def dataInput():
    """Gets the input for the name, amount, percentage, and number of months"""
    name = input("What is your name?\n")
    p = int(input("How much did the car cost?\n"))
    q = input("Do you know the annual percentage rate of the loan? (y/n)\n").lower()
    if q == "y":
        r = float(input("What is the annual percentage rate of the loan?\n"))
    else:
        r = 4.5
    q2 = input("Do you know the number of months that you are paying the loan? (y/n)\n").lower()
    if q2 == "y":
        n = int(input("How many months are you paying?\n"))
    else:
        n = 60
    return(name, p, r, n)

def calculate(p, r, n):
    """Calculates the monthly pay and returns it"""
    rate = r/1200
    M = p*rate*(1+rate)**n/(((1+rate)**n)-1)
    return(M)

def display(name, p, r, n, M):
    """Prints everything"""
    print("Your Name:",name)
    print("Amount the Car Cost:",p)
    print("Annual Rate of Interest:",r)
    print("Number of years to pay:",n/12)
    print("{:}{:.2f}".format("Monthly Payment: $",M))

def main():
    """Main function that loops if the user wants it too"""
    flag = "y"
    while flag == "y":
        name, p, r, n = dataInput()
        M = calculate(p, r, n)
        display(name, p, r, n, M)
        flag = input("Would you like to run the program again? (y/n)\n").lower()
main()