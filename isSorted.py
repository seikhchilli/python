def isSorted(list1):
    list2 = [] + list1
    list2.sort()
    if list2 == list1 :
        return True
    else:
        return False


def main():
    list1 = []
    print("Enter list: ")
    for i in range(11):
        x = eval(input())
        list1.append(x)
    
    if isSorted(list1):
        print("The list is already sorted.")
    
    else:
        print("The list is not sorted.")

main()
    
