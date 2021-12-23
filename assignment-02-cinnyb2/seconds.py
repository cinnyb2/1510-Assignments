import doctest


def second(weeks, days, hours, minutes):
    """
    Return the total number of seconds represented by the given arguments.

    Positive arguments should be added to the total, and negative arguments
    should be deducted from the total

    :param weeks: positive or negative int
    :param days: positive or negative int
    :param hours: positive or negative int
    :param minutes: positive or negative int
    :precondition: all parameters either a negative or positive int
    :postcondition: calculates the correct number of seconds in given arguments
    :return: int either positive or negative

    # Test to see
    >>> second(-1, 0, 0, -4)
    -605040

    >>> second(1, 1, 1, 1)
    694860

    # Test to see if the function will take all 0s are arguments
    >>> second(0, 0, 0, 0)
    0

    # Test to see if the function will work with float numbers
    >>> second(0, 1, 0, 29)
    88140
    """
    total_seconds = (weeks * 604800) + (days * 86400) + (hours * 3600) + (minutes * 60)
    return int(total_seconds)


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()

