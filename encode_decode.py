# Encode-Decode Text Game
# Rules:
# 1. The user will be asked to input some text.
# 2. The user can then choose whether to encode or decode the text.
# 3. Encoding and decoding rules:
#    - If the text is 1 character long, it remains unchanged.
#    - If the text is 2 characters long, the characters are reversed for encoding and decoding.
#    - If the text is longer than 2 characters:
#      - For encoding: The first character of the text moves to the end, and 3 random characters are added at the start and end of the encoded text.
#      - For decoding: The random characters are stripped, and the last character of the remaining text is moved to the front to restore the original.
# 4. If the text length is not valid for decoding, it will show an error message.
# 5. The game allows the user to play multiple rounds until they choose to exit.

import string
import random

def generate_char(size):
    return ''.join(random.choice(string.ascii_letters) for choices in range(size))

opt="y"
while(opt=='y'):
    text=input("Enter your text: ")
    print("Choose your option: ")
    print("1. Encode text")
    print("2. Decode text")
    option=input()
    match (option):
        case "1":
            if(len(text)==1):
                print("Your encoded text is: ", text) 
            
            elif(len(text)==2):
                print("Your encoded text is: ",text[::-1])
                
            else:
                start=text[0]
                text=text[1:]+start
                random_start=generate_char(3)
                random_end=generate_char(3)
                new_text=random_start+text+random_end
                print("Your encoded text is: ",new_text)
            
        case "2":
            if(len(text)==1):
                print("Your decoded text is: ",text) 
                
            elif(len(text)==2):
                print("Your decoded text is: ",text[::-1])
                
            elif(len(text)>6):
                new__text=text[3:-3]
                decoded_text = new__text[-1:] + new__text[:-1]
                #new__text[4:5]+new__text[0:4]
                #elloh=h+ello=hello
                print("Your decoded text is: ",decoded_text)
                
            else:
                print("Improper Text!")
        
        case _:
            print("Invalid Input!")

    print("Do you want to play again: (press y for yes)")
    opt=input()
    continue    
            
            
        