# program to find the largest sequence of alphabets from given string

# s = "abcdtuvwxyz"  // hard code input for testing
s = input("Enter your string here:")
left = 0
right = 1
newlist = []
newstring = ''
while right < len(s):
    if (ord(s[right]) - ord(s[left])) == 1:
        newstring += s[left]
    else:
        newstring += s[left]
        newlist.append(newstring)
        newstring = ''
    left += 1
    right += 1
newstring += s[-1]
newlist.append(newstring)
Max = max(newlist, key=len)
print(Max)
