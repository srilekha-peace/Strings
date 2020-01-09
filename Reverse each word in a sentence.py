def reverse_func(str):
    words = str.split(" ")
    print(words) #['Dont', 'waste', 'time']

    newWords = [word[::-1] for word in words]
    print(newWords) # ['tnoD', 'etsaw', 'emit']

    result = " ".join(newWords)
    print(result) # tnoD etsaw emit

if __name__ == '__main__':
    string = "Dont waste time"
    reverse_func(string)
