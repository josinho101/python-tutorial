def my_function():
    print("from my function")

my_function()

#passing arguments to function
def greet(name):
    print("hello " + name)

greet("Joseph")
greet("Lizy")

#named arguments
def get_fullname(firstname, lastname):
    print(firstname + " " + lastname)

get_fullname(lastname = "J", firstname = "Joseph")

#default arguments
def sum(a = 2, b = 2):
    print(a + b)

sum(5, 5) #with params
sum() #with no params. will use default values for params

#return statement
def substract(a, b):
    return a - b;

print(substract(3, 2))
