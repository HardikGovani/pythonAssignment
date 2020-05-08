#Python program to input age and check eligibility for voting

def main():
    
    # input age
    age = int(input("Enter Age : "))

    # condition to check voting eligibility
    if age>=18:
            status="Eligible"
    else:
        status="Not Eligible"

    print("You are ",status," for Vote.")

if __name__ == "__main__":
    while True:
        main()
