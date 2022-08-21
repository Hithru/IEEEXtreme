# Challenge Name: Caesar Cipher
# Difficulty: Easy

def caesar_cipher(string: str, rotate_factor: int):
    original_alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_alphabet = original_alphabet[rotate_factor:] + original_alphabet[:rotate_factor]
    cipher_dict = {}
    for i in range(26):
        cipher_dict[original_alphabet[i].upper()] = cipher_alphabet[i].upper()
        cipher_dict[original_alphabet[i]] = cipher_alphabet[i]
    answer = ""
    for char in string:
        if char in cipher_dict:
            answer += cipher_dict[char]
        else:
            answer += char

    return answer


print(caesar_cipher("middle-Outz", 2))
print(caesar_cipher("Always-Look-on-the-Bright-Side-of-Life", 11))