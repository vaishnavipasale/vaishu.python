Calculate the area of a triangle using Heron's formula.
a = float(input("Enter value of a"))
b = float(input("Enter value of b"))
c = float(input("Enter value of c"))
s = (a + b + c) / 2
print(f"semiperimeter is {s}")
area = (s * (s-a) *(s-b) * (s-c)) ** 0.5
print(f"area of triangle is {area}")
