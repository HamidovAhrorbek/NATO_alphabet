import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
print(data.to_dict())

phenetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phenetic_dict)

word = input("Enter a word: ").upper()
output_list = [phenetic_dict[letter] for letter in word]
print(output_list)
