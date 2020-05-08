#Python program to convert Centimeter to Inches 

#equ: 1 inch = 2.54 centimeters

def main():
    num = float(input("\nEnter a Distance in Centimeter: "))
    inch = num / 2.54
    print("\nDistance in Inches =" ,inch)

if __name__ == "__main__":
    while True:
        main() 