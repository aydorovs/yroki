words = ['мадам', 'самолет', 'madam', 'oko']
palindromes = []

for word in words:
    if word == word[::-1]:
        palindromes.append(word)

print(palindromes)

