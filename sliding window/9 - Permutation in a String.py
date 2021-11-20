"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string.
For example, “abc” has the following six permutations:

abc
acb
bac
bca
cab
cba

If a string has ‘n’ distinct characters, it will have n! permutations.

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


def find_permutation(str1, pattern):
    pattern_map = {}
    for i in pattern:
        if i not in pattern_map:
            pattern_map[i] = 0
        pattern_map[i] += 1

    window_start, window_end, character_map = 0, 0, {}
    for window_end in range(len(str1)):
        if str1[window_end] not in pattern_map:
            window_start += 1
            character_map = {}
            continue
        else:
            if str1[window_end] not in character_map:
                character_map[str1[window_end]] = 0
            character_map[str1[window_end]] += 1
            if character_map == pattern_map:
                return True
            if character_map[str1[window_end]] > pattern_map[str1[window_end]]:
                character_map[str1[window_start]] -= 1
                window_start += 1
    return False


def main():
    print(find_permutation('oidbcaf', 'abc'))
    print(find_permutation('odicf', 'dc'))
    print(find_permutation('bcdxabcdy', 'bcdyabcdx'))
    print(find_permutation('aaacb', 'abc'))

main()