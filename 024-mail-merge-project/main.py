#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
        

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    text = letter.read()

for name in names:
    stripped_name = name.strip()
    new_text = text.replace("[name]", f"{stripped_name}")
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as new_letter:
        new_letter.write(new_text)
