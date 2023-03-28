# Add 1 to the concatenation of list numbers and then divide them as separate element and store in list
Input = [1, 2, 9] #Input = eval(input('Enter your list here'))
output = []
Str = ''
for i in Input:
    Str += str(i)
Sumstr = str(int(Str) + 1)
for v in Sumstr:
    output.append(int(v))
print(output)
