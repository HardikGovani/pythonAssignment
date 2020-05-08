#python program to check whether the input character is an alphabet#

def main():
    char = input("\nEnter a character:")
    if (char>='a' or char>='A')and(char<='Z' or char<='z'):
        print(char + " is a alphabet")
    else:
        print(char + " is not a alphabet")

if __name__ == "__main__":
    while True:
        main()



