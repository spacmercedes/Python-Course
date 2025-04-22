# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter:row.code for (index,row)  in data.iterrows()}
print(dict)

def generate_phonetic():
    wordin = input("Enter a word: ").upper()
    try:
        output_list = [dict[letter] for letter in wordin]
    except KeyError:
        print("Sorry only letters miss girl")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
