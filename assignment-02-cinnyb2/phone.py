import doctest


def phone(alphanumeric_phone_number):
    """
    Converts a string that may have alphanumerics into a phone number with only numbers

    :param alphanumeric_phone_number: string of numbers separated by dash
    :precondition: needs to be provided in format XXX-XXX-XXXX, where x is alphanumeric
    :postcondition: correctly translate the letters into their corresponding numbers
    :return: string

    >>> phone('555-PHO-KING')
    '555-746-5464'

    >>> phone('000-000-0000')
    '000-000-0000'

    >>> phone('ACE-THE-TEST')
    '223-843-8378'

    >>> phone('YOU-217-9E2')
    '968-217-932'

    >>> phone('555-gET-fOoD')
    '555-438-3663'
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    number = '22233344455566677778889999'
    dict_converter = dict(zip(alphabet, number))

    phone_number = ''
    for alphabet in alphanumeric_phone_number.lower():
        if alphabet.isalpha():
            phone_number += dict_converter[alphabet]
        else:
            phone_number += alphabet

    return phone_number


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
