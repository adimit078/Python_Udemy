student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

{"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
letter_dict = {row.letter:row.code for (index,row) in nato.iterrows()}

word_list = list(input("Enter a word please: "))
new_list = [letter_dict[item.upper()] for item in word_list]
print(new_list)
