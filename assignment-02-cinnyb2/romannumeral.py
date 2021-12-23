import doctest


def romannumeral(positive_int):
    """
    Return the Roman numeral as a string that does not contain any leading, inner, or trailing
    whitespace

    :precondition: positive_int must be in the range of between [1, 1_000], and must be a positive int
    :postcondition: correctly converts the positive_int into the roman numeral equivalent with no leading,
    inner, or trailing whitespace
    :param positive_int: a positive int
    :return: string

    >>> romannumeral(3)
    'III'

    >>> romannumeral(5)
    'V'

    >>> romannumeral(6)
    'VI'

    >>> romannumeral(738)
    'DCCXXXVIII'

    >>> romannumeral(1000)
    'M'

    >>> romannumeral(999)
    'CMXCIX'
    """

    roman_numerals_dict = {'M': 1000,
                           'CM': 900,
                           'D': 500,
                           'CD': 400,
                           'C': 100,
                           'XC': 90,
                           'L': 50,
                           'XL': 40,
                           'X': 10,
                           'IX': 9,
                           'V': 5,
                           'IV': 4,
                           'I': 1,
                           }

    roman_number = ""
    for key, value in roman_numerals_dict.items():
        counter = int(positive_int / value)
        roman_number += key * counter
        positive_int -= value * counter
    return roman_number


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()