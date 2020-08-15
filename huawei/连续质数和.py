import math
import numpy as np


def get_prime(num3):
    result = []
    for i in range(2, num3 + 1):
        if prime(i):
            result.append(i)
    return result


def prime(num2):
    for i in range(2, int(math.sqrt(num2) + 1)):
        if num2 % i == 0:
            return False
    return True


def run(num1):
    check = 0
    prime_list = get_prime(num1)
    c1 = 0
    c2 = 1
    while c1<len(prime_list):
        # print(str(c1) + ' ' + str(c2))
        if np.sum(prime_list[c1:c2]) == num1:
            check += 1
            c1 += 1
            c2 += 1
        elif np.sum(prime_list[c1:c2]) < num1:
            c2 += 1
            if c2 > len(prime_list):
                break
            else:
                continue
        elif np.sum(prime_list[c1:c2]) > num1:
            c1 += 1
            continue
    return check


if __name__ == "__main__":
    num = int(input())
    print(run(num))
    # for i in range(2,10001):
    #     print(str(i) + ' ' + str(run(i)))