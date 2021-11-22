"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
"""


def search_triplets(arr):
    triplets = []
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pair(arr, -arr[i], i+1, triplets)
    return triplets


def search_pair(arr, target_sum, next_index, triplets):
    left, right = next_index, len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target_sum:
            triplets.append([arr[next_index-1], arr[left], arr[right]])
            left += 1
            right -= 1
        elif arr[left] + arr[right] > target_sum:
            right -= 1
        else:
            left += 1


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
