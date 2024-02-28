#!/usr/bin/python3
""" Making changes """


def makeChange(coins, total):
    """ To Generate changes needed to reach total

    Args:
        coins ([List]): [The list of Coins available]
        total ([int]): [The total amount needed]
    """
    if total <= 0:
        return 0
    check = 0
    temp = 0
    coins.sort(reverse=True)
    for j in coins:
        while check < total:
            check += j
            temp += 1
        if check == total:
            return temp
        check -= j
        temp -= 1
    return -1
