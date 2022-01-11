'''
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20x20 grid?
'''

def main():

    # get data from file
    with open('11_grid.txt') as file:
        lines = file.readlines()

    file.close()

    # create 20x20 array from data
    grid = [ [0] * 20 for i in range(20)]
    for i in range(0, 20):
        line = lines[i].split()
        for j in range(0, 20):
            grid[i][j] = int(line[j])

    # calculate horizontal and vertical max
    max = 0
    
    for i in range(0, 20):
        for j in range(0, 17):
            
            horz_p = grid[i][j]
            vert_p = grid[j][i]

            for k in range(1, 4):
                horz_p *= grid[i][j+k]
                vert_p *= grid[j+k][i]
            
            if horz_p > max:
                max = horz_p
            
            if vert_p > max:
                max = vert_p
            

    # calculate diagonal max        
    for i in range(0, 17):
        for j in range(0, 17):
            
            diag_1 = grid[i][j]
            diag_2 = grid[i+3][j]

            for k in range(1, 4):
                diag_1 *= grid[i+k][j+k]
                diag_2 *= grid[i+3-k][j+k]

            if diag_1 > max:
                max = diag_1

            if diag_2 > max:
                max = diag_2

    print(max)  # 70600674


if __name__ == "__main__":
    main()