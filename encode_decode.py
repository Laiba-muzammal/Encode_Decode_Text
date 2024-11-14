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
            
            
        
