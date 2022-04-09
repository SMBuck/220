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
    # my_list = []
    # prime_1 = int(n / 2)
    # prime_2 = int(n / 2)
    # if n % 2 != 0:
    #     return None
    # elif prime_1 % 2 == 0:
    #     prime_1 += 1
    #     my_list.append(prime_1)
    #     if prime_1 % 2 == 0:
    #         my_list.remove(prime_1)
    #         prime_1 += 1
    #         my_list.append(prime_1)
    # elif prime_2 % 2 == 0:
    #     prime_2 -= 1
    #     my_list.append(prime_1)
    #     if prime_2 % 2 == 0:
    #         prime_2 -= 1
    #         my_list = my_list + [prime_2]
    # return my_list
    my_list = []
    my_prime_list = []
    i = 0
    while i < n:
        i += 1
        my_list.append(i)
        if n % i == 0 or i % 2 == 0:
            my_list.remove(i)
    diff = n - my_list[0]
    my_prime_list.append(my_list[0])
    if diff in my_list:
        my_prime_list.append(diff)
    elif n % 2 != 0:
        return None
    return my_prime_list


if __name__ == "__main__":
    # print(fibonacci(9))
    # print(double_investment(10000, .05))
    # print(syracuse(5))
    print(goldbach(10))
