import doctest


def dijkstra(random_list_of_strings):
    """
    Sort a random list of strings into the colours of the dutch national flag (red, white, blue)

    The dutch national flag is in the following order 'red', 'white', 'blue'
    :param random_list_of_strings: non-empty list of strings that contain "red", "white", and "blue"

    >>> flag = ['white', 'blue', 'red']
    >>> dijkstra(flag)
    >>> print(flag)
    ['red', 'white', 'blue']

    >>> flag = ['white', 'red', 'blue', 'white']
    >>> dijkstra(flag)
    >>> print(flag)
    ['red', 'white', 'white', 'blue']

    >>> flag = []
    >>> dijkstra(flag)
    >>> print(flag)
    []

    >>> flag = ['white', 'blue', 'blue', 'red', 'white', 'red', 'white']
    >>> dijkstra(flag)
    >>> print(flag)
    ['red', 'red', 'white', 'white', 'white', 'blue', 'blue']

    >>> flag = ['red', 'white', 'blue']
    >>> dijkstra(flag)
    >>> print(flag)
    ['red', 'white', 'blue']

    # test to see if it works for only a list of only blue
    >>> flag = ['blue', 'blue', 'blue']
    >>> dijkstra(flag)
    >>> print(flag)
    ['blue', 'blue', 'blue']
    """

    sorted_list = sorted(random_list_of_strings[:])
    for item in sorted_list:
        if item == 'blue' in sorted_list:
            sorted_list.remove(item)
            sorted_list.insert(len(sorted_list), item)

    random_list_of_strings.clear()
    random_list_of_strings.extend(sorted_list)


def main():
    """
    Drive the program.
    """
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
