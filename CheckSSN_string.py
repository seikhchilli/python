def CheckSSN(ssn):
    if len(ssn) != 9:
        return False

    for i in ssn:
        if(i >= '0' and i <= '9'):
            continue
        else:
            return False
        
    return True

def main():
    ssn = input("Enter your Social Security Number: ")

    if CheckSSN(ssn):
        print("Valid SSN")
    else:
        print("Invalid SSN")

main()