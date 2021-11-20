"""
Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string.
As we know, when we are not allowed to repeat characters while finding permutations of a string,
we get N! permutations (or anagrams) of a string having N characters.
For example, here are the six anagrams of the string “abc”:

abc
acb
bac
bca
cab
cba

Write a function to return a list of starting indices of the anagrams of the pattern
in the given string.

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc"
"""


def find_string_anagrams(str1, pattern):
    result_indexes = []
    window_start, window_end, pattern_map, str_map = 0, 0, {}, {}
    for i in pattern:
        if i not in pattern_map:
            pattern_map[i] = 0
        pattern_map[i] += 1

    for window_end in range(len(str1)):
        if str1[window_end] not in pattern_map:
            window_start += 1
            str_map = {}
            continue
        else:
            if str1[window_end] not in str_map:
                str_map[str1[window_end]] = 0
            str_map[str1[window_end]] += 1
            while str_map[str1[window_end]] > pattern_map[str1[window_end]]:
                str_map[str1[window_start]] -= 1
                window_start += 1
            if str_map == pattern_map:
                while window_start != window_end + 1:
                    result_indexes.append(window_start)
                    window_start += 1
    return result_indexes


def main():
    print(find_string_anagrams('ppqp', 'pq'))
    print(find_string_anagrams('abbcabc', 'abc'))


main()