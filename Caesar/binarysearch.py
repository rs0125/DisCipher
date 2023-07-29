def wordcount(arr):
    temp = 0
    arr = arr.split()
    for i in arr:
        if i.isalpha():
            temp += 1
    return temp


def search(arr, x):
    if arr.find(x) != -1:
        return True
