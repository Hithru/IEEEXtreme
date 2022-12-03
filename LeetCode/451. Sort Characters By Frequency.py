# Problem Number: 451
# Problem Name: Sort Characters By Frequency
# Difficulty: Medium

class Solution:
    def frequencySort(self, s: str) -> str:
        characters = {}
        for i in s:
            characters.setdefault(i, 0)
            characters[i] += 1


        print(characters)
        sorted_characters = sorted(characters.items(), key=lambda kv: kv[1], reverse=True)
        print(sorted_characters)
        keys = [tup[0] * tup[1] for tup in sorted_characters]
        print(keys)
        return "".join(keys)