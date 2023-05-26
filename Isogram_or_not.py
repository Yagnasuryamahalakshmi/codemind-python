def is_isogram(word):
    word = word.lower()
    unique_chars = set()
    for char in word:
        if char in unique_chars:
            return False
        else:
            unique_chars.add(char)
    return True
input_word = input()
result = is_isogram(input_word)
print(result)