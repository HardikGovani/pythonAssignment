#Python program to print Palindrome numbers from the given list_ 

def main():
    # Give size of list
    print("Enter size of list")
    n=int(input())

    print("Enter list element by space separated: ex: 121 234 565 897 etc")
    # Give list of numbers having size n
    l=list(map(int,input().strip().split(' ')))

    print("Palindrome numbers are:")
    # check through the list to check 
    # number is palindrome or not
    for i in l:
        num=str(i)
        if("".join(reversed(num))==num):
            print(i)
    
if __name__ == "__main__":
    while True:
        main()

