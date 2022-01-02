def main():
    lis = []
    print("Enter some number between 1 and 100: ")
    for i in range(10):
        x = eval(input())
        lis.append(x)
    
    while len(lis) != 0:
        i = lis[0]
        count = lis.count(i)
        if count > 1:
            print(i, "occured ", count, " times")
        else:
            print(i, " occured ", count, " time")
        
        while i in lis:
            lis.remove(i)
    
main()