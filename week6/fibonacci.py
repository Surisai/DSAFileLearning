
# Function 3: fibonacci
def fibonacci(n):
    if n == 0:
        print("fibonacci(0) = 0")
        return 0
    elif n == 1:
        print("fibonacci(1) = 1")
        return 1

    a, b = 0, 1
    print(f"Start: a = {a}, b = {b}")

    for i in range(2, n + 1):
        a, b = b, a + b
        print(f"Step {i}: a = {a}, b = {b}")

    print(f"fibonacci({n}) = {b}")
    return b


fibonacci(6)



    