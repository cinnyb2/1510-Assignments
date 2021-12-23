import doctest


def caesarcipher(message, encode, shift):
    """

    Return either an encrypted message or a message that is decrypted depending on if you set the encode agrument
    to true or false

    # True encode the cipher and False decodes the cipher

    :param message: str that may be empty
    :param encode: bool (True or False)
    :param shift: positive or negative
    :precondition: message must be a string, encode must be either True or False, and shift must be an integer.
    This program only shifts the number and letter, all special characters will be left as is
    :postcondition: converts the message into a cipher by moving each letter by the specified integer in shift
    :return: string

    >>> caesarcipher('HI',True, 3)
    'KL'

    >>> caesarcipher('123',True, 2)
    '345'

    >>> caesarcipher('123',False, 2)
    '901'

    >>> caesarcipher('a', True, -3)
    'x'

    >>> caesarcipher('a', False, -3)
    'd'

    >>> caesarcipher('0', True, 10)
    '0'

    >>> caesarcipher('!@#$*()', True, 36)
    '!@#$*()'

    >>> caesarcipher('HeLl0 w0R3lD', True, 20)
    'ByFf0 q0L3fX'

    >>> caesarcipher('Xcmdn gjqz8 M88n8 kzvipo WpOOzm XpKn', False, -5)
    'Chris love3 R33s3 peanut BuTTer CuPs'
    """
    if encode is True:
        message = encrypt(message, shift)
        return message
    if encode is False:
        message = decrypt(message, shift)
        return message


def encrypt(plain_message, shift):
    """

    Encrypts plain message by changing each letter to the specified shift

    :param plain_message: str, can be empty
    :param shift: int
    :precondition: plain_message must be a str, and shift must be an int, special characters are not shifted
    :postcondition: correctly encodes plain_message into cipher text by shifting the letter/s and number/s
    by the specified shift/s
    :return: str, can be empty

    >>> encrypt('HI', 3)
    'KL'

    >>> encrypt('123', 2)
    '345'

    >>> encrypt('', 2)
    ''

    >>> encrypt('HeLl0 w0R3lD', 20)
    'ByFf0 q0L3fX'

    >>> encrypt('Chris love3 R33s3 peanut BuTTer CuPs', -5)
    'Xcmdn gjqz8 M88n8 kzvipo WpOOzm XpKn'
    """
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    encrypt_message = ''
    for char in plain_message:
        if char.isalpha():
            if char in alphabet_upper:
                index = (alphabet_upper.find(char) + shift) % len(alphabet_upper)
                encrypt_message += alphabet_upper[index]
            elif char in alphabet_lower:
                index = (alphabet_lower.find(char) + shift) % len(alphabet_lower)
                encrypt_message += alphabet_lower[index]
        elif char.isnumeric():
            if char in number:
                index = (number.find(char) + shift) % len(number)
                encrypt_message += number[index]
        else:
            encrypt_message += char
    return encrypt_message


def decrypt(encrypt_message, shift):
    """
    Decode the encrypted message into plain message

    :param encrypt_message: str, can be empty
    :param shift: positive or negative int
    :precondition: encrypt_message must be a str, and shift must be an int, special characters are not shifted
    :postcondition: corrrectly decode encrypt_message into plain text by shifting the letter/s and number/s by the
    specified shift/s
    :return: str, can be empty

    >>> decrypt('', 2)
    ''

    >>> decrypt('KL', 3)
    'HI'

    >>> decrypt('345', 2)
    '123'

    >>> decrypt('ByFf0 q0L3fX', 20)
    'HeLl0 w0R3lD'

    # Test to see if argument can take a negative integar
    >>> decrypt('Xcmdn gjqz8 M88n8 kzvipo WpOOzm XpKn', -5)
    'Chris love3 R33s3 peanut BuTTer CuPs'
    """
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    decrypt_message = ''

    for char in encrypt_message:
        if char.isalpha():
            if char in alphabet_upper:
                index = (alphabet_upper.find(char) - shift) % len(alphabet_upper)
                decrypt_message += alphabet_upper[index]
            elif char in alphabet_lower:
                index = (alphabet_lower.find(char) - shift) % len(alphabet_lower)
                decrypt_message += alphabet_lower[index]

        elif char.isnumeric():
            if char in number:
                index = (number.find(char) - shift) % len(number)
                decrypt_message += number[index]
        else:
            decrypt_message += char
    return decrypt_message


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
