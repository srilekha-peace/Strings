ascii_chars = 256

def remove_duplicates(str):
    temp = " "
    res_index = 0
    index = 0
    hash_map = [0] * ascii_chars
    mutable_list = list(str)

    while index != len(mutable_list):
        temp = mutable_list[index]
        if (hash_map[ord(temp)]) == 0:
            (hash_map[ord(temp)]) = 1
            mutable_list[res_index] = temp
            res_index += 1

        index += 1

    return "".join(mutable_list[:res_index])


if __name__ == '__main__':
    str = "abacbdce"
    print(remove_duplicates(str))
