# Challenge Name: Happy Lady Bugs
# Difficulty: Easy

def happy_ladybugs(b):
    ladybug_colours = {}
    ladybug_colours.setdefault('_', 0)

    for i in b:
        ladybug_colours.setdefault(i, 0)
        ladybug_colours[i] += 1

    if ladybug_colours["_"] > 0:
        for k, v in ladybug_colours.items():
            if k != "_" and v <= 1:
                return "NO"
        else:
            return "YES"
    else:
        if len(b) == 1:
            # When only one element is present which is not "_"  return "NO"
            return "NO"
        elif b[0] != b[1] or b[len(b) - 1] != b[len(b) - 2]:
            # Check first and final characters are happy if not return "NO"
            return "NO"
        else:
            for j in range(1, len(b) - 1):
                # Check characters excluding first and last are happy if not return "NO"
                if b[j] != b[j - 1] and b[j] != b[j + 1]:
                    return "NO"
            else:
                # if every character is happy return "YES"
                return "YES"


print(happy_ladybugs("BAAAB"))
print(happy_ladybugs("B_RRBR"))
print(happy_ladybugs("_"))
print(happy_ladybugs("G"))
print(happy_ladybugs("B"))
