# As A Junior developer working on a text analysis project
# Display consonants in a sentence as while skipping vowels
# Also skip non-alphabetic characterss
x = input()
v = "aeiouAEIOU"
for i in x:
    if i.isalpha():
        if i not in v:
            print(i, end=" ")
