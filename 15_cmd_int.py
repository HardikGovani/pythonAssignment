#Python program for calculating and display compound interest

def main():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the interest rate: "))
    t = float(input("Enter the time in years: "))
    amount = compound_interest(p, r, t)
    interest = amount - p
    print("Compound amount is %.2f" % amount)
    print("Compound interest is %.2f" % interest)    

def compound_interest(principle, rate, time):
    result = principle * (pow((1 + rate / 100), time))
    return result


if __name__ == "__main__":
    while True:
        main()
