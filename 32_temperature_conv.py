#Python program to convert temperature from Celsius to Fahrenheit and vice-versa 

###Celsius to Fahrenheit:  °C= (5/9)*(°F-32)
###Fahrenheit to Celsius:  °F= (9/5)*(°C) + 32 

def Celsius_to_Fahrenheit(c):
    f = (9/5)*c + 32
    return f
    
# Define a function to convert
# Fahrenheit temperature to Celsius
def Fahrenheit_to_Celsius(f) :
    c = (5/9)*(f - 32)
    return c

def main():
    # input a number 
    print("Enter 1 for Celsius to Fahrenheit")
    print("Enter 2 for Fahrenheit to Celsius")
    num = int(input())
    
    if num == 1:
      print("Enter temperature in Celsius: ")
      tmp = float(input())
      print(tmp, "degree celsius is equal to:",Celsius_to_Fahrenheit(tmp),"Fahrenheit")
    elif num == 2:
      print("Enter temperature in Fahrenheit: ")
      tmp = float(input())
      print(tmp,"Fahrenheit is equal to:",Fahrenheit_to_Celsius(tmp),"degree celsius")
    else:
      print("You are fool!!")
      pass

# Driver Code
if __name__ == "__main__":
    while True:
        main() 
