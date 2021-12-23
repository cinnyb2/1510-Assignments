import calendar
import doctest


def leapyears(lower_bound, upper_bound):
    """
    Returns how many leap years there will be in range of [lower_bound, upper_bound]

    :param lower_bound: int
    :param upper_bound: int
    :precondition: lower_bound <= upper_bound and both value must be greater than 0
    :postcondition: correctly calculates the number of leap years within range specified
    :return: int

    >>> leapyears(2000, 2015)
    4

    # Test to see if it is inclusive of upper_bound
    >>> leapyears(2000, 2016)
    5

    # Test to see if it would count year 0 as leap year (which it is),
    >>> leapyears(0, 1)
    1

    #Test to see if function will correct answer for lower_bound if both arguments are the same
    >>> leapyears(2000, 2000)
    1
    """
    exclusive = calendar.leapdays(lower_bound, upper_bound)
    inclusive_upper = calendar.isleap(upper_bound)
    if inclusive_upper is True:
        return exclusive + 1
    else:
        return exclusive


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
