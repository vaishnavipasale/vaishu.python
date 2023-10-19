Calculate compound interest.
p = float (input("enter the principal"))
r = float (input("enter the rate"))
t = float (input("enter the time"))
print(f"principal is {p}")
print(f"rate is {r}")
print(f"time is {t}")
interst = p * (( 1 + r / 100) ** t) 
print(f"compound interst is {interst}")
