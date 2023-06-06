string=input().split()
vowel_count=[sum(char.lower()in'aeiou'for char in word)for word in string]
print(*vowel_count)