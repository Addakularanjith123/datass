from timeit import default_timer
b=["a"]*10
start=default_timer()
res=""
for i in b:
    res=res+i
stop=default_timer()
print(f"{res}")
print(f"time taken for loop is {stop-start}")

