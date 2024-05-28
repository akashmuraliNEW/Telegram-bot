import string

vowel = ['a','e','i','o','u']
alphabets = []

for i in string.ascii_lowercase:
    alphabets.append(i)
const = [items for items in alphabets if  items not in vowel]
print(const)

value = input('enter a string')