#python program to add two Matrices

#manual change mat: 

def main():
    print("Matrices 1")
    print("X = [[1,2,3],[4,5,6],[7,8,9]] \n")

    print("Matrices 2")
    print("Y = [[9,8,7],[6,5,4],[3,2,1]]\n")
   
    X = [[1,2,3],
    [4,5,6],
    [7,8,9]]

    Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]

    result = [[X[i][j] + Y[i][j]  for j in range(len(X[0]))] for i in range(len(X))]
    for r in result:
        print("SUM = ",r)
        
        input() #wait. 

if __name__ == "__main__":
    while True:
        main()
