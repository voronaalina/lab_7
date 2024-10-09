user_input = input("Введіть символи: ")

def count_lett_dig(input_string):
    letters_count = 0
    digits_count = 0
    for symbol in input_string:
        if symbol.isalpha():
            letters_count += 1
        elif symbol.isdigit():
            digits_count += 1
    return letters_count, digits_count

letters, digits = count_lett_dig(user_input)

print("Кількість літер: ", letters)
print("Кількість цифр: ", digits)