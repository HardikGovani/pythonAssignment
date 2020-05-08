#Python program to count number of trailing zeros in Factorial of number N 


def findTrailingZeros(n):       
    count = 0
    i = 5
    while (n / i>= 1): 
        count += int(n / i) 
        i *= 5
    return int(count) 

def main():
    num = int(input("\nEnter a Number: "))
    print("Count of trailing 0s "+
    "in", num, " is", findTrailingZeros(num)) 

if __name__ == "__main__":
    while True:
        main() 
        
