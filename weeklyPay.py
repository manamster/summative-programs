#Calvin Leo Comstock-Fisher
#2/8/21
#Weekly Pay Program

def dataInput():
    """This is the function that gets the name, hours worked, and the payrate of an employee"""
    name = input("What is the employee's name?\n")
    hours = int(input("How many hours did they work?\n"))
    if hours < 40:
        hours = 40
    payRate = float(input("What is their pay rate?\n"))
    if payRate < 11:
        payRate = 11
    return(name, hours, payRate)
    

def calculate(hours, payRate):
    """Calculates the correct wage of the employee"""
    if hours == 40:
        wage = hours * payRate
        if hours > 40:
            overtime = hours - 40
            wage += overtime * (payRate * 1.5)

    return(wage)

def display(name, hours, payRate, wage):
    """Prints all the information about the employees work that week"""
    print("Name:", name)
    print("Hours Worked:", hours)
    print("Pay Rate: $", payRate, " per hour")
    print("Total Weekly Pay: $", wage)

def main():
    """Main function that loops and calls all other functions"""
    flag = "y"
    while flag == "y":
        name, hours, payRate = dataInput()
        wage = calculate(hours, payRate)
        display(name, hours, payRate, wage)
        flag = input("Do you want to run the program again? (y/n)\n").lower()

main()