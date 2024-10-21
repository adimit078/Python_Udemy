#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Names/invited_names.txt") as file:
    names = file.readlines()
    for i in range(len(names)):
        names[i] = names[i].strip()

with open("./input/Letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names:
        newLetter = letter.replace("[name]", name)
        newFile = open(f"./output/ReadyToSend/{name}Letter.txt", "w")
        newFile.write(newLetter)
        newFile.close()




