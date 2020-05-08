#Python program to print ASCII value of a character

def main():
    
    ch = input("Enter a character: ")
    print("The ASCII value of '" + ch + "' is", ord(ch))

if __name__ == "__main__":
    while True:
        main()
