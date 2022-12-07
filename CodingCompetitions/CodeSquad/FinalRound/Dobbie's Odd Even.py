number_of_cards = int(input())

cards = list(map(int,input().strip().split()))

odd_cards = 0
even_cards = 0

for card in cards:
    if card%2 == 0:
        even_cards += 1
    else:
        odd_cards += 1
if even_cards > odd_cards:
    print(2*odd_cards+1)
elif even_cards == odd_cards:
    print(even_cards+odd_cards)
else:
    difference = odd_cards - even_cards
    answer = even_cards*2 + 2*(difference//3)
    remainder = difference%3
    if remainder ==1:
        answer -=1
    elif remainder ==2:
        answer +=1
    print(answer)
