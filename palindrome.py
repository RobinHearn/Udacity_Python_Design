# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

from collections import Counter
import itertools


def longest_subpalindrome_slice(text):
    text = text.upper()

    if len(set(text)) == len(text):
        return (0, 0)

    if text == '':
        return (0, 0)

    palindromes = []
    found = 0

    Counter(text)

    for x in set(text):
        if Counter(text)[x] > 1:
            char_match = list(itertools.combinations([pos for pos, char in enumerate(text) if char == x], 2))
            char_match = sorted(char_match, key=lambda sub: -(abs(sub[1] - sub[0])))
            print(char_match)
            for y in range(len(char_match)):
                string1 = text[(char_match[y][0]):(char_match[y][1] + 1)]
                if string1 == string1[::-1]:
                    (i, j) = (char_match[y][0], char_match[y][1] + 1)
                    # (i,j) = (char_match[y][0],char_match[y][1]+1)
                    palindromes.append(tuple([i, j]))
                    print(i, j)
                    break

    longest_palindrome = max(palindromes, key=lambda sub: abs(sub[1] - sub[0]))

    return (longest_palindrome)

    "Return (i, j) such that text[i:j] is the longest palindrome in text."


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


# print test()

print
longest_subpalindrome_slice('Race carr')