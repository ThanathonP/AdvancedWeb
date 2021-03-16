def add(x,y):
    """Add Function"""
    return x+y

def subtract(x,y):
    """subtract Function"""
    return x-y

def multiply(x,y):
    """multiply Function"""
    return x*y

def divide(x,y):
    """divide Function"""
    if y==0:
        raise ValueError('Can not divide by zero!')
    return x/y


print (add(10,5))
print (subtract(10,5))
print (multiply(10,5))
print (divide(11,5))