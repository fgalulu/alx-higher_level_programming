#!/usr/bin/python3
# function that finds a peak in unsorted arrays.


def find_peak(list_of_integers):
    """find largest value in unsorted array"""
    if list_of_integers:
        largest = list_of_integers[0]
        for x in list_of_integers:
            if x > largest:
                largest = x

        return largest
    else:
        return None
