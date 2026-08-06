# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
import pandas
#TODO 1. Create a dictionary in this format:
data=pandas.read_csv("day26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
phenotic_dictionary={row.letter:row.code for (index, row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word=input("Enter a word : ").upper()
# NATO_list=[value for letters in word for(key, value) in phenotic_dictionary.items() if letters==key]my answer and that to corret man
output_list=[phenotic_dictionary[letter] for letter in word]
print(output_list)
