class A:
    a=10
class B(A):
    b=9
    c=a*b

ob=B

print(ob.c)