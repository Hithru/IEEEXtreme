# Challenge Name: Palindrome Index
# Difficulty: Easy

def palindrome_index(string: str):
    start_index = 0
    end_index = len(string) - 1
    remove_index = -1

    while start_index < end_index:
        if string[start_index] != string[end_index]:
            if remove_index >= 0:
                print("failed", remove_index)
                return -1
            elif (string[start_index + 1], string[start_index + 2]) == (string[end_index], string[end_index - 1]):
                remove_index = start_index
                start_index = start_index + 1
            elif (string[start_index], string[start_index + 1]) == (string[end_index - 1], string[end_index - 2]):
                remove_index = end_index
                end_index = end_index - 1
            else:
                return -1
            continue
        start_index += 1
        end_index -= 1
    print("success")
    return remove_index


print(palindrome_index("hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"))
