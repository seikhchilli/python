def CheckSSN(ssn):
    if len(ssn) != 9:
        return False

    if not ssn.isdigit():
        return False
        
    return True

def main():
    ssn = input("Enter your Social Security Number: ")

    if CheckSSN(ssn):
        print("Valid SSN") 
    else:
        print("Invalid SSN")

main()