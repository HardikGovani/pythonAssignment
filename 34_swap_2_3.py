#Python program for swapping the value of two integers and also for swapping the value  of two integers without third variable 

def main():
    
    print("\nSelect SWAP CASE: \nCASE 1 --> Using Third Variable. \nCASE 2 --> Not Using Third Variable")
    num = int(input("Enter a CASE: "))

    if num == 1:
       print("CASE 1 SELECTED:") 
       num1 = int(input("Enter a NUMBER A:"))
       num2 = int(input("Enter a NUMBER B:"))
       num3 = num1
       num1 = num2
       num2 = num3
       print("\nNUMBER AFTER SWAPPING:")
       print("NUMBER A= ",num1, "NUMBER B= ",num2)
    elif num ==2:
       num1 = int(input("Enter a NUMBER A:"))
       num2 = int(input("Enter a NUMBER B:"))
       num1 = num1 + num2
       num2 = num1 - num2
       num1 = num1 - num2       
       print("\nNUMBER AFTER SWAPPING:")
       print("NUMBER A= ",num1, "NUMBER B= ",num2)
    else:
        print("OOPS!! TRY AGAIN")

if __name__ == "__main__":
    while True:
        main()
