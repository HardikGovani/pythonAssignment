#Generate random integers between 0 and 9 in Python 

import random
def main():
    print("Random number by random import: ")
    print(random.randint(0,9))
    print("END- press Enter for new one")
    input() #wait
    
if __name__ == "__main__":
    while True:
        main()

