import random


def lottery():
    """
    Generate a random list of 6 numbers in the range of [1, 49] sorted from lowest to highest

    :precondition: must be positive int in range of [1, 49]
    :postcondition: generate a random list of 6 numbers in the range of [1,49] sorted from lowest to highest
    :return: list
    """
    return sorted(random.sample(range(1, 49), 6))
