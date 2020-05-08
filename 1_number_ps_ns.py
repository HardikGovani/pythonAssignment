#python program to check if a number is positive or negative#

def main():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number \n")
    elif num == 0:
        print("Zero \n")
    else:
       print("Negative number \n")

if __name__ == "__main__":
    while True:
        main() 