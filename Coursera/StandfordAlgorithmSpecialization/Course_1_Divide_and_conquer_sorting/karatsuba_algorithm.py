import math


def karatsuba_algorithm(first_number: int, second_number: int):
    if len(str(first_number)) == 1 or len(str(second_number)):
        return first_number * second_number
    else:
        length = max(len(str(first_number)), len(str(second_number)))
        half_length = math.ceil(length / 2)

        first_number_first_part = int(str(first_number)[:half_length])
        first_number_second_part = int(str(first_number)[half_length:])
        second_number_first_part = int(str(second_number)[:half_length])
        second_number_second_part = int(str(second_number)[half_length:])

        first_term = karatsuba_algorithm(first_number_first_part, second_number_first_part)
        last_term = karatsuba_algorithm(first_number_second_part, second_number_second_part)
        middle_term = karatsuba_algorithm((first_number_first_part + first_number_second_part), (
                second_number_first_part + second_number_second_part)) - first_term - last_term
        return 10 ** (2 * half_length) * first_term + 10 ** half_length * middle_term + last_term


print(karatsuba_algorithm(3141592653589793238462643383279502884197169399375105820974944592,
                          2718281828459045235360287471352662497757247093699959574966967627))
print(karatsuba_algorithm(12345, 6789))
