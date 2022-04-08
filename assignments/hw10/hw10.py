def fibonacci(n):
    fib_list = []
    first = 0
    second = 1
    index = n - 1
    sequencing = True
    if n <= 1:
        return None
    else:
        while sequencing:
            if len(fib_list) < n:
                first, second = second, first + second
                fib_list.append(first)
            else:
                break
        return fib_list[index]


def double_investment(principle, rate):
    acc = 0
    compound = principle
    while compound < (2 * principle):
        compound = compound * (1 + rate)
        acc += 1
    return acc


def syracuse(n):
    my_list = []
    while n > 1:
        my_list.append(int(n))
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(n * 3 + 1)
    my_list.append(1)
    return my_list


def goldbach(n):
    my_list = []
    if n % 2 != 0:
        return None
    elif n % 2 == 0:
        prime_1 = int(n / 2) + 1
        prime_2 = int(n / 2) - 1
        if prime_1 % 2 != 0:
            my_list.append(prime_1)
        else:
            my_list.append(prime_1 + 1)
        if prime_2 % 2 != 0:
            my_list.append(prime_2)
        else:
            my_list.append(prime_2 - 1)
    return my_list
        # if prime_1 != 0 and prime_2 != 0:




if __name__ == "__main__":
    # print(fibonacci(9))
    # print(double_investment(10000, .05))
    # print(syracuse(5))
    print(goldbach(3614))
