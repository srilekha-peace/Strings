def count_vowels(string):
    count = 0
    for i in range(len(string)):
        if is_vowels(string[i]):
            count += 1
    return count

def is_vowels(ch):
    return ch.upper() in ['A', 'E', 'I', 'O','U']

if __name__ == '__main__':
    str = "Python Programming"
    print(count_vowels(str))
