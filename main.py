import random

x = ["lol", "rofl", "lmao"]
y = x
a,b,c = x
print(a , b, c)
print(x)

def myfunction():
    global a
    a = "hello"
    print(a)

myfunction()
print(a)

y[1]= "changed"
print(y)
print(x)

for i in range(len(x)):
    cont = input("Do you want to print the next item? (y/n): ")
    if cont == "y":
        print(x[i])
    else:
        break
print(type(x))
x = 9j

print(type(x))

for i in range(10):
    print(random.randint(1, 10))