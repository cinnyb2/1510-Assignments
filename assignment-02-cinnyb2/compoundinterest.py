import doctest


def compoundinterest(principle_amount, annual_interest_rate, number_per_year_compound, years_in_account):
    """
    Returns the projected amount of money in the user's account according to their given arguments

    :param principle_amount: positive or negative float
    :param annual_interest_rate: positive or negative float
    :param number_per_year_compound: int > 0
    :param years_in_account: a float > 0
    :precondition: principle_amount and annual_interest_rate must be > 0
    :postcondition: calculates the correct projected amount of money in the account with
    given arguments
    :return: float

    >>> compoundinterest(1000.0, 0.1, 2, 2.0)
    1215.5062500000001

    # Test with negative float for annual_interest_rate
    >>> compoundinterest(1000.0, -0.1, 2, 2.0)
    814.5062499999999

    # Test with negative float for principle_amount
    >>> compoundinterest(-1023, 0.5, 3, 1.0)
    -1624.4861111111113

    # Test to see if principle_amount and annual_interest_rate can take 0 as an argument
    >>> compoundinterest(0.0, 0.0, 1, 1)
    0.0
    """
    total_money = principle_amount * (1 + annual_interest_rate / number_per_year_compound) ** (
            number_per_year_compound * years_in_account)
    return total_money


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
