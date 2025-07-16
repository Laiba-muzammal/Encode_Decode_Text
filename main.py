
# ===== main.py =====
from encoder import encode
from decoder import decode

opt = "y"
while opt.lower() == 'y':
    text = input("Enter your text: ")
    print("Choose your option:")
    print("1. Encode text")
    print("2. Decode text")
    option = input()

    if option == "1":
        print("Your encoded text is:", encode(text))
    elif option == "2":
        print("Your decoded text is:", decode(text))
    else:
        print("Invalid Input!")

    opt = input("Do you want to play again? (press y for yes): ")
