#Python program Print all numbers between 1 to 1000 which are divisible by 7 and must not be divisible by 5 

def main():
    print("Numbers from 1000: divisible by 7 and must not be divisible by 5")
    n= 1000
    nl=[]
    for x in range(0, n):
        if (x%7==0) and (x%5!=0):
            nl.append(str(x))
    print (','.join(nl))

if __name__ == "__main__":
    while True:
        main()
        input() #wait
