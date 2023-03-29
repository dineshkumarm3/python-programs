# program to define n number of elements in list
# if the number only perfectly divided by 3, instead of number add fizz
# if the number only perfectly divided by 5, instead of number add buzz
# if the number perfectly divided by 3 and 5, instead of number add fizzbuzz
def fizzBuzz(n):
    answer = list()
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer
print(fizzBuzz(5))