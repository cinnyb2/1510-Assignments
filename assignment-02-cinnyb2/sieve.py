# import doctest
# import math
# import itertools as it
#
#
# def eratosthenes(upper_bound):
#     """
#     Returns the prime numbers within the range of [0, upper_bound]
#
#     :param upper_bound: positive int
#     :precondition:
#     :postcondition:
#     :return: list
#
#     >>> eratosthenes(2)
#     [2]
#
#     >>> eratosthenes(0)
#     []
#
#     >>> eratosthenes(3)
#     [2, 3]
#
#     >>> eratosthenes(30)
#     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#
#     >>> eratosthenes(31)
#     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
#
#     >>> eratosthenes(100)
#     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#     """
#     prime_number = []
#
#     if upper_bound < 2:
#         return []
#
#     if upper_bound >= 2:
#         for item in range(2, (upper_bound + 1)):
#             if prime_checker(item) is True:
#                 prime_number.append(item)
#     return prime_number
#
#
# def prime_checker(number):
#     """
#     Check to see if a number is a prime number or not
#
#     :param number: a positive int
#     :return: bool
#
#     >>> prime_checker(0)
#     False
#     >>> prime_checker(1)
#     False
#
#     >>> prime_checker(2)
#     True
#
#     >>> prime_checker(9)
#     False
#
#     >>> prime_checker(97)
#     True
#
#     >>> prime_checker(47)
#     True
#
#     >>> prime_checker(1217)
#     True
#
#     >>> prime_checker(855)
#     False
#
#     >>> prime_checker(26)
#     False
#     """
#     if number < 2:
#         return False
#
#     if number == 2:
#         return True
#
#     if number == 3:
#         return True
#
#     for item in it.islice(it.count(2), math.isqrt(number) + 1):
#         if number % item == 0:
#             return False
#
#     return True


# def get_login_name(first, last, id_number):
#     set1 = first[0:3]
#     set2 = last[0:3]
#     set3 = id_number[-2:]
#     login_name = f"{set2}{set1}{set3}"
#     return login_name
#
#
# def main():
#     id = get_login_name("Cornelius", "Overlander", "A00123579")
#     print(id)
#
#
# if __name__ == "__main__":
#     main()

# letters = list("Hello world")
# my_list = letters[3:8]
# print(my_list)

# def ignore_letter_prefix(a_student_number):
#     return int(a_student_number[1:])
#
# students = ["A0100", "A0050", "A0075"]
# sorted_students = sorted(students, key=ignore_letter_prefix)
# print(sorted_students)
#
# print(format(0.2, '%'))
# print(format(0.2, '.0%'))

x = 6


def f():
    print("Within f: x =", x)
    x = 12
    print("Within f: x=", x)

print("Before f: x=", x)
f()
print("After f: x=", x)

