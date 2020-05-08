#python program to check if number is prime or not#

def main():
    
    num = int(input("Enter a number: "))
    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number\n")
               #print(i,"times",num//i,"is",num)
               break
       else:
           print(num,"is a prime number\n")
           
    # if input number is less than
    # or equal to 1, it is not prime
    else:
       print(num,"is not a prime number\n")

if __name__ == "__main__":
    while True:
        main()



