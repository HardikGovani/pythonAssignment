#Python program to count total number of bits in a number. 

def main():
    n=int(input("Enter Number ::>"))
    totalbits(n)

def totalbits(n):
   binumber = bin(n)[2:]
   print("TOTAL BITS: ",len(binumber)) 
    
if __name__ == "__main__":
    while True:
        main()
