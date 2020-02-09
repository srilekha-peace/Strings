def check_palindrome(string):

    start = 0
    end = len(string) - 1

    while(end > start):
        if string[start] != string[end]:
            print("Not a plaindrome")
            return

        start += 1
        end -= 1
    print("Given string is a palindrome")

if __name__ == '__main__':
    str = "malayalam"
    mutable_list = list(str)
    check_palindrome(mutable_list)
