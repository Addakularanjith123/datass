def factorial(num):
    prod = 1
    for i in range(1, num+ 1):
        prod = prod * i
    factorial=prod
    print(factorial)
    print(prod)
    n_rfact = prod
    return factorial
print(f"the fuction{factorial(4)}")