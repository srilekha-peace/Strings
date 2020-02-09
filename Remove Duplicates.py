def remove_duplicates(s, n):
    res = 0

    for i in range(0, n):
        for j in range(0, i+1):
            if s[i] == s[j]:
                break
        if(j == i):
            s[res] = s[i]
            res += 1

    return "".join(s[:res])

if __name__ == '__main__':
    str = "abacbdce"
    s = list(str)
    n = len(s)
    print(remove_duplicates(s, n))

