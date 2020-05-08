#Python program to print numbers from N to 1 (use range() with reverse order) 

def main():
    print("")
    n=int(input("Enter n value:"))
    for i in range(n,0,-1):
        print(i,end=" ")

if __name__ == "__main__":
    while True:
        main()
