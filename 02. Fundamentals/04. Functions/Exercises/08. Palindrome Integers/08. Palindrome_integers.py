def palindrome_check(list_num):
    for i in list_num:
        if i == i[::-1]: # reversva stringa
            print("True")
        else:
            print("False")


number = list(map(str, input().split(", ")))
palindrome_check(number)
