# program to print n Tribonacci number
# here we are adding previous 3 numbers to get next number

n = int(input("Enter the no of Tribonacci number you want : "))
n1, n2, n3 = 0, 1, 1
if n > 0:
    if n == 1:
        print(n1)
    elif n == 2:
        print(n2)
    elif n == 3:
        print(n3)
    else:
        print(n1, n2, n3, end=' ')
        for x in range(3, n):
            n1, n2, n3 = n2, n3, n1 + n2 + n3
            print(n3, end=' ')

else:
    print('Invalid input')
