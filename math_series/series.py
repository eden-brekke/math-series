def fibonacci(n):
    """
     this function will require a value(n) 0 at 0 and 1 at 1 is hardcoded into fibonacci
     then if its not less than or equal to 1 it can return a recursion method
     where the recursion will call the function with n -1 summed with the function with n-2
    """
    if n <= 1:
        if n == 0:
            return 0
        else:
            return 1
    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
     this function will require a value(n) 0 at 2 and 1 at 1 is hardcoded into lucas
     then if its not less than or equal to 1 it can return a recursion method
    where the recursion will call the function with n -1 summed with the function with n-2
    """
    if n <= 1:
        if n == 0:
            return 2
        else:
            return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n,f=0,s=1):
    """
        this function will check if your input are either fibonacci or lucas or if it will be the sum of both.
    """
    if n == 0:
        return f
    elif n == 1:
        return s
    else:
        return sum_series(n-1, f, s) + sum_series(n-2, f, s)

