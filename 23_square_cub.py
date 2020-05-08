#Python program to write functions to find square and cube of a given number 

def main():
    number = int(input("\nEnter a number: "))
    # square and cube
    print ("square of {0} is {1}".format(number, square(number)))
    print ("Cube of {0} is {1}".format(number, cube (number)))

#Function to get square:
def  square (num):
	return (num*num)

#Function to get cube:
def  cube (num):
	return (num*num*num)

if __name__ == "__main__":
    while True:
        main()
