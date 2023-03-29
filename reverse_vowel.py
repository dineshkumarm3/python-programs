# Reverse only the vowel letters

s = input("Enter you string here: ")
L = []  # empty list to store vowels
vowels = 'aeiuoAEIOU'
for i in s:
    if i in vowels:
        L.append(i)
newstr = ""
for j in s:
    if j in vowels:
        newstr += L[-1]
        L.pop(-1)
    else:
        newstr += j
print(newstr)
