def main():
    s = input("Enter a string: ").strip()

    if isPalindrome(s):
        print("Yes it is a palindrome.\n")
    else:
        print("NO, it's not a palindrome.\n")



def isPalindrome(s):
    low = 0;

    high = len(s) - 1;

    while(low < high):
        if s[low] != s[high]:
            return False

        high -= 1
        low += 1
    return True

main()
