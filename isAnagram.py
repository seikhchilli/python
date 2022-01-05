def isAnagram(list1, list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

def main():
    string1 = input()
    string2 = input()
    list1 = []
    list2 = []
    for i in string1:
        list1.append(i)
    
    for i in string2:
        list2.append(i)

    if isAnagram(list1, list2):
        print("is an Anagram")
    else:
        print("is not an Anagram")

main()