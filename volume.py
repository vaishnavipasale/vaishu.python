Calculate the volume of different 3D shapes (cube, sphere, cylinder).
length = float (input("Enter a length"))
breadth = float (input("Enter a breadth"))
height = float (input("Enter a height"))
r = float (input("Enter a radius"))
v = length * breadth * height
print(f"volume of cube is : {v}")
v1 = 4/3 * 3.14 * r * r * r
print(f"volume of sphere is : {v1}")
v2 = 3.14 * r * r * height
print(f"volume of cylinder is : {v2}")
