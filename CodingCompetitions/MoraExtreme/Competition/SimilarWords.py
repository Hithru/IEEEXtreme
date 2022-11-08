from collections import Counter

T = int(input())
while(T>0):
    result = 1
    uniques = 1
    word, N = input().split(' ')
    N = int(N)
    length = len(word)
    word_i = len(word)-2
    while(word_i>=0):
        if(word_i + N + 1 >= length):
            uniques = len(Counter(word[word_i:]))
        else:
            uniques = len(Counter(word[word_i:word_i+N+1]))
        #print(uniques)
        result *= uniques
        word_i-=1
    print(result)
    T-=1