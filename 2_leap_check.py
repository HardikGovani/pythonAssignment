#python program to check leap year#

def main():
    year = int(input("\nEnter a year:"))
    if (year % 4) == 0:
        if (year % 100) == 0:
           if (year % 400) == 0:
               print("{0} is a leap year".format(year))
           else:
               print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
       print("{0} is not a leap year".format(year))

if __name__ == "__main__":
    while True:
        main()



