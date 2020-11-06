def staircase(n):
    if n <= 0 or n > 100:
        print(ValueError('The input must be in (0,100]'))
    else:
        for i in range(n):
            print((n - i)*' ' + (i + 1) * '#')


staircase(6)
