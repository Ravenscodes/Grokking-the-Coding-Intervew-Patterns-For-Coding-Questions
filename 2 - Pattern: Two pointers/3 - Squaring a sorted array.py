"""
Given a sorted array, create a new array containing squares of all the numbers
of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
"""


def make_squares(arr):
    squares = []
    left, right = 0, len(arr) - 1
    while left < right:
        if abs(arr[left]) > abs(arr[right]):
            squares.append(arr[left]**2)
            left += 1
        elif abs(arr[left]) < abs(arr[right]):
            squares.append(arr[right] ** 2)
            right -= 1
        else:
            squares.append(arr[right] ** 2)
            squares.append(arr[left] ** 2)
            left += 1
            right -= 1
    if len(arr) % 2 == 1:
        squares.append(arr[left])
    squares.reverse()
    return squares


def main():
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))


main()