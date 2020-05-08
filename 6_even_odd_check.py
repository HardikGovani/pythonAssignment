#Python Program to check even or odd number

def main():

    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))

if __name__ == "__main__":
    while True:
        main()



