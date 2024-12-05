from random import random


def random_list(length=1):
    """Create a list of random numbers.

    The numbers will be floats between 0 and 1.

    Parameters
    ----------
    length : int
      The length of the list to create.

    Returns
    -------
    list of float
      The list of random numbers.

    Examples
    --------
    >>> random_list(3)
    """

    return [random() for _ in range(length)]
