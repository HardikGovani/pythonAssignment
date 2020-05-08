#Python program to find the factorial of a number using recursion

def main():
    
    # input a number 
    num = int (input("Enter an integer number: "))
    print("Factorial of {0} is: {1} ".format (num, fact(num)))
    # function to calculate the factorial 

def fact(n):
    if n == 0:
        return 1 
    return n * fact(n-1)

if __name__ == "__main__":
    while True:
        main()
