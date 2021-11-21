"""
Given an array of sorted numbers, remove all duplicates from it.
You should not use any extra space; after removing the duplicates
in-place return the length of the subarray that has no duplicate in it.

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""


def remove_duplicates(arr):
    if not arr:
        return 0
    left = 0
    len_sub = 1
    for right in range(1, len(arr)):
        if arr[right] != arr[left]:
            len_sub += 1
            left = right
    return len_sub


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()