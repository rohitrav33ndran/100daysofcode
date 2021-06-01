#TODO: Create a letter using starting_letter.txt
import os


#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



def write_letter(name):
    with open("Input/Letters/starting_letter.txt", mode="r") as input_file:
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="a") as output_file:
            for line in input_file:
                if "[name]" in line:
                    fstring = f'{name},'
                    output_file.write(line.replace('[name],',fstring))
                else:
                    output_file.write(line)


with open("Input/Names/invited_names.txt", mode="r") as invites:
    for name in invites:
        trimmed_name = name.rstrip("\n")
        write_letter(trimmed_name)