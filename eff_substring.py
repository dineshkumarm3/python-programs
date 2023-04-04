# Optimal Partition of String
# Given a string s, partition the string into one or more substrings
# such that the characters in each substring are unique.
# That is, no letter appears in a single substring more than once.

def partitionstring(s):
    L = list()
    ns = ''
    for i in range(len(s)):
        if s[i] not in ns:
            ns += s[i]
        else:
            L.append(ns)
            ns = ''
            ns += s[i]
    L.append(ns)
    return L


# driver code
s = "abacaba"
output=partitionstring(s)
for x in output:
    print(x)
