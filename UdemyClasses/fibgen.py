# A generator function for Fibonacci numbers

def fibonacci():
    """fibonacci generator
    Returns
    -------
        current get the value zero plus 1, and previous get the old value of
        current, which the first time it runs is zero. Next time around
        current becomes 1 plus zero, so one again, in other words,
        and previous this time, becomes one. And the third time around,
        current becomes two and previous becomes one. Then we get three and
        two, followed by five and three and so on.
    Yields
    ------
        _description_
    """

    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()
for i in range(21):
    print(i, next(fib))
