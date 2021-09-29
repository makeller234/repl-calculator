"""Functions for common math operations."""
nums=[]

def add(nums):
    """Return the sum of the two inputs."""
    sum =0
    for i in nums:
        sum += i
        
    return (sum)
#testing add function
#print(add([1,2,3]))

def subtract(nums):
    """Return the second number subtracted from the first."""
    result=nums[0]
    i = 1
    while i <= (len(nums)-1):
        result= result - nums[i]
        i+=1
        
    return (result)
#print(subtract([10,5,3]))

def multiply(num1, num2):
    """Multiply the two inputs together."""
    return (num1*num2)


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    return (num1/num2)

def square(num1):
    """Return the square of the input."""
    return (num1 ** 2)

def cube(num1):
    """Return the cube of the input."""
    return (num1 ** 3)


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return (num1 ** num2)

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return (num1%num2)


def add_mult(num1, num2, num3):
    """Get the sum of num1 and num2, then multiply sum with num3."""
    return ((num1 + num2) *num3)

def add_cubes(num1, num2):
    """Add the cubes of num1 and num2."""

    return ((num1**3) + (num2**3))