N = int(input("Введіть кількість слів: "))

words = []

for i in range(N):
    word = input(f"Введіть слово {i + 1}: ")
    sp_word = ' '.join(word)
    words.append(sp_word)

result = ', '.join(words)

print("Результат: ", result)