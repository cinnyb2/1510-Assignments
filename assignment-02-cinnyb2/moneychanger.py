import doctest


def moneychanger(cash_amount):
    """
    Return a list of how many of each denomination are required

    The denominations are in the following order 100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05

    :param cash_amount: float
    :precondition: cash_amount cannot be negative and must be a float
    :postcondition: correctly calculate a list of all the denomination in the order specified above, all cents >= 0.03
    will be rounded to 0.05, since pennies do no exist in canada.
    :return: list that tell how many of each denomination are required

    >>> moneychanger(66.53)
    [0, 1, 0, 1, 1, 0, 1, 2, 0, 1]

    >>> moneychanger(0)
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    >>> moneychanger(123210.07)
    [1232, 0, 0, 1, 0, 0, 0, 0, 0, 1]

    # Test to see if it works for 0.03
    >>> moneychanger(6.33)
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 2]

    # Test at least one of each denomination
    >>> moneychanger(188.74)
    [1, 1, 1, 1, 1, 1, 1, 2, 2, 1]

    >>> moneychanger(88.88)
    [0, 1, 1, 1, 1, 1, 1, 3, 1, 0]
    """
    denominations_list = [100, 50, 20, 10, 5, 2, 1, 0.25, 0.10, 0.05]
    change = []

    for denom in denominations_list:
        change.append(int(cash_amount // denom))
        cash_amount = cash_amount % denom

    if cash_amount >= 0.03:
        change[-1] += 1

    return change


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
