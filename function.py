# defining a function
def print_text():
	print("Hello World!")

# calling a function
print_text()


# Function with arguments
def print_values(a,b):
	print("The values of a and b are",a,"and",b)

print_values(10,20)


# Function with default arguments
def print_text(a,b=5):
	print("The values of a and b are",a,"and",b)

print_text(10)
print_text(10,15) # this will override the default value of b


# Function Call - Keyword Arguments
def print_values(a,b):
	print("The values of a and b are",a,"and",b)

print_values(b=20,a=10)


# Recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

fact = factorial(5)
print("Result of factorial", fact)
