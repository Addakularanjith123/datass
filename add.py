class A:
    a = 10

class B(A):
    b = 9
    c = A.a * b  # Directly using inherited attribute a

# Creating an instance of the derived class
ob = B()

# Printing the result
print(ob.c)  # Output should be 90
