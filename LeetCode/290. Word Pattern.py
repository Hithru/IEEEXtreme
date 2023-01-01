# Problem Number: 290
# Problem Name: Word Pattern
# Difficulty: Easy

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        letter_word_map = {}
        words_letter_map = {}

        for i in range(len(pattern)):
            l = pattern[i]
            if l in letter_word_map:
                if letter_word_map[l] != words[i]:
                    return False
            else:
                if words[i] in words_letter_map:
                    return False
                else:
                    letter_word_map[l] = words[i]
                    words_letter_map[words[i]] = l

        else:
            return True