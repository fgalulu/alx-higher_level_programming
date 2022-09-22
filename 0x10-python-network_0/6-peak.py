#!/usr/bin/python3
# function that finds a peak in unsorted arrays.

def find_peak(list_of_integers):
    """find largest value in unsorted array"""

   if list_of_integers:
       list_of_integers.sort()
       return list_of_integers[-1]
   else:
       return None
