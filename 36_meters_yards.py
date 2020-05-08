#Python program to convert meters into yards 

#equ: 1 meter = 1.094 yards

def main():
    num = float(input("\nEnter a Distance in METER: "))
    yd = num * 1.094
    print("\nDistance in Yards =" ,yd)

if __name__ == "__main__":
    while True:
        main() 