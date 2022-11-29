# Problem Number: 380
# Problem Name: Insert Delete GetRandom O(1)
# Difficulty: Medium
from random import random


class RandomizedSet:

    def __init__(self):
        self.valueDict = {}

    def insert(self, val: int) -> bool:
        if val not in self.valueDict:
            self.valueDict[val] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.valueDict:

            return False
        else:
            del self.valueDict[val]
            return True

    def getRandom(self) -> int:
        keys = list(self.valueDict.keys())
        length = len(keys)
        return keys[random.randint(0, length - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()