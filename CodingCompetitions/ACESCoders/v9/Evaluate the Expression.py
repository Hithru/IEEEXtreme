stack = []

operation = input().strip()

while operation != "#":
    stack.append(operation)
    operation = input().strip()

# print(stack)
start_tag_index = []
i = 0
while i < len(stack):
    # print(stack)
    word = stack[i]
    if word == "{+}" or word == "{*}" or word == "{-}":
        start_tag_index.append(i)

    if word == "{/+}" or word == "{/*}" or word == "{/-}":
        start = start_tag_index.pop()
        elements = stack[start + 1:i]
        elements_length = len(elements)

        new_element = int(elements[0])

        for k in range(1, elements_length):

            if stack[start] == "{+}":
                new_element += int(elements[k])
            elif stack[start] == "{-}":
                new_element -= int(elements[k])
            else:
                new_element *= int(elements[k])
        stack[start] = new_element
        stack = stack[:start + 1] + stack[i + 1:]
        i -= elements_length
        i -= 1

    i += 1

print(stack[-1] % (10 ** 9 + 7))
