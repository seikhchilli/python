def bubbleSort(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - i - 1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]

def main():
    print("Enter ten numbers: ")
    list1 = []
    for i in range(10):
        x = eval(input())
        list1.append(x)
    
    bubbleSort(list1)
    
    print("Sorted list: ", list1)

main()




