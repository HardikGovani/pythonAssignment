#Python program to declare any variable without assigning any value. 

def main():
    # declare variable 
    num = None

    # print the value
    print ("value of num: ", num)

    # checking variable
    if (num==None):
        print ("Nothing")
    else:	
        print ("Something")
        
    # assign some value
    num = 100

    # print the value
    print ("value of num: ", num)

    # checking variable
    if (num==None):
        print ("Nothing")
    else:	
        print ("Something")

    input()  #wait

if __name__ == "__main__":
    while True:
        main()
