# Check if given string can be rearranged to form a palindrome
def checkforpali(strr):
    list1 = []
    for i in range(len(strr)):
        if strr[i] in list1:
            list1.remove(strr[i])
        else:
            list1.append(strr[i])
    if (len(strr) % 2 == 0 and len(list1) == 0 or
            (len(strr) % 2 == 1 and len(list1) == 1)):
        return True
    return False


user_input = input("Enter your string here to check whether palindrome can be constructed:")
if checkforpali(user_input):
    print("palindrome can be constructed")
else:
    print("Palindrome cannot be constructed")

