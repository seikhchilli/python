s1 = input("Enter string: ").strip()
s2 = input("Enter substring to be searched: ").strip()

if s2 in s1:
    print("Yes " + s2 + " is a part of " + s1 + "\n")
else:
    print("No, " + s2 + " is not a part of " + s1 + "\n")

