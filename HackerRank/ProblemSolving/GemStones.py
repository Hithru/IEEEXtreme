# Challenge Name: Gem Stones
# Difficulty: Easy
from typing import List


def gem_stones(arr: List[str]):
    occurrences = {}
    for rocks in arr:
        characters = set(list(rocks))
        for character in characters:
            occurrences.setdefault(character, 0)
            occurrences[character] += 1
    return list(occurrences.values()).count(len(arr))


print(gem_stones(['abcdde', 'baccd', 'eeabg']))
