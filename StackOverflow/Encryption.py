def convert_base(number: int, base: int):
    answer = ""
    while number > 0:
        answer = str(number % base) + answer
        number = number // base

    return answer


word = input()
input_base = int(input())

encrypt_string = ""
for character in word:
    encrypt_string = encrypt_string + convert_base(ord(character), input_base)

print(encrypt_string)
