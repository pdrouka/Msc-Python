import time

# nice work, change the name


def fibo1(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fibo1(n-1) + fibo1(n-2)


def fibo2(n):

    if n == 1 or n == 2:
        return 1
    else:

        f2 = 1
        f1 = 1
        for i in range(n-2):
            temp = f1
            f1 = f1 + f2
            f2 = temp

    return f1


n = input('Dotse n : ')
#start = time.time()
#F1n = fibo1(n)
end = time.time()
F2n = fibo2(n)
end2 = time.time()
print 'time1 = %s' % (end2 - end)
# print 'F_%s = %s'%( n,F2n)
