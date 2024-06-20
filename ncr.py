def factorial(num):
    prod = 1
    for i in range(1, num + 1):
        prod = prod * i
    factorial = prod
    print(factorial)
    print(prod)
    n_rfact = prod
    return factorial


print(f"the fu{factorial(4)}")
#ncr
n=5
r=3
# n!/(n-r)!(r!)

prod=1
for i in range(1,n+1):
    prod=prod*i
print(prod)
nfact=prod

prod=1
for i in range(1,n-r+1):
    prod=prod*i
print(prod)
n_rfact=prod

prod=1
for i in range(1,r+1):
    prod=prod*i
print(prod)
rfact=prod

ncr=nfact/(n_rfact)(rfact)
print(f"the result={ncr}")
