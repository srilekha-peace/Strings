def check_anagram(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    if l1 != l2:
        print("Not an anagram")
        return

    count1 = count2 = 0

    for i in range(0, l1):
        count1 = count1 + ord(s1[i])

    for j in range(0,l2):
        count2 = count2 + ord(s2[j])

    if count1 == count2:
        print("Both strings are anagram to each other")
    else:
        print("Not an anagram")

    return

if __name__ == '__main__':
    str1 = "silent"
    str2 = "listen"
    check_anagram(list(str1), list(str2))
