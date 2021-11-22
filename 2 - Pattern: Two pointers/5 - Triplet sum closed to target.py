"""
Given an array of unsorted numbers and a target number,
find a triplet in the array whose sum is as close to the target number as possible,
return the sum of the triplet. If there are more than one such triplet,
return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    greatest_sum = arr[0] + arr[1] + arr[2]
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        greatest_sum = find_pair(arr, i + 1, -arr[i] + target_sum, greatest_sum)
        if greatest_sum == target_sum:
            return target_sum
    return greatest_sum


def find_pair(arr, next_index, target_sum, greatest_sum):
    left, right = next_index, len(arr) - 1
    while left < right:
        tmp_sum = arr[left] + arr[right]
        if tmp_sum == target_sum:
            return target_sum
        elif tmp_sum > target_sum:
            right -= 1
        elif tmp_sum < target_sum and tmp_sum + arr[next_index - 1] < greatest_sum:
            left += 1
        else:
            greatest_sum = tmp_sum + arr[next_index - 1]
            left += 1
    return greatest_sum


def main():
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
