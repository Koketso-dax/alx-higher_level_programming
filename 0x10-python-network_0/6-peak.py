#!/usr/bin/python3
"""
Peak number module
"""


def find_peak(list_of_int):
    """
    Finds a peak in a list of unsorted integers.
    """
    if not list_of_int:
        return None

    m_index = len(list_of_int) // 2
    m_element = list_of_int[m_index]

    if (m_index == 0 or _element >= list_of_int[m_index - 1]) and \
       (m_index == len(list_of_int) - 1
         or m_element >= list_of_int[m_index + 1]):
        return m_element
    elif m_index > 0 and list_of_int[m_index - 1] > m_element:
        return find_peak(list_of_int[:m_index])
    else:
        return find_peak(list_of_int[m_index + 1:])
