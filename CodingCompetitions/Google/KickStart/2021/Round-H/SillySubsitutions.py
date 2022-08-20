test_cases = int(input())

for t in range(test_cases):
    string_length = int(input())
    string = input()

    index = 1
    changes = {"01":"2","12":"3","23":"4","34":"5","45":"6","56":"7","67":"8","78":"9","89":"0","90":"1"}
    while index < len(string)+1:
        if index ==0:
            index +=1
        if string[index-1:index+1] in changes:
            string = string[:index-1] + changes[string[index-1:index+1]]+string[index+1:]
            index -= 1
        else:
            index +=1


    print("Case #{}: {}".format(t + 1, string))