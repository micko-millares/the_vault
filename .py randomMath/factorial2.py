# Takes input from user and calculates the factorial.
def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)  # Recursion


num = int(input("Enter Integer: "))
msgNegative = "Factorial can't be found for negative numbers"
msgZero = "Factorial of 0 = 1"
ans = factorial(num)
if num < 0:
    print(msgNegative)
elif num == 0:
    print(msgZero)
else:
    print(ans)
