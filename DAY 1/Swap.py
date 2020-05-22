x = int(input("Enter first variable : "))
y = int(input("Enter second variable : "))

print("Before swapping : x =",x," , y =",y)

x = x + y
y = x - y
x = x - y

print("After swapping : x =",x," , y =",y)
