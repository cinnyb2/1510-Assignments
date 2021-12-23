import doctest


def eratosthenes(upper_bound):
    """
    Returns the prime numbers within the range of [0, upper_bound]

    :param upper_bound: positive int
    :precondition: upper_bound cannot be a negative number and it cannot be a float
    :postcondition: correctly returns all the prime number within the range of [0, to the specified upper_bound], and is
    inclusive of upper_bound
    :return: list

    >>> eratosthenes(2)
    [2]

    >>> eratosthenes(0)
    []

    >>> eratosthenes(3)
    [2, 3]

    >>> eratosthenes(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    >>> eratosthenes(31)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    >>> eratosthenes(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    """
    lst_of_all_numbers = []
    for item in range(upper_bound + 1):
        lst_of_all_numbers.append(item)

    for number in range(2, int(upper_bound ** 0.5) + 1):
        for multiple in range(number * 2, upper_bound + 1, number):
            lst_of_all_numbers[multiple] = 0

    if len(lst_of_all_numbers) >= 2:
        lst_of_all_numbers[1] = 0

    primes = []
    for number in lst_of_all_numbers:
        if number != 0:
            primes.append(number)

    return primes


def main():
    """
    Drive the program.
    """

    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
