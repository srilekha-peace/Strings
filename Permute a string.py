def permute_str(a,start,end):
    if start == end:
        print("".join(a))

    for i in range(start, end+1):
        a[start],a[i] = a[i],a[start]
        permute_str(a, start+1,end)
        a[start],a[i] = a[i],a[start]

if __name__ == '__main__':
    str = "ABC"
    mutable_list = list(str)
    n = len(str)
    permute_str(mutable_list,0,n-1)
