#Python program to add two binary numbers 

def main():

    num1 = '00001'  #1
    num2 = '00011'  #3
    print("Binary numbers: 00001 + 00011")
    # sum - decimal value 4
    # binary value 00100
    sum1 = bin(int(num1,2) + int(num2,2))
    print("Addition: ",sum1)
    input() #wait. 

if __name__ == "__main__":
    while True:
        main()
