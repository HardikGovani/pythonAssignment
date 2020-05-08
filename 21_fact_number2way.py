#Python program to find factorial of a given number (2 different ways)

# By multiplying numbers two times: (number*number)
# By using Exponent Operator (**): (number**2)
# By using math.pow() method: (math.pow(number,2) 



def main():
    
    # input a number 
    num = int(input("Enter an integer number: "))
    print("Method:1")
    fact =1 
    for i in range (1,num+1) :
        fact = fact*i 
    # print the factorial
    print ("Factorial of {0} is: {1} ".format (num, fact))

    print("Method:2")
    print("Factorial of {0} is: {1} ".format (num, fact_cal(num)))

def fact_cal(n):
    if n == 0:
        return 1 
    return n * fact_cal(n-1)

if __name__ == "__main__":
    while True:
        main()
