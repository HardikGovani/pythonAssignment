#Python program to convert Decimal to binary

def main():
    # decimal number
    number = int(input("Enter any decimal number: "))
    decimalToBinary(number)
    print("")
    
def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')

if __name__ == "__main__":
    while True:
        main()



