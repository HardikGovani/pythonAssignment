#Python program to calculate square of a given number (3 differentways). 

# By multiplying numbers two times: (number*number)
# By using Exponent Operator (**): (number**2)
# By using math.pow() method: (math.pow(number,2) 

import math
def main():
    
    # input a number 
    number = int (input("Enter an integer number: "))
    print("##")
    print("By multiplying numbers two times: (number*number)")
    # calculate square
    square = number*number
    # print
    print ("Square of {0} is {1} ".format(number, square))
    print("##")
    print("By using Exponent Operator (**): (number**2)")
    # calculate square
    square = number**2
    # print
    print ("Square of {0} is {1} ".format(number, square))
    
    print("##")
    print("By using math.pow() method: (math.pow(number,2) ")
    # calculate square
    square = int(math.pow(number, 2))
    # print
    print ("Square of {0} is {1} ".format(number, square))
    

if __name__ == "__main__":
    while True:
        main()