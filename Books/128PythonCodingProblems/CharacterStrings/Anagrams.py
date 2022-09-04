def anagrams(string_array):
    word_dictionary = {}
    for word in string_array:
        sorted_string = "".join(sorted(word))
        if sorted_string in word_dictionary:
            word_dictionary[sorted_string].append(word)
        else:
            word_dictionary[sorted_string] = [word]
    return [word_dictionary[string] for string in word_dictionary if len(word_dictionary[string]) > 1]


print(anagrams(
    ["below", "the", "car", "is", "a", "rat", "drinking", "cider", "and", "bending", "its", "elbow", "while", "this",
     "thing", "is", "an", "arc", "that", "can", "act", "like", "a", "cat", "which", "cried", "during", "the", "night",
     "caused", "by", "pain", "in", "its", "bowel"]))
