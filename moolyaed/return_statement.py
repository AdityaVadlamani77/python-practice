def add(a, b, c):  # optional argument
    '''

    :param a:
    :param b:
    :param c:
    :return:
    '''

    return a**2


z = add(b=1, a=2, c=3)
print(z)

# positional argument
# keyword argument
# required argument
# optional argument
def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

print([fibonacci_of(0)])