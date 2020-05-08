#Python program for calculating and display simple interest 

def main():
    
    P = float(input("Enter the principal amount : "))
    N = float(input("Enter the number of years : "))
    R = float(input("Enter the rate of interest : "))
    #2
    SI = (P * N * R)/100
    print("Simple interest : {}".format(SI))

if __name__ == "__main__":
    while True:
        main()