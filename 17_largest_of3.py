#Python program to find largest of three numbers 

def main():
    num1 = int(input("\nEnter a number1: "))
    num2 = int(input("\nEnter a number2: "))
    num3 = int(input("\nEnter a number3: "))

    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    print("The largest number is", largest)

if __name__ == "__main__":
    while True:
        main()
