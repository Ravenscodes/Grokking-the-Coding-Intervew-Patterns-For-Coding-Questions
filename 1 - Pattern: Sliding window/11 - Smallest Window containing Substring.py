"""
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".
Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""


def find_substring(str1, pattern):
    pattern_map = {}
    for i in pattern:
        if i not in pattern_map:
            pattern_map[i] = 0
        pattern_map[i] += 1

    substr_start, window_start, matched, str_map = 0, 0, 0, {}
    min_length = len(str1) + 1

    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in pattern_map:
            pattern_map[right_char] -= 1
            if pattern_map[right_char] >= 0:
                matched += 1

        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in pattern_map:
                if pattern_map[left_char] == 0:
                    matched -= 1
                pattern_map[left_char] += 1

    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start + min_length]


def main():
    print(find_substring('aabdec', 'abc'))
    print(find_substring('abdbca', 'abc'))
    print(find_substring('adcad', 'abc'))


main()
