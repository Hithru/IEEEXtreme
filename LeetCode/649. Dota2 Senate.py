# Problem Number: 649
# Problem Name: Dota2 Senate
# Difficulty: Medium
class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r_baned = 0
        d_baned = 0

        r_left = 0
        d_left = 0
        if senate[0] == "R":
            d_baned = 1
            r_left += 1
        else:
            r_baned = 1
            d_left = 1

        left = [senate[0]]

        run = True

        members = senate[1:]
        while run:
            print(members)
            run = False
            for k in members:
                if k == "R":
                    if r_baned > 0:
                        r_baned -= 1
                    else:
                        d_baned += 1
                        r_left += 1
                        left.append("R")
                else:
                    if d_baned > 0:
                        d_baned -= 1
                    else:
                        r_baned += 1
                        d_left += 1
                        left.append("D")
            if r_left == 0:
                return "Dire"
            elif d_left == 0:
                return "Radiant"
            else:
                r_left = 0
                d_left = 0
                members = left
                left = []
                run = True


