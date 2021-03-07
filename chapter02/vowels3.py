vowels = ['a', 'e', 'i', 'o', 'u']
found = []
word = input("Provide a word to srearch for vowels: ")
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print()
for vowel in found:
    print(vowel)

for vowel in found:
    print(vowel)

# 可以使用insert 把一个对象插入到列表的末尾
# found.insert(2, 4)
# temp = found.pop(2)
# print("temp = ", temp)
