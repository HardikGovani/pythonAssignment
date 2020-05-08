#Python program to print Odd and Even numbers from the list of integers. 

def main():
    # list of numbers 
    print("List of numbers: list1 = [1,2,3,4,5,6,7,8,9,10]")
    list1 = [1,2,3,4,5,6,7,8,9,10]
    even_list = []
    odd_list = []
    # iterating each number in list 
    for num in list1: 
        # checking condition 
        if num % 2 == 0: 
            even_list.append(num)
        else:
            odd_list.append(num)
    print("Even Numbers", even_list)
    print("Odd Numbers", odd_list)
    input() #wait

if __name__ == "__main__":
    while True:
        main()
